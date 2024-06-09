from pytube import Playlist, YouTube, exceptions
from pydub import AudioSegment
from tqdm import tqdm
import os
import time
import re
import ssl
import requests
import json
import socket
import concurrent.futures


def download_video(video, index, download_path):
    try:
        print(f"{index:02d}_Downloading {video.title}...")
        audio_stream = video.streams.filter(only_audio=True, file_extension='mp4').first()
        if audio_stream:
            audio_file = audio_stream.download(output_path=download_path, filename_prefix=f"{index:02d}_")
            total_size = os.path.getsize(audio_file)
            progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=video.title, ascii=True)
            with open(audio_file, 'rb') as file:
                for chunk in iter(lambda: file.read(4096), b''):
                    progress_bar.update(len(chunk))
            progress_bar.close()
            mp3_file = os.path.splitext(audio_file)[0] + ".mp3"
            try:
                AudioSegment.from_file(audio_file).export(mp3_file, format="mp3", bitrate="320k")
                os.remove(audio_file)
                print(f"Downloaded and converted {video.title} to MP3.")
            except Exception as e:
                print(f"Failed to convert {video.title}: {e}")
        else:
            print(f"Failed to find audio stream for {video.title}.")
    except exceptions.AgeRestrictedError:
        print(f"Skipping age-restricted video: {video.title}")
    except (socket.gaierror, exceptions.PytubeError) as e:
        print(f"Network-related error: {e}. Retrying...")
    except Exception as e:
        print(f"Failed to download {video.title}: {e}")


def get_mix_videos(mix_url):
    print(f"Fetching Mix videos from: {mix_url}")
    video_urls = []
    try:
        response = requests.get(mix_url)
        if response.status_code == 200:
            html = response.text
            video_ids = re.findall(r'"videoId":"(.*?)"', html)
            video_urls = [f"https://www.youtube.com/watch?v={video_id}" for video_id in video_ids]
            video_urls = list(dict.fromkeys(video_urls))  # Remove duplicates
            print(f"Found {len(video_urls)} videos in the Mix.")
        else:
            print(f"Failed to fetch Mix videos. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error while fetching Mix videos: {e}")
    return video_urls


def download_video_with_retries(video, index, download_path, retries=3):
    for attempt in range(retries):
        try:
            download_video(video, index, download_path)
            break
        except Exception as e:
            print(f"Error downloading {video.title}: {e}. Retrying ({attempt + 1}/{retries})...")
            time.sleep(2)  # Wait a bit before retrying
            if attempt == retries - 1:
                print(f"Failed to download {video.title} after {retries} attempts. Will retry later.")
                return False  # Indicate that this video needs to be retried later
    return True  # Indicate successful download


def download_playlist_or_mix(url, download_path):
    start_time = time.time()

    if not os.path.exists(download_path):
        os.makedirs(download_path)
    index = 1
    videos = []
    video_urls = []

    try:
        if 'list=' in url:
            if 'RD' in url or 'RDMM' in url:
                video_urls = get_mix_videos(url)
            else:
                playlist = Playlist(url)
                video_urls = playlist.video_urls
            print(f"Found {len(video_urls)} videos in the playlist/mix.")
        else:
            video = YouTube(url)
            video_urls = [url]
    except (ssl.SSLError, exceptions.PytubeError) as e:
        print(f"Error retrieving playlist or mix: {e}")
        return

    if not video_urls:
        print("No videos found. Please check the URL and try again.")
        return

    videos = [YouTube(video_url) for video_url in video_urls]

    failed_videos = []
    for video in videos:
        print()
        if not download_video_with_retries(video, index, download_path):
            failed_videos.append((video, index))
        index += 1

    # Retry failed videos
    if failed_videos:
        print("Retrying failed videos...")
        for video, idx in failed_videos:
            download_video_with_retries(video, idx, download_path, retries=5)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total elapsed time: {elapsed_time:.2f} seconds.")


if __name__ == "__main__":
    url = input("Enter YouTube playlist or Mix URL: ")
    download_path = input("Enter download destination path: ")
    download_playlist_or_mix(url, download_path)
