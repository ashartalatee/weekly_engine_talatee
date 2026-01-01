# ENGINE 05 — Rule-Based Cleaning Engine
# DAY 1 — Boundary & Identity

## Tujuan Hari Ini
Menentukan batas tegas engine:
- apa yang DITANGANI
- apa yang TIDAK ditangANI
agar engine ini tidak berubah menjadi script ad-hoc.

## Masalah Dunia Nyata
Setiap klien selalu minta:
“tolong bersihkan data ini”
tanpa definisi jelas:
- bersih menurut siapa?
- konsisten sampai kapan?
- bisa dipakai ulang atau tidak?

Tanpa sistem aturan, cleaning selalu:
- manual
- diulang
- tidak bisa distandarkan
- tidak bisa dijual mahal

## Definisi Engine Ini
Engine ini adalah:
> Mesin pembersih data berbasis ATURAN (rule-based),
bukan intuisi manusia.

Engine bekerja dengan prinsip:
- Semua keputusan cleaning HARUS berasal dari konfigurasi
- Kode tidak mengenal konteks klien
- Kode hanya mengeksekusi aturan

## Yang Ditangani Engine
Engine ini MENANGANI:
1. Text cleaning
   - trim
   - lowercase / uppercase
   - replace map
   - regex cleanup

2. Numeric cleaning
   - hapus simbol
   - normalisasi decimal & thousand separator
   - cast ke tipe numerik

3. Date cleaning
   - parsing berbagai format tanggal
   - output format tunggal

## Yang TIDAK Ditangani Engine
Engine ini TIDAK MENANGANI:
- Outlier detection berbasis statistik
- AI / ML / fuzzy logic
- Koreksi data berdasarkan asumsi bisnis
- Validasi kebenaran nilai (itu engine lain)

Jika data butuh itu → pipeline lain.

## Prinsip Arsitektur
1. Config adalah sumber kebenaran
2. Jika rule tidak valid → engine HARUS berhenti
3. Lebih baik gagal daripada hasil salah
4. Engine harus bisa dipakai klien berbeda tanpa ubah kode

## Dampak ke Level Keahlian
Dengan engine ini:
- Saya tidak lagi “membersihkan data”
- Saya membangun STANDAR pembersihan
- Saya bisa menyimpan, mengulang, dan menjual aturan

## Kalimat Pegangan
“Saya tidak membersihkan data.
Saya membangun standar pembersihan data.”

## Catatan Pribadi
Engine ini adalah titik transisi:
dari tukang bersih → pembuat sistem.

# DAY 2 — Cleaning Rules Design

## Tujuan Hari Ini
Mendesain bahasa aturan (cleaning rules)
yang memisahkan:
- niat pembersihan
- cara pembersihan

## Kenapa Rules Lebih Penting dari Kode
Kode bisa berubah.
Aturan bisa dipakai ulang.

Klien tidak peduli bagaimana kodenya bekerja,
mereka peduli:
“aturan data saya apa?”

## Prinsip Desain Rules
1. Satu kolom = satu definisi cleaning
2. Semua aksi eksplisit dan berurutan
3. Tidak ada asumsi tersembunyi
4. Rules harus bisa dibaca tanpa buka kode

## Insight Penting Hari Ini
Jika aturan cleaning bisa dijelaskan ke klien,
maka engine ini layak dijual sebagai sistem,
bukan jasa manual.

# DAY 3 — Rule Loader & Validation

## Tujuan Hari Ini
Membuat engine yang berani berkata:
“aturan ini salah — saya tidak akan jalan.”

## Kenapa Validasi Itu Wajib
Silent error = data rusak diam-diam.
Data rusak diam-diam = reputasi hancur.

Lebih baik engine berhenti
daripada klien percaya pada data salah.

## Prinsip Hari Ini
1. Rules adalah kontrak
2. Kontrak harus divalidasi
3. Engine tidak boleh menebak

## Insight Penting Hari Ini
Engineer sejati bukan yang kodenya panjang,
tapi yang berani menghentikan sistem saat salah.

# DAY 4 — Text Cleaning Engine

## Tujuan Hari Ini
Membangun text cleaning engine
yang tidak bergantung kolom, klien, atau dataset.

## Prinsip Implementasi
1. Semua aksi berasal dari rules
2. Urutan aksi menentukan hasil
3. Engine tidak mengubah data tanpa perintah eksplisit

## Kenapa Text Sangat Penting
Sebagian besar data dunia nyata adalah text.
Jika text cleaning tidak rapi,
seluruh pipeline akan terlihat amatir.

## Insight Penting Hari Ini
Kekuatan engine ini bukan pada kecerdasannya,
tapi pada kepatuhannya terhadap aturan.

# DAY 5 — Numeric & Date Cleaning Engine

## Tujuan Hari Ini
Membangun cleaning engine untuk angka dan tanggal
yang tegas, eksplisit, dan tidak menebak.

## Kenapa Numeric & Date Sangat Sensitif
Kesalahan kecil di angka atau tanggal
bisa mengubah:
- laporan keuangan
- keputusan bisnis
- kepercayaan klien

## Prinsip Implementasi
1. Hapus noise secara eksplisit
2. Parsing hanya dengan format yang diizinkan
3. Gagal jika data tidak sesuai aturan

## Insight Penting Hari Ini
Profesionalisme data terlihat
bukan dari seberapa banyak data diproses,
tapi dari keberanian menolak data yang salah.

# DAY 6 — Dispatcher & Runner

## Tujuan Hari Ini
Menghubungkan semua cleaning engine
menjadi satu alur kerja utuh.

## Arsitektur Alur
Rules → Dispatcher → Cleaning Engine → Output

Kode tidak mengenal:
- klien
- nama kolom
- konteks bisnis

Kode hanya patuh aturan.

## Kenapa Dispatcher Penting
Tanpa dispatcher:
- logic tercecer
- engine sulit diskalakan
- sistem cepat rusak

Dispatcher adalah pemisah
antara niat (rules) dan eksekusi (kode).

## Insight Penting Hari Ini
Engine yang baik bukan yang pintar,
tapi yang taat aturan dan mudah diarahkan.

# DAY 7 — Publish & Reflection

## Tujuan Hari Ini
Menjadikan engine ini layak dipublikasikan
sebagai sistem profesional, bukan latihan.

## Yang Dibuktikan Engine Ini
- Saya mampu membangun sistem data berbasis aturan
- Saya memahami masalah data dunia nyata
- Saya tidak tergantung pada satu dataset atau klien

## Dampak ke Identitas Profesional
Engine ini adalah bukti bahwa saya:
bukan sekadar menulis script,
melainkan membangun mesin yang bisa bekerja berulang.

## Penutup
Engine ini akan menjadi fondasi
untuk pipeline yang lebih besar,
bukan akhir perjalanan.

