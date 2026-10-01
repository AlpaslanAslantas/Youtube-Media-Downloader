import os
import sys
import threading
import subprocess
import customtkinter as ctk
from tkinter import filedialog
import yt_dlp
import imageio_ffmpeg

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class YouTubeDownloaderApp(ctk.CTk):

  def __init__(self):
    super().__init__()

    self.title("YouTube Medya İndirici")
    self.geometry("580x660")
    self.resizable(False, False)

    self.cancel_requested = False
    self.video_info = None

    self.download_folder = os.path.join(
        os.path.expanduser("~"), "Downloads"
    )

    self.default_resolutions = [
        "En Yüksek Kalite",
        "8K (4320p)",
        "4K (2160p)",
        "2K (1440p)",
        "1080p",
        "720p",
        "480p",
        "360p",
        "240p",
        "144p",
    ]

    self.label_title = ctk.CTkLabel(
        self,
        text="YouTube Ses & Video İndirici",
        font=ctk.CTkFont(size=22, weight="bold"),
    )
    self.label_title.pack(pady=(20, 10))

    self.frame_url = ctk.CTkFrame(self, fg_color="transparent")
    self.frame_url.pack(pady=10, fill="x", padx=30)

    self.entry_url = ctk.CTkEntry(
        self.frame_url,
        placeholder_text="YouTube video linkini yapıştırın...",
        width=380,
        height=38,
    )
    self.entry_url.pack(side="left", padx=(0, 8))

    self.btn_scan = ctk.CTkButton(
        self.frame_url,
        text="Kaliteleri Tara",
        command=self.start_scan_thread,
        width=110,
        height=38,
        fg_color="#3B82F6",
        hover_color="#2563EB",
    )
    self.btn_scan.pack(side="left")

    self.label_format = ctk.CTkLabel(
        self,
        text="Format Seçin:",
        font=ctk.CTkFont(size=13, weight="bold"),
    )
    self.label_format.pack(pady=(5, 2))

    self.combo_format = ctk.CTkComboBox(
        self,
        values=["mp3", "wav", "mp4"],
        width=200,
        height=32,
        command=self.on_format_change,
    )
    self.combo_format.set("mp3")
    self.combo_format.pack(pady=5)

    self.frame_resolution = ctk.CTkFrame(self, fg_color="transparent")

    self.label_res = ctk.CTkLabel(
        self.frame_resolution,
        text="Video Kalitesi:",
        font=ctk.CTkFont(size=13, weight="bold"),
    )
    self.label_res.pack(pady=(5, 2))

    self.combo_res = ctk.CTkComboBox(
        self.frame_resolution,
        values=self.default_resolutions,
        width=200,
        height=32,
        command=self.update_estimated_size,
    )
    self.combo_res.set("En Yüksek Kalite")
    self.combo_res.pack(pady=5)

    self.label_size = ctk.CTkLabel(
        self,
        text="Tahmini Boyut: -",
        font=ctk.CTkFont(size=12, weight="bold"),
        text_color="#9CA3AF",
    )
    self.label_size.pack(pady=3)

    self.frame_folder = ctk.CTkFrame(self, fg_color="transparent")
    self.frame_folder.pack(pady=10, fill="x", padx=30)

    self.btn_select_folder = ctk.CTkButton(
        self.frame_folder,
        text="Klasör Seç",
        command=self.select_folder,
        width=100,
        height=32,
    )
    self.btn_select_folder.pack(side="left", padx=(0, 10))

    self.label_folder_path = ctk.CTkLabel(
        self.frame_folder,
        text=self.download_folder,
        font=ctk.CTkFont(size=11),
        text_color="gray",
        anchor="w",
    )
    self.label_folder_path.pack(side="left", fill="x", expand=True)

    self.btn_download = ctk.CTkButton(
        self,
        text="İndirmeyi Başlat",
        command=self.handle_download_button,
        height=42,
        width=220,
        font=ctk.CTkFont(size=14, weight="bold"),
        fg_color="#10B981",
        hover_color="#059669",
    )
    self.btn_download.pack(pady=12)

    self.btn_open_folder = ctk.CTkButton(
        self,
        text="Klasörü Aç",
        command=self.open_download_folder,
        height=36,
        width=160,
        font=ctk.CTkFont(size=12, weight="bold"),
        fg_color="#4B5563",
        hover_color="#374151",
    )
    self.btn_open_folder.pack(pady=(0, 10))

    self.label_status = ctk.CTkLabel(
        self,
        text="Hazır",
        font=ctk.CTkFont(size=12),
        text_color="gray",
        wraplength=520,
    )
    self.label_status.pack(pady=5)

  def open_download_folder(self):
    folder_path = os.path.abspath(self.download_folder)
    if os.path.exists(folder_path):
      if sys.platform == "win32":
        os.startfile(folder_path)
      elif sys.platform == "darwin":
        subprocess.run(["open", folder_path])
      else:
        subprocess.run(["xdg-open", folder_path])
    else:
      self.label_status.configure(
          text="Seçili klasör bulunamadı!", text_color="#EF4444"
      )

  def on_format_change(self, choice):
    if choice == "mp4":
      self.frame_resolution.pack(after=self.combo_format, pady=5)
    else:
      self.frame_resolution.pack_forget()
    self.update_estimated_size()

  def select_folder(self):
    folder_selected = filedialog.askdirectory(
        title="İndirilecek Klasörü Seçin", initialdir=self.download_folder
    )
    if folder_selected:
      self.download_folder = folder_selected
      self.label_folder_path.configure(text=self.download_folder)

  def handle_download_button(self):
    if self.cancel_requested is False and self.btn_download.cget("text") == "İndirmeyi Durdur":
      self.cancel_requested = True
      self.label_status.configure(
          text="İndirme iptal ediliyor...", text_color="#EF4444"
      )
    else:
      self.start_download_thread()

  def start_scan_thread(self):
    threading.Thread(target=self.scan_qualities, daemon=True).start()

  def scan_qualities(self):
    url = self.entry_url.get().strip()
    if not url:
      self.label_status.configure(
          text="Lütfen önce geçerli bir URL girin!", text_color="#EF4444"
      )
      return

    self.btn_scan.configure(state="disabled")
    self.label_status.configure(
        text="Video kaliteleri taranıyor...", text_color="#3B82F6"
    )

    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "nocheckcertificate": True,
    }

    try:
      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        self.video_info = ydl.extract_info(url, download=False)
        formats = self.video_info.get("formats", [])

        heights = set()
        for f in formats:
          h = f.get("height")
          if h and f.get("vcodec") != "none":
            heights.add(h)

        available_res = ["En Yüksek Kalite"]
        check_list = [
            (4320, "8K (4320p)"),
            (2160, "4K (2160p)"),
            (1440, "2K (1440p)"),
            (1080, "1080p"),
            (720, "720p"),
            (480, "480p"),
            (360, "360p"),
            (240, "240p"),
            (144, "144p"),
        ]

        for target_h, label in check_list:
          if any(h >= target_h for h in heights):
            available_res.append(label)

        if len(available_res) == 1:
          available_res = self.default_resolutions

        self.combo_res.configure(values=available_res)
        self.combo_res.set(available_res[0])

        self.combo_format.set("mp4")
        self.on_format_change("mp4")

        self.label_status.configure(
            text=f"Mevcut Kaliteler Taranıp Listelendi! ({self.video_info.get('title', '')[:35]}...)",
            text_color="#10B981",
        )
        self.update_estimated_size()
    except Exception as e:
      self.label_status.configure(
          text=f"Tarama hatası: {str(e)[:50]}...", text_color="#EF4444"
      )
    finally:
      self.btn_scan.configure(state="normal")

  def get_format_size(self, f, duration):
    if not f:
      return 0
    size = f.get("filesize") or f.get("filesize_approx")
    if size:
      return size

    tbr = f.get("tbr")
    if tbr and duration:
      return tbr * duration * 125
    return 0

  def update_estimated_size(self, choice=None):
    if not self.video_info:
      self.label_size.configure(text="Tahmini Boyut: -")
      return

    fmt_type = self.combo_format.get()
    res_choice = self.combo_res.get()
    formats = self.video_info.get("formats", [])
    duration = self.video_info.get("duration") or 0

    if fmt_type in ["mp3", "wav"]:
      audio_formats = [f for f in formats if f.get("vcodec") == "none"]
      if audio_formats:
        best_audio = max(
            audio_formats, key=lambda x: self.get_format_size(x, duration)
        )
        size_bytes = self.get_format_size(best_audio, duration)
        if size_bytes > 0:
          mb_size = size_bytes / (1024 * 1024)
          self.label_size.configure(
              text=f"Tahmini Boyut: ~{mb_size:.2f} MB", text_color="#3B82F6"
          )
          return
      self.label_size.configure(text="Tahmini Boyut: Belli değil")
    else:
      audio_bytes = 0
      audio_formats = [f for f in formats if f.get("vcodec") == "none"]
      if audio_formats:
        best_audio = max(
            audio_formats, key=lambda x: self.get_format_size(x, duration)
        )
        audio_bytes = self.get_format_size(best_audio, duration)

      target_h = self.parse_resolution_height(res_choice)

      matching_videos = []
      for f in formats:
        if f.get("vcodec") != "none" and f.get("height"):
          if target_h is None or f.get("height") <= target_h:
            matching_videos.append(f)

      if matching_videos:
        selected_vid = max(matching_videos, key=lambda x: x.get("height", 0))
        vid_bytes = self.get_format_size(selected_vid, duration)

        total_bytes = vid_bytes + audio_bytes
        if total_bytes > 0:
          mb_size = total_bytes / (1024 * 1024)
          self.label_size.configure(
              text=f"Tahmini Boyut: ~{mb_size:.2f} MB", text_color="#3B82F6"
          )
          return

      self.label_size.configure(text="Tahmini Boyut: Belli değil")

  def parse_resolution_height(self, res_str):
    if "8K" in res_str:
      return 4320
    elif "4K" in res_str:
      return 2160
    elif "2K" in res_str:
      return 1440
    elif "1080p" in res_str:
      return 1080
    elif "720p" in res_str:
      return 720
    elif "480p" in res_str:
      return 480
    elif "360p" in res_str:
      return 360
    elif "240p" in res_str:
      return 240
    elif "144p" in res_str:
      return 144
    return None

  def start_download_thread(self):
    self.cancel_requested = False
    threading.Thread(target=self.download_media, daemon=True).start()

  def progress_hook(self, d):
    if self.cancel_requested:
      raise Exception("İndirme kullanıcı tarafından iptal edildi.")

    if d["status"] == "downloading":
      percent = d.get("_percent_str", "").strip()
      speed = d.get("_speed_str", "").strip()

      downloaded_bytes = d.get("downloaded_bytes", 0)
      total_bytes = d.get("total_bytes") or d.get("total_bytes_estimate", 0)

      if total_bytes > 0:
        d_mb = downloaded_bytes / (1024 * 1024)
        t_mb = total_bytes / (1024 * 1024)
        size_str = f"({d_mb:.1f} MB / {t_mb:.1f} MB)"
      else:
        size_str = ""

      self.label_status.configure(
          text=f"İndiriliyor: {percent} {size_str} - {speed}",
          text_color="#3B82F6",
      )
    elif d["status"] == "finished":
      self.label_status.configure(
          text="Dönüştürülüyor / İşleniyor...", text_color="#EAB308"
      )

  def download_media(self):
    url = self.entry_url.get().strip()
    selected_format = self.combo_format.get()
    selected_res = self.combo_res.get()

    if not url:
      self.label_status.configure(
          text="Lütfen geçerli bir YouTube URL'si girin!", text_color="#EF4444"
      )
      return

    self.btn_download.configure(
        text="İndirmeyi Durdur", fg_color="#EF4444", hover_color="#DC2626"
    )
    self.label_status.configure(
        text="Bağlantı kuruluyor...", text_color="#3B82F6"
    )

    try:
      ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
      ffmpeg_exe = None

    if selected_format in ["mp3", "wav"]:
      file_label = selected_format
    else:
      if "En Yüksek" in selected_res:
        file_label = "Max"
      else:
        file_label = selected_res.split(" ")[0]

    ydl_opts = {
        "outtmpl": f"{self.download_folder}/%(title)s [{file_label}].%(ext)s",
        "progress_hooks": [self.progress_hook],
        "nocheckcertificate": True,
    }

    if ffmpeg_exe:
      ydl_opts["ffmpeg_location"] = ffmpeg_exe

    if selected_format in ["mp3", "wav"]:
      ydl_opts.update({
          "format": "bestaudio/best",
          "postprocessors": [{
              "key": "FFmpegExtractAudio",
              "preferredcodec": selected_format,
              "preferredquality": "192",
          }],
      })
    else:
      target_h = self.parse_resolution_height(selected_res)

      if target_h:
        res_format = (
            f"bestvideo[height<={target_h}][ext=mp4]+bestaudio[ext=m4a]/"
            f"bestvideo[height<={target_h}]+bestaudio/best"
        )
      else:
        res_format = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"

      ydl_opts.update({"format": res_format})

    try:
      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

      self.label_status.configure(
          text=f"Başarıyla İndirildi!\nKaydedilen Yer: {self.download_folder}",
          text_color="#10B981",
      )
    except Exception as e:
      if "iptal edildi" in str(e):
        self.label_status.configure(
            text="İndirme işlemi durduruldu.", text_color="#EF4444"
        )
      else:
        self.label_status.configure(
            text=f"Hata: {str(e)}", text_color="#EF4444"
        )
    finally:
      self.btn_download.configure(
          text="İndirmeyi Başlat", fg_color="#10B981", hover_color="#059669"
      )
      self.cancel_requested = False


if __name__ == "__main__":
  app = YouTubeDownloaderApp()
  app.mainloop()