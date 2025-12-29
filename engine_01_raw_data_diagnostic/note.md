# Note — Engine 01 Raw Data Diagnostic
## Hari 1 — Struktur & Tujuan

### Kenapa Hari Ini Tidak Coding
Hari ini fokus ke struktur karena:
- data cleaning tanpa struktur selalu berantakan
- engine ini akan jadi fondasi banyak engine lain
- struktur yang salah akan menyulitkan scaling

### Masalah Nyata yang Ingin Diselesaikan
Klien sering:
- langsung minta data dibersihkan
- tidak sadar data mereka rusak parah
- tidak punya gambaran kondisi awal data

Engine ini dibuat untuk:
- menunjukkan kondisi data secara objektif
- memberi dasar keputusan: lanjut, berhenti, atau perbaiki proses

### Prinsip yang Dipakai
- Diagnosis sebelum treatment
- Fakta sebelum asumsi
- Laporan lebih penting dari script

### Catatan untuk Future Me
Kalau suatu hari merasa:
“Kenapa engine ini ribet?”

Ingat:
Tanpa diagnostic, semua cleaning adalah tebakan.

## Hari 2 — Data Sample & Loader

### Kenapa Data Sample Harus Jelek
Hari ini aku sengaja membuat data yang:
- formatnya campur aduk
- ada duplikat
- ada missing
- kelihatan “menyebalkan”

Karena:
Data klien hampir selalu seperti ini.
Data rapi itu pengecualian, bukan aturan.

### Pelajaran Penting
Masalah data bukan cuma teknis.
Masalah data = jejak proses bisnis yang tidak rapi.

### Tentang Loader
Loader hari ini:
- tidak memperbaiki apa pun
- hanya membaca & melaporkan

Ini penting supaya:
- diagnostic tidak bias
- kesalahan terlihat apa adanya

### Catatan untuk Future Me
Kalau suatu hari tergoda langsung cleaning:
ingat, tanpa melihat data mentah,
kamu sedang menipu dirimu sendiri.

## Hari 3 — Missing & Null Pattern

### Insight Hari Ini
Missing data jarang acak.
Kalau satu kolom banyak kosong,
biasanya ada proses bisnis yang gagal.

### Kenapa Pakai Rasio, Bukan Jumlah
Jumlah missing bisa menipu:
- 10 missing di 1.000 baris = biasa
- 10 missing di 20 baris = bahaya

Rasio membantu melihat tingkat kerusakan.

### Tentang Severity
Aku tidak mau hanya bilang:
“ada missing”

Aku ingin bisa bilang:
- aman
- perlu perhatian
- berbahaya

### Catatan untuk Future Me
Kalau tergoda langsung isi missing:
ingat, missing adalah pesan,
bukan sekadar kekurangan data.

## Hari 4 — Duplicate & Near-Duplicate

### Insight Hari Ini
Duplikat = risiko nyata:
- Laporan keuangan bisa double
- Analisis marketing salah target
- KPI jadi bias

Exact vs Near:
- Exact: identik persis, biasanya sistem export/import
- Near: typo, spasi, huruf besar kecil, mirip tapi tidak sama

### Pelajaran
- Tidak semua duplikat perlu dihapus
- Fokus: **tunjukkan problem ke klien** dan biarkan mereka ambil keputusan

### Catatan untuk Future Me
Kalau tergoda langsung hapus:
ingat, duplikat = sinyal proses bisnis salah.

## Hari 5 — Format & Schema Anomaly

### Insight Hari Ini
- Format tanggal berbeda-beda → risiko error laporan & pivot table
- Format angka campur simbol → risiko financial miscalculation
- Schema beda urutan/kolom → pipeline bisa crash

### Prinsip
- Tidak membersihkan dulu
- Fokus: deteksi → lapor → insight
- Engine ini adalah **alat komunikasi ke bisnis & tim**

### Catatan untuk Future Me
Kalau suatu hari tergoda langsung ubah format:
ingat, ini masih **diagnostic**
Format adalah sinyal integritas data

## Hari 6 — Runner & Report

### Insight Hari Ini
- Semua modul dari Hari 2–5 digabung jadi **satu mesin diagnostic**
- Report JSON bisa dibaca non-teknis → klien bisa percaya
- Logging & trace → bukti profesionalisme

### Pelajaran
- Integrasi > coding satu per satu
- Output = bukti nilai, bukan jumlah baris
- Struktur modular membuat engine ini scalable

### Catatan untuk Future Me
Kalau buka repo ini lagi:
- Ingat, diagnostic = mata & insting
- Runner = cara otak memproses semua sinyal data
- Jangan tergoda langsung cleaning → dulu pahami masalahnya
