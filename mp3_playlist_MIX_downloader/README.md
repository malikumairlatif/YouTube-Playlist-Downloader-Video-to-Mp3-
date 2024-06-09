# YouTube-Playlist-Downloader (Video-to-Mp3)
This python script enables to download entire playlist from YouTube into Mp3 format. Best for music downloads.

<ol>
<li>
<p><strong>Dependencies and Imports</strong>:</p>
<ul>
<li><code>pytube</code>: To download videos from YouTube.</li>
<li><code>pydub</code>: To handle audio conversion.</li>
<li><code>tqdm</code>: To create a progress bar for each download.</li>
</ul>
</li>
<li>
<p><strong>Functions</strong>:</p>
<ul>
<li><code>download_playlist(playlist_url, download_path)</code>: This function downloads all the videos in a YouTube playlist as audio files and saves them in the specified download path.</li>
<li><code>Playlist(playlist_url)</code>: This function creates a Playlist object representing the YouTube playlist specified by the <code>playlist_url</code>.</li>
<li><code>os.path.exists(download_path)</code>: This function checks if the specified download path exists on the system.</li>
<li><code>os.makedirs(download_path)</code>: This function creates the specified download path if it does not already exist.</li>
<li><code>enumerate(playlist.videos, start=1)</code>: This function iterates over the videos in the playlist, starting from index 1.</li>
<li><code>video.streams.filter(only_audio=True, file_extension='mp4').first()</code>: This function filters the available streams to select the first stream that contains only audio and has an MP4 file extension.</li>
<li><code>os.path.getsize(audio_file)</code>: This function returns the size of the specified file in bytes.</li>
<li><code>tqdm(total=total_size, unit='B', unit_scale=True, desc=video.title, ascii=True)</code>: This function creates a progress bar to visualize the download progress of the audio file.</li>
<li><code>open(audio_file, 'rb')</code>: This function opens the audio file in binary read mode.</li>
<li><code>AudioSegment.from_file(audio_file).export(mp3_file, format="mp3", bitrate="320k")</code>: This function converts the downloaded audio file to MP3 format with a bitrate of 320kbps.</li>
<li><code>os.remove(audio_file)</code>: This function deletes the original audio file after it has been successfully converted to MP3 format.</li>
</ul>
</li>
<li>
<p><strong>Main Logic</strong>:</p>
<ul>
<li>Prompts the user for the YouTube playlist URL and download directory.</li>
<li>Downloads the playlist, converts each audio stream to MP3 at 320kbps, and saves it to the specified directory.</li>
</ul>
</li>
</ol>
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
