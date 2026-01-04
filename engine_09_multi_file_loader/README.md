# Engine 09 — Multi-File Loader Engine

## Masalah Dunia Nyata
Klien jarang mengirim satu file rapi.
Yang datang biasanya:
- puluhan file
- format campur (CSV, Excel, JSON)
- struktur kolom berbeda
- sebagian rusak

Tanpa sistem loader yang benar, proses data akan:
- sering gagal
- sulit diaudit
- tidak bisa diskalakan

## Solusi Engine Ini
Engine ini bertugas untuk:
- menemukan semua file data dalam folder & subfolder
- memuat data dari berbagai format
- menangani file rusak tanpa menghentikan proses
- mencatat struktur (schema) setiap file
- menghasilkan laporan kondisi data awal

## Output Utama
- `loader_report.json`
  - total file
  - file berhasil dimuat
  - file gagal
  - snapshot schema
  - daftar error

## Kenapa Engine Ini Penting
Tanpa engine ini:
- batch cleaning tidak mungkin stabil
- schema alignment mustahil
- engineer akan terus panik di awal project

Engine ini adalah **gerbang masuk dunia data nyata**.
