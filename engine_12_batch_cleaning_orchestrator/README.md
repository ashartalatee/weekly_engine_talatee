# Engine 12 — Batch Cleaning Orchestrator

## Masalah Dunia Nyata
Klien jarang mengirim satu file data.
Biasanya mereka mengirim:
- puluhan file
- format tidak konsisten
- revisi berkali-kali
- sebagian file rusak

Jika satu file gagal dan seluruh proses berhenti,
biaya, waktu, dan kepercayaan klien langsung rusak.

## Tujuan Engine Ini
Engine ini bertugas:
- menjalankan proses cleaning dalam jumlah besar
- memastikan kegagalan satu file tidak menghentikan batch
- memberikan ringkasan hasil yang bisa dipahami klien

## Yang Engine Ini BUKAN
- Bukan script for-loop
- Bukan fokus ke logic cleaning
- Bukan alat eksplorasi data

## Nilai Bisnis
Dengan engine ini:
- proses massal bisa diprediksi
- error bisa dikontrol
- harga jasa bisa dinaikkan karena stabilitas sistem

# Engine 12 — Batch Cleaning Orchestrator

## Deskripsi
Batch Cleaning Orchestrator adalah engine untuk menjalankan **batch data cleaning** secara terstruktur dan aman.
Engine ini:
- Membaca batch jobs dari config
- Menjalankan job berurutan
- Retry otomatis & fail-safe jika job gagal
- Logging tiap job
- Membuat summary report untuk klien

## Masalah Dunia Nyata
- Klien sering kirim puluhan file CSV dengan format berbeda
- Satu file gagal bisa menghentikan proses
- Klien butuh ringkasan hasil, bukan log teknis

## Cara Pakai
1. Isi `config/batch_jobs.yaml` sesuai kebutuhan
2. Letakkan file input di `data/input/`
3. Jalankan orchestrator:
```bash
python src/orchestrator.py
