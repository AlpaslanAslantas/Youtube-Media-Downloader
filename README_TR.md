# 🎵 YouTube Medya İndirici (Python & CustomTkinter)

Bu uygulama; YouTube videolarını istenilen çözünürlükte (144p - 8K) veya sadece ses formatında (`mp3`, `wav`, `mp4`) bilgisayarınıza indirmenizi sağlayan modern ve kullanıcı dostu bir masaüstü yazılımıdır.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-blueviolet?style=for-the-badge)
![yt-dlp](https://img.shields.io/badge/Core-yt--dlp-red?style=for-the-badge)
![AI Assisted](https://img.shields.io/badge/Developed%20With-AI%20Assisted-green?style=for-the-badge)

---

## ⚙️ Uygulama Nasıl Çalışır?

Uygulama arka planda modüler bir mimari ve iş parçacığı (multithreading) yapısı kullanarak çalışır:

1. **Bağlantı ve Tarama:** Kullanıcı bir YouTube URL'si girdiğinde `Kaliteleri Tara` butonu çalıştırılır. `yt-dlp` altyapısı kullanılarak videonun meta verileri indirilmeksizin analiz edilir; desteklenen çözünürlükler ve tahmini dosya boyutları dinamik olarak arayüze aktarılır.
2. **Arka Plan İş Parçacıkları (Threading):** İndirme ve dönüştürme işlemleri grafik arayüzünün (GUI) donmaması veya kilitlenmemesi için arka planda ayrı bir iş parçacığında yürütülür.
3. **Otomatik FFmpeg Dönüştürme:** `imageio-ffmpeg` entegrasyonu sayesinde sistemde harici bir FFmpeg kurulumuna ihtiyaç duyulmadan ses dönüştürmeleri (`mp3`, `wav`) otomatik olarak gerçekleştirilir.
4. **İlerleme Takibi ve İptal Mekanizması:** İndirme esnasında canlı yayın akışı `progress_hook` fonksiyonu ile izlenir; anlık hız, indirilen MB miktarı ve yüzde arayüzde güncellenir. İstenildiği takdirde indirme işlemi tek tıkla iptal edilerek geçici dosyalar temizlenir.

---

## 🤖 Yapay Zekâ Destekli Geliştirme Süreci (AI-Assisted Development)

Bu proje, güncel yazılım geliştirme pratikleri doğrultusunda **Yapay Zekâ (AI)** desteğiyle geliştirilmiştir:

- **Mimari ve İhtiyaç Analizi:** Uygulamanın sahip olması gereken kullanıcı deneyimi (UX) adımları (çözünürlük tarama, canlı iptal mekanizması, dinamik dosya adı etiketleme vb.) geliştirici tarafından kurgulanmıştır.
- **Kod Üretimi ve Hata Ayıklama (Debugging):** Python kod taslaklarının oluşturulması, `yt-dlp` kütüphanesinin güncel API entegrasyonu, FFmpeg çakışmalarının giderilmesi ve PyInstaller ile derleme süreçlerinde LLM (Yapay Zekâ) araçlarından faydalanılmıştır.
- **Sonuç:** Yapay zekanın hız ve verimlilik gücü ile geliştiricinin yönlendirme, test ve problem çözme becerilerinin birleşimi sonucunda eksiksiz bir ürün ortaya konmuştur.

---

## 🌟 Öne Çıkan Özellikler

- 🎨 **Modern Koyu Tema Arayüz:** CustomTkinter ile estetik ve kullanıcı dostu tasarım.
- 🎬 **Geniş Format ve Kalite Desteği:** `mp3`, `wav` ses ve 144p'den 8K'ya kadar `mp4` video formatları.
- 🔍 **Akıllı Kalite Taraması:** Videodaki mevcut gerçek çözünürlükleri indirme öncesi listeleme.
- 📊 **Tahmini Boyut Hesaplama:** Seçilen kaliteye göre yaklaşık dosya boyutunu önceden görüntüleme.
- ⛔ **İndirme Durdurma (İptal Etme):** İndirmeyi yarıda kesebilme ve diskteki geçici artıkları temizleme.
- 📂 **Klasör Yönetimi ve Hızlı Erişim:** İndirme klasörünü seçebilme ve doğrudan dosya gezgininde açma.
- 📦 **Tek Tıkla Çıktı:** Otomatik FFmpeg entegrasyonu ile harici bağımlılıksız çalışma.

---

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler
- Python 3.9 veya üzeri

### 1. Depoyu klonlayın
```bash
git clone [https://github.com/AlpaslanAslantas/youtube-media-downloader.git](https://github.com/AlpaslanAslantas/youtube-media-downloader.git)
cd youtube-media-downloader

Bu uygulama yalnızca eğitim, kişisel kullanım ve telifsiz/açık lisanslı içeriklerin indirilmesi amacıyla geliştirilmiştir. Kullanıcılar, YouTube Hizmet Şartlarına (Terms of Service) ve ilgili telif hakkı yasalarına uymakla kendileri sorumludur. Yazılımın üçüncü şahıslar tarafından telif hakkı ihlali oluşturacak şekilde kullanımından geliştirici sorumlu tutulamaz.
