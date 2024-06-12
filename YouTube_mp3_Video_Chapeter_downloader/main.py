import os
import logging
import time
from pytube import YouTube, exceptions
from pydub import AudioSegment
from tqdm import tqdm
import yt_dlp as youtube_dl

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_embedded_chapters(video_url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        chapters = info_dict.get("chapters", [])
        chapter_list = []
        if chapters:
            for chapter in chapters:
                start_time = chapter.get("start_time")
                title = chapter.get("title")
                end_time = chapter.get("end_time")
                if start_time is not None and title is not None:
                    chapter_list.append((start_time, title, end_time))
        return chapter_list

def convert_to_mp3(audio_segment, mp3_file, start_time, end_time=None):
    try:
        if end_time:
            chapter_audio = audio_segment[start_time * 1000: end_time * 1000]
        else:
            chapter_audio = audio_segment[start_time * 1000:]

        chapter_audio.export(mp3_file, format="mp3", bitrate="320k")
        logging.info(f"Converted to MP3: {mp3_file}")
    except Exception as e:
        logging.error(f"Error converting to MP3: {e}")

def prompt_user_for_chapters():
    logging.info("No valid chapters found. Please enter timestamps with chapter names in the format 'mm:ss - Title':")
    logging.info("Enter an empty line to finish.")
    chapters = []
    while True:
        user_input = input()
        if not user_input.strip():
            break
        try:
            time_str, title = user_input.split(" - ")
            parts = time_str.split(":")
            if len(parts) == 2:
                start_time = int(parts[0]) * 60 + int(parts[1])
            elif len(parts) == 3:
                start_time = int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
            else:
                raise ValueError("Invalid time format.")
            chapters.append((start_time, title.strip()))
        except ValueError:
            logging.error("Invalid format. Please enter in the format 'mm:ss - Title'.")
    return chapters

def download_video(video, download_path, video_url, retries=3):
    try:
        logging.info(f"Downloading {video.title}...")
        audio_stream = video.streams.filter(only_audio=True, file_extension='mp4').first()
        if audio_stream:
            audio_file = audio_stream.download(output_path=download_path)
            audio_segment = AudioSegment.from_file(audio_file)
            os.remove(audio_file)

            chapters = get_embedded_chapters(video_url)
            if not chapters:
                chapters = prompt_user_for_chapters()

            if chapters:
                for chapter_index, (start_time, title, end_time) in enumerate(chapters):
                    chapter_name = f"{chapter_index:02d}_{title}.mp3"
                    mp3_file = os.path.join(download_path, chapter_name)
                    logging.info(f"{chapter_index:02d}_Converting chapter: {title}...")
                    convert_to_mp3(audio_segment, mp3_file, start_time, end_time)
            else:
                logging.info("No valid chapters found. Converting the entire video.")
                mp3_file = os.path.join(download_path, f"{video.title}.mp3")
                audio_segment.export(mp3_file, format="mp3", bitrate="320k")
                logging.info(f"Downloaded and converted {video.title} to MP3.")
        else:
            logging.error(f"Failed to find audio stream for {video.title}.")
    except exceptions.AgeRestrictedError as e:
        logging.error(f"Skipping age-restricted video: {video.title}")
    except Exception as e:
        if retries > 0:
            logging.warning(f"Error downloading {video.title}: {e}. Retrying ({retries} attempts left)...")
            time.sleep(5)  # Wait a bit before retrying
            download_video(video, download_path, video_url, retries - 1)
        else:
            logging.error(f"Failed to download {video.title} after multiple attempts: {e}")

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    download_path = input("Enter download destination path: ")

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    try:
        video = YouTube(video_url)
        download_video(video, download_path, video_url)
    except exceptions.PytubeError as e:
        logging.error(f"Error initializing YouTube video: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
