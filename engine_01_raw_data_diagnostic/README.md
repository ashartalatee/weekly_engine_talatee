# Engine 01 — Raw Data Diagnostic Engine

## Masalah Dunia Nyata
Sebagian besar klien tidak tahu:
- di mana data mereka rusak
- seberapa parah kerusakannya
- apakah data masih layak dipakai

Akibatnya:
- cleaning dilakukan asal
- laporan jadi menyesatkan
- keputusan bisnis salah arah

## Tujuan Engine Ini
Engine ini bertugas untuk:
- memindai kondisi awal data
- mendeteksi pola kerusakan
- menghasilkan laporan faktual sebelum cleaning

Engine ini **TIDAK memperbaiki data**.  
Engine ini **membaca kondisi data**.

## Jenis Diagnostik
Engine ini memeriksa:
- Missing & null value
- Duplicate & near-duplicate
- Format anomaly (tanggal, angka, teks)
- Schema inconsistency (kolom & struktur)

## Output
- File laporan JSON
- Insight awal yang bisa dijelaskan ke klien non-teknis

## Posisi Engine Ini
Engine ini adalah:
- langkah pertama sebelum cleaning
- fondasi semua engine berikutnya
- alat komunikasi antara data & bisnis
