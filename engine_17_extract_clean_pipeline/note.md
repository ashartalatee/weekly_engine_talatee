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

# Day 02 — Pipeline Mental Model

Pipeline bukan soal urutan teknis,
tapi urutan tanggung jawab.

Extract bertugas membawa data masuk.
Clean bertugas memperbaiki sebisanya.
Validate bertugas melindungi sistem.

Keputusan penting hari ini:
- Pipeline boleh berhenti
- Validasi punya hak veto
- Semua stage dikontrol config

Insight:
Banyak sistem data rusak karena tidak ada titik
di mana data boleh ditolak secara resmi.

# Day 03 — Extractor Wrapper

Hari ini saya sadar extractor bukan alat scraping,
tapi adaptor antara dunia luar dan pipeline.

Keputusan desain:
- Extractor hanya bertugas memindahkan data
- Tidak ada cleaning, tidak ada validasi
- Output selalu file + metadata

Insight:
Masalah data sering muncul karena extractor terlalu pintar
dan mencampur tanggung jawab.

# Day 04 — Cleaner Wrapper

Hari ini saya memisahkan antara:
- aturan pembersihan
- mesin pembersihan

Keputusan penting:
- Semua rule datang dari config
- Cleaner tidak tahu konteks bisnis
- Logic dibuat generik dan tahan lama

Insight:
Cleaner yang terlalu pintar cepat usang.
Cleaner yang patuh pada config bisa hidup lama.

# Day 05 — Validator & Quality Gate

Hari ini saya sadar validator bukan alat teknis,
tapi alat keberanian.

Validator tidak memperbaiki data.
Ia melindungi sistem dari data buruk.

Keputusan penting:
- Kualitas data diukur, bukan dirasa
- Data boleh ditolak secara resmi
- Pipeline berhak berhenti

Insight:
Tanpa quality gate, semua laporan adalah kebohongan yang tertunda.

# Day 06 — Pipeline Orchestrator

Hari ini saya berhenti menulis script.
Saya mulai menulis sistem.

Pipeline tidak peduli bagaimana data diproses.
Pipeline hanya peduli:
- urutan
- keputusan
- tanggung jawab

Insight:
Orchestrator yang baik itu bodoh secara teknis,
tapi pintar secara arsitektur.
