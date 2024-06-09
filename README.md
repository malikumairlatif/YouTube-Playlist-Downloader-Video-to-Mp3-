# YouTube MP3 Downloader

A Python-based YouTube MP3 Downloader that allows you to download audio from YouTube videos or playlists and convert them to MP3 format.

## Features

- Download audio from individual YouTube videos or entire playlists.
- Convert downloaded audio to MP3 format.
- Display download progress.
- Retry mechanism for failed downloads.
- Skip age-restricted content.
- Organize and save downloaded files to a specified directory.

## Dependencies

This project requires the following Python libraries:

- `pytube`: For downloading YouTube videos.
- `pydub`: For converting audio files.
- `tqdm`: For displaying download progress.
- `requests`: For making HTTP requests.
- `ffmpeg`: Required by `pydub` for audio conversion.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/youtube-mp3-downloader.git
   cd youtube-mp3-downloader
   
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

## Contributing
Contributions are welcome! Please fork this repository and submit pull requests with your changes. Make sure to follow the coding standards and add appropriate documentation.
