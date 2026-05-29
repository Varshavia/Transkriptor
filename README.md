# 🎙️ Transkriptor

Ses dosyalarını metne dönüştüren yerel web uygulaması. OpenAI Whisper kullanır — tamamen ücretsiz, internet gerektirmez.

## 🚀 Başlatma

**`baslat.bat`** dosyasına çift tıklayın. İlk açılışta gerekli kütüphaneleri otomatik yükler.

Uygulama açıldığında tarayıcınızda **http://localhost:5000** adresi açılır.

## 🎵 Desteklenen Formatlar

MP3, WAV, M4A, OGG, FLAC, MP4, WebM

## 🤖 Model Seçimi

| Model  | Hız     | Kalite   | Bellek |
|--------|---------|----------|--------|
| Tiny   | ⚡⚡⚡⚡ | ★★       | ~1 GB  |
| Base   | ⚡⚡⚡   | ★★★      | ~1 GB  |
| Small  | ⚡⚡     | ★★★★     | ~2 GB  |
| Medium | ⚡       | ★★★★★    | ~5 GB  |
| Large  | 🐢       | ★★★★★+   | ~10 GB |

> İlk kullanımda seçilen model indirilir (~100 MB – 3 GB arası).

## 📤 Çıktı Formatları

- **Tam metin** — kopyalanabilir, TXT olarak indirilebilir
- **SRT altyazı dosyası** — zaman damgalı, video düzenleyicilere uygun

## ⚙️ Manuel Kurulum

```
pip install flask openai-whisper werkzeug
python app.py
```
