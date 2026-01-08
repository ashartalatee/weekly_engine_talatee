# Engine 16 — Retry, Logging & Fail-Safe
## Day 1 — Fondasi & Cara Berpikir

### 1. Masalah Dunia Nyata
- Banyak job data mati total hanya karena 1 error kecil
- Klien tidak peduli stack trace
- Klien bertanya: “Data saya aman atau tidak?”

### 2. Kenapa Engine Ini Penting
- Semua engine extraction akan gagal TANPA ini
- Retry asal-asalan = sistem tidak profesional
- Logging buruk = tidak bisa audit

### 3. Prinsip yang Saya Pegang
- Error harus diklasifikasikan
- Tidak semua error layak di-retry
- Sistem harus bisa lanjut walau sebagian gagal

### 4. Definisi Awal
- Retry = usaha ulang TERBATAS untuk error sementara
- Fatal error = dihentikan, dicatat, tidak diulang
- Fail-safe = sistem tetap jalan

### 5. Catatan untuk Saya di Masa Depan
(Jelaskan dengan bahasa sendiri: 
kenapa engine ini penting dan 
apa yang akan rusak kalau dihapus)

## Day 2 — Logger Terpusat

### 1. Masalah Nyata
- Print tidak bisa diaudit
- Error hilang saat script mati
- Klien bertanya: “Kenapa gagal?”

### 2. Keputusan Desain
- Satu logger untuk semua engine
- Format JSON agar bisa dianalisis
- Pisahkan log umum & error

### 3. Pelajaran Penting
- Logger ganda = bencana debugging
- Logger bukan alat developer, tapi alat kepercayaan

### 4. Catatan untuk Masa Depan
Jika engine lain tidak pakai logger ini,
berarti desain sistem sedang rusak.

## Day 3 — Retry Policy & Backoff

### 1. Insight Penting
- Retry tanpa aturan = menyiksa sistem
- Tidak semua error layak dicoba ulang

### 2. Keputusan Sistem
- Retry dibatasi jumlahnya
- Delay meningkat (backoff)
- Retry menghasilkan log

### 3. Dampak ke Engine Lain
- API engine akan lebih stabil
- Batch job tidak mudah mati
- Error lebih mudah dilacak

### 4. Catatan Masa Depan
Jika kamu melihat retry loop tak berujung,
berarti prinsip hari ini dilanggar.

## Day 4 — Error Classification

### 1. Insight Penting
- Menyamakan semua error = sistem bodoh
- Error adalah sinyal, bukan gangguan

### 2. Keputusan Sistem
- Error dibagi retryable & fatal
- Retry policy tunduk pada klasifikasi
- Semua engine pakai standar yang sama

### 3. Dampak ke Agency
- Lebih mudah jelaskan ke klien
- Sistem terlihat dewasa
- Debugging lebih cepat

### 4. Catatan Masa Depan
Jika kamu tergoda menambahkan `except Exception`
tanpa klasifikasi, berhenti dan baca ulang note ini.

## Day 5 — Fail-Safe Wrapper

### 1. Masalah Dunia Nyata
- Batch job mati karena 1 data rusak
- Tidak ada catatan apa yang gagal
- Semua harus diulang dari nol

### 2. Prinsip Fail-Safe
- Error dicatat, bukan disembunyikan
- Sistem harus lanjut
- Gagal = data, bukan bencana

### 3. Dampak ke Agency
- Job besar jadi aman dijalankan
- Klien percaya sistem tahan banting
- Re-run bisa selektif

### 4. Catatan Masa Depan
Jika kamu melihat sistem mati total,
berarti fail-safe tidak dipakai.

## Day 6 — Runner & Simulasi Dunia Nyata

### 1. Apa yang Terjadi Saat Dijalankan
- Tidak semua job berhasil
- Sistem tetap jalan
- Semua kegagalan tercatat

### 2. Insight Terpenting
- Gagal itu normal
- Sistem profesional mengelola kegagalan

### 3. Dampak ke Engine Lain
- Engine extraction aman
- Batch processing stabil
- Pipeline bisa dipercaya

### 4. Catatan Masa Depan
Jika sistem terlihat “rapuh”,
cek kembali runner ini.


---

## Day 7 — Publish & Refleksi

### 1. Apa yang Berubah
- Saya tidak lagi takut error
- Saya mengontrol kegagalan
- Sistem saya bisa dipercaya

### 2. Pelajaran Terpenting
- Stabilitas lebih penting dari fitur
- Logger & fail-safe bukan tambahan, tapi fondasi

### 3. Dampak ke Identitas Profesional
- Ini bukan script
- Ini engine yang bisa dijual
- Ini dasar agency

### 4. Catatan untuk Masa Depan
Engine lain WAJIB pakai ini.
Kalau tidak, berarti standar turun.
