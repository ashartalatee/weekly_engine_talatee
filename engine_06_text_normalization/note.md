# NOTE — Engine 06 Text Normalization
## Day 1 — Memahami Kerusakan Text Dunia Nyata

Hari ini saya belum menulis banyak kode.
Fokus saya adalah memahami bagaimana text rusak di data klien.

Contoh kerusakan yang saya temui:
- Spasi berlebih
- Huruf besar/kecil tidak konsisten
- Singkatan (jl, jln, jalan)
- Typo ringan
- Variasi penulisan kategori
- Angka ditulis sebagai teks

Insight penting:
Text normalization bukan soal "membersihkan",
tapi soal "menyetujui satu standar bersama".

Kesalahan yang harus dihindari:
- Hardcode aturan di dalam script
- Mengira semua text harus sempurna
- Terlalu agresif mengubah data

Batas engine ini:
- Tidak memperbaiki typo kompleks
- Tidak menggunakan AI
- Fokus pada konsistensi, bukan kecerdasan

## Day 2 — Rule Adalah Kontrak, Bukan Kode

Hari ini saya tidak mengejar kesempurnaan aturan.
Saya mendesain rule yang:
- bisa dibaca manusia
- bisa diubah tanpa menyentuh code
- cukup aman untuk sebagian besar klien

Insight penting:
Rule yang baik lebih bernilai dari code yang pintar.

Saya sadar:
Kalau setiap perubahan text harus ubah script,
berarti saya belum membangun engine.

Kesalahan yang dihindari:
- Hardcode mapping di Python
- Over-normalization
- Menganggap semua klien sama

## Day 3 — Mesin Umum Lebih Penting dari Kasus Spesifik

Hari ini saya menulis core normalizer yang tidak tahu konteks data.
Ia hanya tahu satu hal: mengikuti aturan.

Insight penting:
Engine yang baik tidak pintar,
tapi patuh pada kontrak (config).

Saya sengaja:
- Tidak memasukkan logic nama
- Tidak memasukkan mapping kategori
- Tidak memasukkan alamat

Karena:
Jika core ini stabil,
engine lain tinggal menumpang.

Kesalahan yang saya hindari:
- Langsung membuat logic spesifik
- Menggabungkan semua kasus di satu file

## Day 4 — Layer Spesifik Adalah Tempat Nilai Bisnis

Hari ini saya menambahkan normalizer khusus
tanpa menyentuh core engine.

Insight penting:
Nilai bisnis tidak ada di core,
tapi di layer spesifik yang bisa diganti per klien.

Saya sengaja:
- Membuat NameNormalizer dan CategoryNormalizer terpisah
- Mengontrol semuanya lewat config

Ini membuat engine:
- Lebih aman
- Lebih mudah dirawat
- Lebih mudah dijual

Kesalahan yang saya hindari:
- Menyatukan semua logic dalam satu file
- Mengubah core demi satu kasus klien

## Day 5 — Address Tidak Boleh Disokpintarkan

Hari ini saya sadar:
Alamat adalah data paling berisik dan tidak stabil.

Tujuan engine ini:
- Membuat alamat konsisten
- Bukan membuat alamat "benar 100%"

Insight penting:
Address normalization harus konservatif.
Lebih baik kurang agresif daripada merusak data.

Batas tegas engine:
- Tidak mengubah angka jadi teks
- Tidak menebak wilayah
- Tidak menggunakan AI

Ini penting agar:
- Klien percaya
- Data tidak rusak diam-diam

## Day 6 — Engine Harus Bisa Berjalan Sendiri

Hari ini saya menghubungkan semua bagian engine.
Bukan lagi potongan script, tapi satu alur kerja.

Insight penting:
Runner adalah wajah engine.
Kalau runner rapi, engine dipercaya.

Saya juga sadar:
Test bukan untuk membuktikan saya pintar,
tapi untuk menjaga agar engine tidak rusak di masa depan.

Dengan ini, engine sudah:
- Bisa dijalankan
- Bisa dicek hasilnya
- Bisa dijelaskan ke orang lain
