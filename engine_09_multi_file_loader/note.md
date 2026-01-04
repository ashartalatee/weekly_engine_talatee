# NOTE — Engine 09 Multi-File Loader

## Hari 1 — Struktur & Niat Engine

Hari ini saya tidak menulis logika apa pun.
Fokus saya adalah memahami masalah dunia nyata:
klien tidak pernah mengirim satu file yang rapi.

Engine ini dibuat agar:
- saya tidak panik melihat banyak file
- proses tidak berhenti karena satu file rusak
- saya bisa menjelaskan kondisi data ke klien dengan fakta

Pelajaran hari ini:
Engineer yang baik berpikir tentang sistem
sebelum menulis kode.

## Hari 2 — File Discovery

Hari ini saya membangun radar data.
Engine ini belum membaca isi file,
tapi sudah tahu:
- ada berapa file
- format apa saja
- ukuran masing-masing

Insight penting:
Masalah data sering muncul
bahkan sebelum file dibuka.

Engineer bekerja dari luar ke dalam,
bukan langsung ke isi tabel.

## Hari 3 — File Loader

Hari ini saya belajar satu hal penting:
file rusak bukan musuh,
tapi fakta dunia nyata.

Engine ini tidak berhenti
hanya karena satu file gagal dibaca.

Insight:
Engineer profesional tidak bertanya
“kenapa error”,
tapi “bagaimana sistem tetap jalan”.

## Hari 4 — Error Collector

Hari ini saya berhenti takut error.
Error saya kumpulkan, bukan saya sembunyikan.

Dengan struktur ini,
saya bisa menjawab klien:
“berapa file gagal, di tahap mana, dan kenapa”.

Insight:
Profesional tidak menghindari error,
mereka mengelolanya.

## Hari 5 — Schema Snapshot

Hari ini saya berhenti fokus ke isi data,
dan mulai melihat bentuknya.

Saya sadar:
banyak masalah data bukan salah nilainya,
tapi karena strukturnya tidak pernah disepakati.

Snapshot schema ini adalah
pondasi untuk menyatukan data yang berbeda.

Engineer melihat struktur
sebelum berpikir tentang kebenaran.

## Hari 6 — Runner & Report

Hari ini semua bagian engine disatukan.
Saya tidak lagi menjalankan file satu-satu,
tapi satu sistem utuh.

Dengan laporan ini,
saya bisa menjelaskan kondisi data
tanpa membuka satu baris kode pun.

Insight:
Kode bekerja untuk saya,
bukan saya bekerja untuk kode.
