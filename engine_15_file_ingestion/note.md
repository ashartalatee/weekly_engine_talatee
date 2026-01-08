# NOTE — Engine 15: File Ingestion

## Tujuan Engine Ini
Engine ini dibuat untuk memastikan data
dari dunia nyata yang berantakan
tetap bisa masuk ke sistem tanpa merusak pipeline.

## Masalah Ingestion yang Sering Terjadi
- Klien kirim file dengan nama & format aneh
- Struktur folder berubah-ubah
- File corrupt / kosong
- Akses SFTP tidak stabil
- Satu file gagal → semua proses mati (ini yang ingin dihindari)

## Prinsip Desain yang Saya Pegang
1. Satu file gagal ≠ sistem gagal
2. Semua kegagalan harus tercatat
3. Lebih baik skip dengan log daripada crash
4. Ingestion ≠ cleaning

## Batasan Engine (Disengaja)
- Engine ini tidak memperbaiki data
- Engine ini tidak memaksa format
- Fokus hanya membawa data masuk dengan aman

## Alasan Engine Ini Layak Dijual
Banyak tim bisa cleaning,
tapi gagal sejak ingestion.
Engine ini menyelamatkan proses sebelum terlambat.

## DAY 2 — File Discovery & Detection

### Insight Utama
Masalah ingestion jarang ada di cleaning,
tapi di file yang tidak seharusnya diproses.

### Jenis File Bermasalah yang Ditemui
- File kosong
- File backup / temporary
- File dengan ekstensi salah

### Keputusan Desain
- Discovery ≠ detection
- Discovery hanya cari file
- Detector bertugas memutuskan layak / tidak

### Risiko Jika Tahap Ini Di-skip
- Pipeline crash di tengah
- Error sulit ditelusuri
- Klien menyalahkan sistem, bukan datanya

## DAY 3 — Loader & Format Reality Check

### Insight Utama
Ekstensi file hanyalah janji,
bukan jaminan isi.

### Kasus Gagal yang Ditemui
- CSV rusak tapi lolos ekstensi
- Excel kosong tapi tidak error
- JSON dengan struktur tak terduga

### Keputusan Desain
- Loader tidak pernah melempar exception
- Error dikembalikan sebagai data
- Empty dataframe dianggap gagal

### Risiko Jika Loader Naif
- Pipeline mati mendadak
- Error sulit direproduksi
- Klien kehilangan kepercayaan

## DAY 4 — Error sebagai Aset

### Insight Utama
Error bukan musuh sistem.
Error adalah bukti bahwa sistem bekerja di dunia nyata.

### Jenis Error yang Tercatat
- Invalid extension
- File kosong
- Format rusak
- Gagal parse data

### Keputusan Desain
- Semua error ditulis ke log
- Tidak ada exception dilempar ke atas
- Bahasa log harus bisa dibaca non-teknis

### Dampak ke Bisnis
- Klien tahu file mana yang bermasalah
- Engineer bisa debug tanpa menebak
- Pipeline tidak mati mendadak

## DAY 5 — SFTP adalah Dunia Nyata

### Insight Utama
SFTP bukan masalah teknis murni,
tapi masalah jaringan, credential, dan ekspektasi.

### Risiko Nyata SFTP
- Koneksi drop
- Credential salah
- Folder berubah tanpa pemberitahuan
- File setengah ter-download

### Keputusan Desain
- Semua error SFTP diperlakukan sebagai data
- Tidak ada retry agresif
- Tidak mematikan ingestion lain

### Dampak Profesional
- Sistem tetap hidup walau SFTP bermasalah
- Klien mendapat laporan jelas
- Engineer tidak panik di production

## DAY 6 — Runner & Sistem Nyata

### Insight Utama
Engine baru layak dipakai
ketika bisa dijalankan tanpa menyentuh kode.

### Keputusan Desain
- Semua sumber dikendalikan via config
- Runner hanya orkestrasi
- Tidak ada logika bisnis di runner

### Dampak Profesional
- Mudah dipakai tim
- Mudah dipindah antar klien
- Risiko human error turun drastis

## RANGKUMAN ENGINE 15

### Masalah yang Diselesaikan
File ingestion yang rapuh
dan sering mematikan pipeline.

### Solusi yang Dibangun
Sistem ingestion yang:
- tahan error
- terlog
- bisa dipakai ulang
- tidak bergantung satu sumber

### Pelajaran Terbesar
Masalah data jarang ada di algoritma.
Masalah ada di dunia nyata sebelum data masuk sistem.

### Kapan Engine Ini Dipakai
- Sebelum cleaning
- Sebelum validation
- Sebelum reporting

### Nilai Jual ke Klien
Klien tidak membayar karena file dibaca,
tapi karena sistem **tetap hidup walau data bermasalah**.
