# Date & Time Harmonization Engine

Engine ini dirancang untuk menangani kekacauan tanggal & waktu
yang sering terjadi pada data dunia nyata:
- format campur aduk
- timezone tidak konsisten
- tanggal tidak masuk akal
- asumsi sistem yang diam-diam salah

## Masalah Dunia Nyata
Sebagian besar sistem menganggap tanggal hanyalah string.
Akibatnya:
- laporan meleset jam / hari
- agregasi waktu salah
- keputusan bisnis keliru

## Solusi Engine Ini
Engine ini bekerja dengan prinsip:
1. Deteksi format, bukan menebak
2. Parsing hanya setelah yakin
3. Semua waktu diberi konteks timezone
4. Output disatukan ke UTC
5. Tanggal tidak masuk akal ditandai, bukan dibuang
6. Semua keputusan dicatat dalam laporan

## Alur Kerja Engine
Raw Data → Detect → Parse → Normalize → Apply Timezone → Validate → Report

## Struktur Engine
- `config/` : aturan format & timezone
- `src/` : logika engine
- `data/` : contoh input & output
- `reports/` : laporan harmonisasi
- `tests/` : validasi dasar

## Contoh Output
- `cleaned_sample.csv`  
  Semua datetime konsisten & siap dipakai sistem lain
- `harmonization_report.json`  
  Penjelasan kenapa data diterima / ditolak

## Kapan Engine Ini Dipakai?
- Data cleaning project
- Data extraction pipeline
- Reporting & analytics
- Integrasi sistem lintas zona waktu

---

Engine ini adalah bagian dari **Talatee Data Engine**  
dibangun sebagai aset reusable, bukan script sekali pakai.
