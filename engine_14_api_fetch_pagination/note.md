# Engine 14 — API Fetch & Pagination Engine

## Hari 1 — Struktur & Mental Model

### Kenapa Engine Ini Dibuat
API klien sering:
- Dokumentasinya buruk
- Pagination berbeda-beda
- Error tiba-tiba (timeout, 429, 500)
Banyak agency gagal bukan karena tidak bisa fetch API,
tapi karena engine mereka rapuh dan tidak reusable.

### Masalah Dunia Nyata yang Disasar
- Data API hanya terambil sebagian
- Page berhenti di tengah tanpa sadar
- Script mati → data tidak lengkap → laporan salah

### Batasan Engine Ini
Engine ini:
- Fokus API GET (REST)
- Tidak fokus auth kompleks (OAuth advance di luar scope)
- Mengutamakan stabil & bisa diulang

### Filosofi Desain
- Config > code
- Retry adalah kewajiban, bukan fitur tambahan
- Pagination bukan detail kecil, tapi inti engine

### Catatan untuk Saya di Masa Depan
Kalau membuka engine ini lagi:
- Ingat: ini mesin agency, bukan script cepat
- Jangan ubah logic tanpa cek pagination_rules.yaml
- Semua API aneh pasti bisa ditundukkan dengan config

## Hari 2 — API Client Inti

### Fokus Hari Ini
Membuat satu pintu resmi untuk request API.

### Masalah Dunia Nyata
Tanpa API client terpusat:
- Header beda-beda
- Timeout lupa
- Debug sulit

### Keputusan Teknis
- API client tidak tahu pagination
- Semua config di luar kode
- raise_for_status() biar error kelihatan cepat

### Insight Penting
API client yang terlalu pintar justru menyulitkan.
Biarkan logic lain (pagination, retry) berdiri sendiri.

## Hari 3 — Pagination Engine

### Fokus Hari Ini
Mengambil data API sampai benar-benar habis,
bukan sampai script berhenti.

### Masalah Dunia Nyata
Banyak API:
- Tidak error
- Tapi data berhenti di tengah
Ini bug paling berbahaya karena tidak terlihat.

### Keputusan Teknis
- Pagination dikontrol config
- Stop condition eksplisit
- Loop sederhana, mudah diaudit

### Insight Penting
Pagination bukan fitur kecil.
Ini penentu apakah data bisa dipercaya atau tidak.

### Catatan untuk Masa Depan
Kalau data klien terasa "kurang":
- Cek pagination_rules.yaml
- Jangan langsung curiga ke cleaning

## Hari 4 — Response Parser

### Fokus Hari Ini
Memisahkan response API mentah dari data yang benar-benar dibutuhkan.

### Masalah Dunia Nyata
API sering:
- banyak field tidak relevan
- berubah tanpa pemberitahuan
Tanpa parser, pipeline mudah rusak.

### Keputusan Teknis
- Parsing terpisah dari fetch
- Field selection eksplisit
- Output konsisten

### Insight Penting
Response yang terlihat “benar”
belum tentu data yang siap dipakai.

### Catatan untuk Masa Depan
Kalau data terasa aneh:
- cek apakah field yang diambil sudah benar
- jangan langsung menyalahkan cleaning
## Hari 5 — Retry & Logging

### Fokus Hari Ini
Membuat engine yang tidak panik saat API gagal.

### Masalah Dunia Nyata
API hampir tidak pernah 100% stabil.
Script yang mati diam-diam lebih berbahaya
daripada script yang error keras.

### Keputusan Teknis
- Retry dibungkus, bukan disebar
- Logging sederhana tapi konsisten
- Error tetap dilempar setelah retry habis

### Insight Penting
Engine profesional bukan yang jarang error,
tapi yang jujur saat error.

### Catatan untuk Masa Depan
Kalau data tiba-tiba kosong:
- cek log dulu
- cek retry count
- jangan langsung percaya output
## Hari 6 — Runner & End-to-End

### Fokus Hari Ini
Menyatukan semua komponen menjadi satu alur utuh.

### Masalah Dunia Nyata
Banyak engine terlihat bagus di potongan,
tapi gagal saat digabung.

### Keputusan Teknis
- Runner hanya orkestrator
- Tidak ada logic bisnis di runner
- Semua perilaku lewat config

### Insight Penting
Kalau engine sulit dijalankan ulang,
berarti desainnya belum matang.

### Catatan untuk Masa Depan
Kalau engine ini mau dipakai klien lain:
- cukup ganti api_config.yaml
- jangan sentuh kode inti
## Hari 7 — Publish & Refleksi

### Fokus Hari Ini
Mengubah engine dari “selesai jalan”
menjadi “layak dipamerkan & dipakai”.

### Pelajaran Terbesar
- Engine bukan soal banyak fitur
- Engine adalah soal batas, kejelasan, dan kejujuran error

### Yang Bisa Ditingkatkan Nanti
- Cursor-based pagination
- Auth lebih kompleks
- Metrics & monitoring

### Catatan Terakhir untuk Saya
Engine ini dibangun pelan tapi benar.
Ini aset, bukan tugas.
