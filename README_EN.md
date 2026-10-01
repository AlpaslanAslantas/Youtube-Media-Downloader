# 🎵 YouTube Media Downloader / YouTube Medya İndirici

[English](#english) | [Türkçe](#türkçe)

---

<a name="english"></a>
## 🇬🇧 English

Modern and user-friendly desktop application built with Python & CustomTkinter to download YouTube videos in desired resolutions (144p - 8K) or audio formats (`mp3`, `wav`, `mp4`).

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-blueviolet?style=for-the-badge)
![yt-dlp](https://img.shields.io/badge/Core-yt--dlp-red?style=for-the-badge)
![AI Assisted](https://img.shields.io/badge/Developed%20With-AI%20Assisted-green?style=for-the-badge)

### ⚙️ How It Works

1. **URL Scan:** Extracts metadata and analyzes available resolutions and estimated file sizes using `yt-dlp` without downloading the video.
2. **Multithreading:** Runs download and conversion processes in a background thread to keep the GUI responsive.
3. **Embedded FFmpeg:** Uses `imageio-ffmpeg` for automatic audio conversions (`mp3`, `wav`) without requiring external system setup.
4. **Progress Tracking & Cancel:** Tracks download speed, downloaded size, and percentage in real-time. Features a one-click cancel button to stop downloads and clean temporary files.

### 🌟 Features

- 🎨 **Modern Dark Theme:** Sleek UI powered by CustomTkinter.
- 🎬 **Multi-Format Support:** `mp3`, `wav` audio and 144p to 8K `mp4` video formats.
- 🔍 **Quality Scan:** Lists actual available resolutions before downloading.
- 📊 **Estimated File Size:** Shows approximate file sizes for selected quality.
- ⛔ **Download Cancel:** Halts downloads instantly and clears temporary files.
- 📂 **Folder Management:** Select destination folder and open it directly in file explorer.

### 🚀 Setup & Execution

#### Requirements
- Python 3.9+

```bash
# 1. Clone repo
git clone [https://github.com/KULLANICI_ADIN/youtube-media-downloader.git](https://github.com/KULLANICI_ADIN/youtube-media-downloader.git)
cd youtube-media-downloader

# 2. Install dependencies
pip install customtkinter yt-dlp imageio-ffmpeg pyinstaller

# 3. Run application
python app.py

This application is developed strictly for educational, personal use, and downloading royalty-free/open-licensed content. Users are solely responsible for complying with YouTube Terms of Service and copyright laws.
