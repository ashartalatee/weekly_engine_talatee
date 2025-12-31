# NOTE — Engine 04 Format Anomaly Detector

## Day 1 — Konsep & Fondasi

Hari ini aku belum menulis satu baris logika pun.

Fokus hari ini adalah:
- Memahami bahwa format rusak lebih berbahaya dari data kosong
- Menyadari bahwa banyak sistem gagal karena format tidak konsisten
- Menetapkan engine ini sebagai alat AUDIT, bukan cleaning

Insight penting:
- Data bisa terlihat benar tapi salah secara sistem
- Klien tidak peduli regex, mereka peduli dampak
- Auditor data bertugas menunjukkan risiko, bukan memperbaiki diam-diam

Keputusan desain:
- Engine ini hanya mendeteksi & melaporkan
- Tidak ada auto-fix di tahap ini
- Output harus bisa dibaca non-teknis

Alasan engine ini wajib:
Tanpa deteksi format, proses cleaning dan analisis
akan menghasilkan kesimpulan palsu.

## Day 2 — Dataset Rusak & Loader

Hari ini aku sengaja membuat dataset yang terlihat “masuk akal”
namun memiliki banyak format berbeda dalam satu kolom.

Insight penting:
- Data rusak jarang terlihat ekstrem
- Kebanyakan terlihat normal di Excel
- Masalah baru muncul saat digabung atau dianalisis

Keputusan teknis:
- Loader tidak melakukan konversi apa pun
- Semua nilai dibaca apa adanya
- Audit harus berbasis kondisi nyata, bukan asumsi

Pelajaran:
Jika loader langsung membersihkan data,
maka kita kehilangan bukti kerusakan format.


## Day 3 — Date Format Anomaly Detection

Hari ini aku belajar bahwa:
- Tanggal bisa terlihat valid tapi tetap berbahaya
- Perbedaan format adalah risiko, bukan kosmetik

Insight:
- Parsing langsung ke datetime menyembunyikan masalah
- Regex lebih jujur untuk tahap audit

Temuan penting:
- Tidak ada format tanggal dominan
- Satu kolom memiliki banyak generasi format

Kesimpulan:
Kolom tanggal tanpa standar adalah
sumber bug, salah analisis, dan laporan menyesatkan.
Tambahan insight:
Regex mendeteksi bentuk, bukan kebenaran nilai.
Tanggal `2023-13-01` lolos format tapi salah makna.

Ini bukan bug.
Ini bukti bahwa:
- Audit format dan validasi nilai adalah dua tahap berbeda
- Engine ini harus berhenti di deteksi bentuk

Kesimpulan baru:
Format konsisten belum tentu aman.
Tapi format tidak konsisten sudah pasti berbahaya.

## Day 4 — Numeric & Currency Format Anomaly

Hari ini aku menyadari:
- Angka adalah sumber kebohongan data paling berbahaya
- Data terlihat “masuk akal” tapi salah total saat dijumlahkan

Insight:
- Convert angka terlalu cepat menyembunyikan risiko
- Audit harus melihat simbol, separator, dan konteks

Temuan:
- Locale bercampur dalam satu kolom
- Currency tidak distandarkan
- Format angka tidak konsisten

Kesimpulan:
Jika angka tidak diaudit formatnya,
maka semua perhitungan di atasnya tidak bisa dipercaya.

Catatan penting:
Beberapa format angka terlihat valid secara regex
namun ambigu secara makna (contoh: 1.000).

Ini bukan kesalahan deteksi,
melainkan bukti bahwa format data tidak aman.

Insight auditor:
- Ambigu = risiko
- Sistem bisa salah menafsirkan nilai

## Day 5 — Text Format & Pattern Grouping

Hari ini aku berhenti menghitung error baris
dan mulai melihat pola kerusakan.

Insight penting:
- Klien tidak butuh daftar error
- Klien butuh ringkasan jenis masalah

Temuan:
- Casing tidak konsisten
- Spasi & simbol muncul acak
- Satu kolom punya banyak gaya penulisan

Kesimpulan:
Pattern grouping mengubah data mentah
menjadi insight yang bisa dijelaskan ke bisnis.
Catatan penting:
Ringkasan pola jauh lebih bernilai
daripada daftar baris rusak.

Dengan satu tabel ringkasan,
klien bisa memahami risiko data mereka
tanpa melihat kode.

## Day 6 — Client-Ready Report

Hari ini engine ini berubah fungsi:
dari alat internal → laporan untuk klien.

Insight:
- Klien tidak butuh kode
- Klien butuh bukti & ringkasan risiko

Keputusan desain:
- Output JSON terstruktur
- Bahasa netral & konsisten
- Siap dipakai engine lain di pipeline

Kesimpulan:
Tanpa reporter, engine tidak bernilai bisnis.
Dengan reporter, engine menjadi aset agency.

## Day 7 — Finalisasi & Publish Readiness

Hari ini engine ini aku kunci sebagai versi stabil.

Yang berubah:
- README berbicara ke klien
- Struktur rapi & konsisten
- Test minimal ditambahkan

Refleksi:
Engine ini bukan sekadar detektor format,
tapi alat komunikasi risiko data.

Jika suatu hari aku lupa detail teknisnya,
cukup baca note.md ini untuk memahami ulang
cara berpikir auditor di balik engine.
