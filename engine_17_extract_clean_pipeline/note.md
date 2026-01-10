# Day 01 — Boundary & Scope Engine 17

## Kenapa engine ini perlu ada
Klien sering mengira masalah ada di laporan,
padahal rusaknya terjadi jauh sebelumnya di extraction atau cleaning.

Engine ini dibuat sebagai jembatan yang hilang itu.

## Apa yang engine ini kerjakan
- Menjalankan extraction via wrapper
- Mengirim hasil ke cleaning
- Menghentikan pipeline jika kualitas gagal
- Menghasilkan laporan kualitas

## Apa yang engine ini TIDAK kerjakan
- Tidak scraping spesifik website
- Tidak cleaning kompleks per kolom
- Tidak optimasi performa besar

## Insight hari ini
Masalah terbesar data bukan teknis,
tapi tidak adanya satu alur yang bisa dijelaskan ke klien.

Engine ini adalah alat komunikasi, bukan sekadar kode.
