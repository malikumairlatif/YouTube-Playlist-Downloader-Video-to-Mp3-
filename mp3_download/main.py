from pytube import Playlist, exceptions
from pydub import AudioSegment
from tqdm import tqdm
import os


def download_playlist(playlist_url, download_path):
    playlist = Playlist(playlist_url)

    # Ensure the download path exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    index = 1
    for video in playlist.videos:
        # Add a blank line before each new download
        print()

        print(f"Downloading {video.title}...")
        try:
            audio_stream = video.streams.filter(only_audio=True, file_extension='mp4').first()
            if audio_stream:
                # Start downloading
                audio_file = audio_stream.download(output_path=download_path, filename_prefix=f"{index:02d}_")

                # Get the file size
                total_size = os.path.getsize(audio_file)
                progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=video.title, ascii=True)

                # Update the progress bar while downloading
                with open(audio_file, 'rb') as file:
                    for chunk in iter(lambda: file.read(4096), b''):
                        progress_bar.update(len(chunk))
                progress_bar.close()

                mp3_file = os.path.splitext(audio_file)[0] + ".mp3"

                # Convert to mp3 with 320kbps bitrate
                try:
                    AudioSegment.from_file(audio_file).export(mp3_file, format="mp3", bitrate="320k")
                    os.remove(audio_file)
                    print(f"Downloaded and converted {video.title} to MP3.")
                except Exception as e:
                    print(f"Failed to convert {video.title}: {e}")
            else:
                print(f"Failed to find audio stream for {video.title}.")

            # Increment the index for successful downloads
            index += 1
        except exceptions.AgeRestrictedError as e:
            print(f"Skipping age-restricted video: {video.title}")


if __name__ == "__main__":
    playlist_url = input("Enter YouTube playlist URL: ")
    download_path = input("Enter download destination path: ")

    download_playlist(playlist_url, download_path)
