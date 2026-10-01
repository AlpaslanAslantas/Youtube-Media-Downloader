<p align="center">
  <a href="#english">
    <img src="https://img.shields.io/badge/🇬🇧_ENGLISH-24292f?style=for-the-badge" alt="English">
  </a>
  <a href="#turkce">
    <img src="https://img.shields.io/badge/🇹🇷_TÜRKÇE-24292f?style=for-the-badge" alt="Turkish">
  </a>
</p>

<a id="english"></a>

# 🎵 YouTube Media Downloader

A modern and user-friendly desktop application that allows you to download YouTube videos in the desired resolution (144p - 8K) or extract audio in formats such as `mp3`, `wav`, and `mp4`.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-blueviolet?style=for-the-badge)
![yt-dlp](https://img.shields.io/badge/Core-yt--dlp-red?style=for-the-badge)
![AI Assisted](https://img.shields.io/badge/Developed%20With-AI%20Assisted-green?style=for-the-badge)

---

## ⚙️ How Does It Work?

The application uses a modular architecture and multithreading to keep the interface responsive during scanning, downloading, and conversion processes.

### 1. 🔗 URL & Quality Scanning

When the user enters a YouTube URL and clicks **Scan Qualities**, the application uses the `yt-dlp` backend to analyze the available media formats.

Available resolutions and estimated file sizes are dynamically displayed in the interface before downloading.

### 2. 🧵 Background Threading

Download and conversion operations are executed in background threads so that the graphical user interface (GUI) does not freeze or become unresponsive.

### 3. 🔄 Automatic FFmpeg Conversion

The application integrates `imageio-ffmpeg`, allowing audio conversion to formats such as `mp3` and `wav` without requiring the user to manually install FFmpeg.

### 4. 📊 Progress Tracking & Cancellation

The download process is monitored through the `progress_hook` mechanism.

The interface displays:

- Download percentage
- Current download speed
- Downloaded amount in MB
- Current status

Users can cancel an active download with a single click. Temporary files are also cleaned up when possible.

---

## 🤖 AI-Assisted Development

This project was developed using an **AI-assisted software development workflow**.

### Architecture & Requirements

The overall application concept and user experience were designed by the developer, including:

- Quality scanning
- Dynamic file naming
- Live download progress
- Download cancellation
- Output format selection
- Download folder management

### Code Generation & Debugging

AI/LLM tools were used during development for:

- Generating Python code drafts
- Integrating the `yt-dlp` API
- Debugging application issues
- Resolving FFmpeg-related problems
- Improving the GUI
- Assisting with PyInstaller packaging

### Development Approach

AI was used as a development assistant rather than as a replacement for the developer's decisions.

The final application was created through a combination of developer planning, AI-assisted coding, testing, debugging, and iteration.

---

## 🌟 Features

- 🎨 **Modern Dark Theme:** Built with CustomTkinter for a clean and user-friendly interface.
- 🎬 **Multiple Formats & Resolutions:** Supports `mp3`, `wav`, and `mp4`, with video resolutions ranging from 144p up to 8K when available.
- 🔍 **Smart Quality Scanning:** Displays the actual media formats and resolutions available for the selected video.
- 📊 **Estimated File Size:** Shows an approximate file size before downloading.
- ⛔ **Download Cancellation:** Allows users to stop an active download and clean up temporary files.
- 📂 **Download Folder Management:** Choose the download directory and quickly open it in File Explorer.
- 📦 **Automatic FFmpeg Integration:** Uses `imageio-ffmpeg` to handle audio conversion without requiring a separate FFmpeg installation.

---

## 🚀 Installation & Usage

### Requirements

- Python 3.9 or newer

### 1. Clone the Repository

```bash
git clone https://github.com/AlpaslanAslantas/youtube-media-downloader.git
cd youtube-media-downloader
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python main.py
```

---

## ⚠️ Disclaimer

This application is intended for **educational purposes, personal use, and downloading content that is legally permitted to be downloaded**, such as public-domain or appropriately licensed content.

Users are responsible for complying with the **YouTube Terms of Service**, copyright laws, and other applicable regulations.

The developer does not encourage or endorse copyright infringement or unauthorized downloading of copyrighted material.

---

<a id="Turkish"></a>

# 🎵 YouTube Medya İndirici

YouTube videolarını istenilen çözünürlükte (144p - 8K) veya yalnızca ses olarak `mp3`, `wav` ve `mp4` formatlarında indirmenizi sağlayan modern ve kullanıcı dostu bir masaüstü uygulamasıdır.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-blueviolet?style=for-the-badge)
![yt-dlp](https://img.shields.io/badge/Core-yt--dlp-red?style=for-the-badge)
![AI Assisted](https://img.shields.io/badge/Developed%20With-AI%20Assisted-green?style=for-the-badge)

---

## ⚙️ Uygulama Nasıl Çalışır?

Uygulama; tarama, indirme ve dönüştürme işlemleri sırasında arayüzün donmasını önlemek amacıyla modüler bir mimari ve **multithreading (iş parçacığı)** yapısı kullanır.

### 1. 🔗 URL ve Kalite Taraması

Kullanıcı bir YouTube URL'si girdiğinde ve **Kaliteleri Tara** butonuna bastığında uygulama, `yt-dlp` altyapısını kullanarak mevcut medya formatlarını analiz eder.

Videoda bulunan çözünürlükler ve tahmini dosya boyutları indirme işleminden önce dinamik olarak arayüzde gösterilir.

### 2. 🧵 Arka Plan İş Parçacıkları

İndirme ve dönüştürme işlemleri ayrı arka plan iş parçacıklarında yürütülür.

Bu sayede grafik kullanıcı arayüzü (GUI) donmaz ve kullanıcı uygulamayla etkileşime devam edebilir.

### 3. 🔄 Otomatik FFmpeg Dönüştürme

Uygulama `imageio-ffmpeg` entegrasyonunu kullanır.

Bu sayede `mp3` ve `wav` gibi ses formatlarına dönüştürme işlemleri için kullanıcının ayrıca sistemine FFmpeg kurması gerekmez.

### 4. 📊 İlerleme Takibi ve İptal

İndirme işlemi `progress_hook` mekanizması üzerinden takip edilir.

Arayüz üzerinde:

- İndirme yüzdesi
- Anlık indirme hızı
- İndirilen MB miktarı
- İşlem durumu

gibi bilgiler gösterilir.

Kullanıcı aktif bir indirmeyi tek tıklamayla iptal edebilir. Geçici dosyalar da mümkün olduğunca temizlenir.

---

## 🤖 Yapay Zekâ Destekli Geliştirme

Bu proje **AI-assisted development (Yapay zekâ destekli geliştirme)** yaklaşımı kullanılarak geliştirilmiştir.

### Mimari ve İhtiyaç Analizi

Uygulamanın genel konsepti ve kullanıcı deneyimi geliştirici tarafından tasarlanmıştır.

Bunlar arasında:

- Kalite tarama sistemi
- Dinamik dosya adlandırma
- Canlı indirme ilerlemesi
- İndirme iptali
- Çıktı formatı seçimi
- İndirme klasörü yönetimi

bulunmaktadır.

### Kod Üretimi ve Hata Ayıklama

Geliştirme sürecinde AI/LLM araçlarından aşağıdaki konularda yararlanılmıştır:

- Python kod taslaklarının oluşturulması
- `yt-dlp` API entegrasyonu
- Hataların tespit edilmesi ve giderilmesi
- FFmpeg kaynaklı problemlerin çözülmesi
- GUI geliştirmeleri
- PyInstaller ile paketleme sürecine destek

### Geliştirme Yaklaşımı

Yapay zekâ, geliştiricinin yerine geçen bir sistem olarak değil, **geliştirme asistanı** olarak kullanılmıştır.

Ortaya çıkan uygulama; geliştirici tarafından yapılan planlama, AI destekli kodlama, test, hata ayıklama ve yinelemeli geliştirme süreçlerinin birleşimiyle oluşturulmuştur.

---

## 🌟 Öne Çıkan Özellikler

- 🎨 **Modern Koyu Tema:** CustomTkinter kullanılarak hazırlanmış temiz ve kullanıcı dostu arayüz.
- 🎬 **Geniş Format ve Çözünürlük Desteği:** `mp3`, `wav` ve `mp4` desteği. Video için mevcut olduğu durumlarda 144p'den 8K'ya kadar çözünürlük seçenekleri.
- 🔍 **Akıllı Kalite Taraması:** Seçilen videoda gerçekten mevcut olan medya formatlarını ve çözünürlükleri gösterir.
- 📊 **Tahmini Dosya Boyutu:** İndirme işleminden önce yaklaşık dosya boyutunu gösterir.
- ⛔ **İndirme İptali:** Aktif indirmeyi durdurma ve geçici dosyaları temizleme imkânı sağlar.
- 📂 **İndirme Klasörü Yönetimi:** İndirme klasörünü seçebilir ve klasörü doğrudan Dosya Gezgini'nde açabilirsiniz.
- 📦 **Otomatik FFmpeg Entegrasyonu:** Ayrı bir FFmpeg kurulumu gerektirmeden ses dönüştürme işlemlerini gerçekleştirmek için `imageio-ffmpeg` kullanır.

---

## 🚀 Kurulum ve Kullanım

### Gereksinimler

- Python 3.9 veya üzeri

### 1. Depoyu Klonlayın

```bash
git clone https://github.com/AlpaslanAslantas/youtube-media-downloader.git
cd youtube-media-downloader
```

### 2. Bağımlılıkları Kurun

```bash
pip install -r requirements.txt
```

### 3. Uygulamayı Çalıştırın

```bash
python main.py
```

---

## ⚠️ Yasal Uyarı

Bu uygulama **eğitim, kişisel kullanım ve yasal olarak indirilmesine izin verilen içeriklerin**, örneğin kamu malı veya uygun lisansa sahip içeriklerin indirilmesi amacıyla geliştirilmiştir.

Kullanıcılar **YouTube Hizmet Şartlarına**, telif hakkı yasalarına ve geçerli diğer yasal düzenlemelere uymaktan kendileri sorumludur.

Geliştirici, telif hakkı ihlalini veya telif hakkıyla korunan içeriklerin izinsiz indirilmesini teşvik etmez veya desteklemez.

---

**Developed with Python, CustomTkinter & yt-dlp.**
