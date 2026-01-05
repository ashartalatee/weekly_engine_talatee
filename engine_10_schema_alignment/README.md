# Engine 10 — Schema Detection & Alignment

Engine ini bertugas menyatukan perbedaan schema data
dari banyak sumber menjadi satu schema target yang konsisten.

Masalah yang diselesaikan:
- Nama kolom berbeda
- Urutan kolom berbeda
- Kolom hilang / ekstra
- Data tidak bisa digabung

Engine ini adalah fondasi scaling data cleaning & reporting.

## Cara Menjalankan

```bash
python src/runner.py
