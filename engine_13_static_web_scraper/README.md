# Static Web Scraper Engine

Engine ini bertujuan untuk mengambil data dari website statis
tanpa perlu copy–paste manual.

## Masalah Dunia Nyata
Banyak tim operasional dan bisnis masih mengambil data web
secara manual, rentan salah, dan tidak repeatable.

## Apa yang Engine Ini Lakukan
- Mengambil HTML dari website statis
- Mengekstrak data berbasis selector
- Menyimpan hasil ke CSV / JSON

## Batasan
- Tidak menangani JavaScript rendering
- Tidak menangani login atau captcha

## Status
 Dalam pengembangan (Day 1)

 # Static Web Scraper Engine

Engine ini adalah bagian dari **Talatee Data Engine Suite**  
Digunakan untuk mengekstrak data dari website statis secara repeatable,
terstruktur, dan siap dipakai bisnis.

---

## Masalah Dunia Nyata
Banyak tim:
- copy–paste data web manual
- rawan salah
- tidak bisa diulang
- tidak punya log jika gagal

Engine ini dibuat untuk **menghilangkan pekerjaan manual tersebut**.

---

## Solusi yang Ditawarkan
Engine ini mampu:
- Mengambil HTML dari website statis
- Mengekstrak data menggunakan CSS selector
- Mengatur target melalui file config (tanpa ubah kode)
- Menyimpan hasil ke CSV / JSON
- Menangani error dengan retry & logging

---

## Batasan
- Tidak menangani JavaScript rendering
- Tidak menangani login / captcha
- Fokus pada website statis (HTML)

---

## Struktur Singkat
```text
engine_13_static_web_scraper/
├── config/        # Konfigurasi scraping
├── src/           # Logic engine
├── data/          # Output
├── logs/          # Log error & proses
└── tests/         # Test inti

pip install -r requirements.txt
python src/runner.py
config/scraper_config.yaml
