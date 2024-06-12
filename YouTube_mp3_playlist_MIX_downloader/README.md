# YouTube-Playlist & Mix-Downloader (Video-to-Mp3)
This python script enables to download entire playlist or YouTube Mix videos from YouTube into Mp3 format. Best for music downloads.

# YouTube Playlist/Mix Downloader

This script downloads audio streams from YouTube playlists or Mixes, converts them to MP3 format, and saves them to a specified directory.

## Features

- Downloads audio streams from YouTube playlists and Mixes.
- Converts downloaded audio files to MP3 format using `pydub`.
- Displays a progress bar for each download using `tqdm`.
- Handles retries for network-related errors and other exceptions.
- Measures and displays the total elapsed time for the download process.

## Dependencies

- **pytube**: A lightweight, Pythonic library for downloading YouTube videos.
- **pydub**: A library for audio manipulation, used here to convert audio files to MP3 format.
- **tqdm**: A library to provide a progress bar for downloads.
- **os**: Standard library module for interacting with the operating system, used for file operations.
- **time**: Standard library module for handling time-related tasks, used to measure elapsed time and implement retries.
- **re**: Standard library module for regular expressions, used to parse video IDs from HTML.
- **ssl**: Standard library module for SSL-related tasks, used to handle SSL errors.
- **requests**: A popular HTTP library for making network requests.
- **socket**: Standard library module for low-level network interface, used to handle network errors.

## Functions

- **download_video(video, index, download_path)**: Downloads and converts a single video.
- **get_mix_videos(mix_url)**: Fetches video URLs from a YouTube Mix URL.
- **download_video_with_retries(video, index, download_path, retries=3)**: Retries downloading a video on failure.
- **download_playlist_or_mix(url, download_path)**: Downloads all videos in a playlist or mix.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/youtube-playlist-mix-downloader.git
   cd youtube-playlist-mix-downloader
   
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure your requirements.txt contains:
    ```bash
   pytube
   pydub
   tqdm
   requests

## Usage:
1.  Run the script:
   ```bash
   python download_youtube.py
```

2.  Enter the YouTube playlist or Mix URL when prompted.
3.  Enter the download destination path when prompted.


   
<h3>Step 1: Install <code>ffmpeg</code></h3>
<ol>
<li>
<p><strong>Windows</strong>:</p>
<ul>
<li>Download the <code>ffmpeg</code> build for Windows from <a href="https://ffmpeg.org/download.html" target="_new" rel="noreferrer">FFmpeg.org</a>.</li>
<li>Extract the downloaded zip file.</li>
<li>Move the <code>bin</code> folder (which contains <code>ffmpeg.exe</code>) to a convenient location, for example, <code>C:\ffmpeg\bin</code>.</li>
</ul>
</li>
<li>
<p><strong>MacOS</strong>:</p>
<ul>
<li>
<p>Install <code>ffmpeg</code> using Homebrew:Install <code>ffmpeg</code> using your package manager, for example, on Ubuntu:</p>
<p><code class="hljs language-markdown"><span class="hljs-code">brew install ffmpeg</span></code></p>
</li>
</ul>
</li>
<li>
<p><strong>Linux</strong>:</p>
</li>
</ol>
<p style="padding-left: 80px;"><code class="hljs language-markdown"><span class="hljs-code">sudo apt update<br />sudo apt install ffmpeg</span></code></p>
<h3>Step 2: Add <code>ffmpeg</code> to System PATH</h3>
<ol>
<li>
<p><strong>Windows</strong>:</p>
<ul>
<li>Open the Start Search, type in "env", and select "Edit the system environment variables."</li>
<li>In the System Properties window, click on the "Environment Variables" button.</li>
<li>In the Environment Variables window, under System variables, find the PATH variable, select it, and click Edit.</li>
<li>Click New and add the path to the <code>ffmpeg</code> bin directory, e.g., <code>C:\ffmpeg\bin</code>.</li>
<li>Click OK to close all the windows.</li>
</ul>
</li>
<li>
<p><strong>MacOS and Linux</strong>:</p>
<ul>
<li>Open your terminal and add <code>ffmpeg</code> to your PATH by editing your shell configuration file (<code>.bashrc</code>, <code>.zshrc</code>, etc.):</li>
</ul>
</li>
</ol>
<p style="padding-left: 80px;"><code class="hljs language-markdown"><span class="hljs-code"><span class="hljs-built_in">export</span> PATH=<span class="hljs-string">"/usr/local/bin:<span class="hljs-variable">$PATH</span>"</span></span></code></p>
<ul>
<li style="list-style-type: none;">
<ul>
<li>Save the file and source it:</li>
</ul>
</li>
</ul>
<p style="padding-left: 80px;"><code class="hljs language-markdown"><span class="hljs-code"><span class="hljs-built_in">source ~/.bashrc <span class="hljs-comment"># or source ~/.zshrc</span></span></span></code></p>
<h3>Step 3: Verify <code>ffmpeg</code> Installation</h3>
<p>To ensure that <code>ffmpeg</code> is properly installed and accessible from your PATH, open a terminal or command prompt and run:</p>
<p style="padding-left: 80px;"><code class="hljs language-markdown"><span class="hljs-code"><span class="hljs-built_in">ffmpeg -version </span></span></code></p>
<p>You should see the <code>ffmpeg</code> version information printed, indicating that it's correctly installed.</p>
