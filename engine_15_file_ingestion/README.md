# Engine 15 — File Ingestion Engine

## Masalah Dunia Nyata
Klien mengirim data dari berbagai sumber:
- folder lokal
- upload manual
- SFTP
dengan format, struktur, dan kualitas yang tidak konsisten.

Masalah utama bukan "membaca file",
tetapi **menjaga sistem tetap hidup walau data bermasalah**.

## Solusi
Engine ini menangani proses ingestion data secara:
- aman
- terlog
- tidak mematikan pipeline

## Apa yang Engine Ini Lakukan
- Menemukan file dari berbagai sumber
- Mendeteksi format & kelayakan file
- Memuat data dengan fail-safe
- Mencatat error tanpa menghentikan proses

## Apa yang Engine Ini TIDAK Lakukan
- Tidak membersihkan data
- Tidak memvalidasi isi bisnis
- Tidak melakukan transformasi kompleks

## Posisi Engine Ini di Pipeline
File Ingestion → Cleaning → Validation → Reporting

## Cara menjalankan
python -m src.runner
