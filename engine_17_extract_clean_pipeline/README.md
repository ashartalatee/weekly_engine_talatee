# Engine 17 — Extract → Clean Pipeline

## Masalah Dunia Nyata
Di dunia nyata, data tidak pernah datang dalam kondisi siap pakai.
Extraction dan cleaning sering terpisah, menyebabkan:
- alur terputus
- data rusak lolos ke laporan
- debugging mahal

## Solusi
Engine ini menyatukan proses:
Extract → Clean → Validate → Output
dalam satu pipeline berbasis konfigurasi.

## Prinsip Utama
- Config-driven, bukan hardcode
- Setiap tahap bisa diganti tanpa ubah kode
- Ada jejak audit & laporan kualitas

## Contoh Kasus
(Data dummy akan ditambahkan)

## Status
🚧 Dalam pengembangan (Talatee Engine Roadmap)
