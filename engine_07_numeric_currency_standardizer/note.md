# Engine 07 — Numeric & Currency Standardizer
## Day 01 — Insting Kerusakan Angka

### 1. Tujuan Hari Ini
Melatih mata & otak untuk melihat kerusakan angka dunia nyata,
bukan langsung menulis kode.

---

### 2. Jenis Kerusakan Angka yang Ditemukan

| Contoh | Jenis Masalah | Catatan |
|------|--------------|--------|
| Rp 1.250.000 | Currency + locale | |
| 1.200,50 | European format | |
| 2.5M | Multiplier | |
| (2,000) | Accounting negative | |
|  | Missing value | |

---

### 3. Insight Penting Hari Ini
(TULIS DENGAN KATA-KATA KAMU SENDIRI)

Contoh:
- Selama ini angka terlihat rapi, tapi secara sistem tidak bisa dipercaya.
- Banyak keputusan bisnis berdiri di atas angka yang ambigu.
- Normalisasi angka adalah fondasi kepercayaan data.

---

### 4. Prinsip yang Akan Saya Pegang di Engine Ini
- Tidak semua data harus diselamatkan.
- Lebih baik STOP daripada salah.
- Semua keputusan parsing harus bisa dijelaskan ke klien.

---
# Engine 07 — Numeric & Currency Standardizer
## Day 02 — Deteksi Format & Locale

### 1. Apa yang Saya Bangun Hari Ini
Saya membangun layer keputusan awal yang
MENENTUKAN bentuk angka sebelum parsing.

---

### 2. Keputusan Penting yang Saya Ambil

| Kasus | Keputusan | Alasan |
|-----|---------|--------|
| 1,200.50 | US_FORMAT | |
| 1.200,50 | EU_FORMAT | |
| Rp 1.250.000 | CURRENCY_OR_TEXT | |
| (2,000) | ACCOUNTING_NEGATIVE | |

---

### 3. Risiko & Ambiguitas
Contoh:
- 1.234 bisa ribuan atau desimal
- Engine tidak boleh menebak tanpa konteks

---

### 4. Prinsip yang Saya Pegang
- Deteksi dulu, parsing belakangan
- Salah deteksi > salah hitung
- Semua logika harus explainable

---
# Engine 07 — Numeric & Currency Standardizer
## Day 02 — Deteksi Format & Locale

### 1. Apa yang Saya Bangun Hari Ini
Saya membangun layer keputusan awal yang
MENENTUKAN bentuk angka sebelum parsing.

---

### 2. Keputusan Penting yang Saya Ambil

| Kasus | Keputusan | Alasan |
|-----|---------|--------|
| 1,200.50 | US_FORMAT | |
| 1.200,50 | EU_FORMAT | |
| Rp 1.250.000 | CURRENCY_OR_TEXT | |
| (2,000) | ACCOUNTING_NEGATIVE | |

---

### 3. Risiko & Ambiguitas
Contoh:
- 1.234 bisa ribuan atau desimal
- Engine tidak boleh menebak tanpa konteks

---

### 4. Prinsip yang Saya Pegang
- Deteksi dulu, parsing belakangan
- Salah deteksi > salah hitung
- Semua logika harus explainable

---

# Engine 07 — Numeric & Currency Standardizer
## Day 03 — Numeric Normalization Core

### 1. Tujuan Hari Ini
Mengubah angka string menjadi float bersih
tanpa asumsi berlebihan.

---

### 2. Urutan Parsing yang Saya Gunakan
1. Validasi input
2. Deteksi format
3. Tangani negatif
4. Bersihkan separator
5. Standarkan desimal
6. Konversi ke float

---

### 3. Keputusan Penting
- Format ambigu TIDAK dipaksa
- Multiplier ditunda ke engine lain
- Error lebih baik daripada salah

---

### 4. Masalah yang Saya Temui
(TULIS ERROR & KEBINGUNGANMU)

---
# Engine 07 — Numeric & Currency Standardizer
## Day 04 — Currency & Multiplier

### 1. Tujuan Hari Ini
Memisahkan nilai bisnis (angka) dari konteks bisnis (currency).

---

### 2. Keputusan Arsitektur
- Currency disimpan terpisah
- Multiplier diproses sebelum numeric normalizer
- Aturan currency via YAML

---

### 3. Insight Penting
- Banyak data finance salah karena currency disimpan sebagai string.
- Currency tanpa konteks = laporan menipu.

---

### 4. Risiko yang Saya Sadari
- Multiplier ambigu
- Currency campur dalam satu kolom

---
# Engine 07 — Numeric & Currency Standardizer
## Day 05 — Validation & Quality Gate

### 1. Perubahan Mindset Hari Ini
Saya sadar bahwa data engineer
punya hak dan kewajiban untuk MENOLAK data.

---

### 2. Aturan Validasi yang Saya Terapkan

| Aturan | Alasan |
|-----|--------|
| value tidak None | |
| currency wajib | |
| range wajar | |

---

### 3. Insight Penting
- Banyak laporan salah bukan karena kode, tapi karena data jelek dibiarkan lolos.
- Quality gate melindungi reputasi engineer.

---

### 4. Risiko Bisnis yang Saya Sadari
- Data lolos tanpa konteks
- Angka ekstrem tanpa verifikasi

---
# Engine 07 — Numeric & Currency Standardizer
## Day 06 — Runner & Batch Processing

### 1. Perubahan Besar Hari Ini
Engine saya sekarang bisa memproses
banyak data sekaligus dan menghasilkan output nyata.

---

### 2. Alur Engine yang Saya Bangun
input CSV → normalize → validate → output + report

---

### 3. Insight Penting
- Error tidak boleh menghentikan seluruh batch.
- Report lebih penting daripada exception stacktrace.

---

### 4. Hal yang Ingin Saya Tingkatkan
- CLI interface
- Config validation rules

---

---
# Engine 07 — Numeric & Currency Standardizer
## Ringkasan Pembelajaran

### Kenapa Engine Ini Saya Bangun
Karena angka adalah fondasi keputusan bisnis,
dan fondasi ini sering rapuh tanpa disadari.

---

### Perubahan Cara Pikir Saya
- Tidak semua data harus diselamatkan
- Validasi adalah tanggung jawab moral engineer
- Report lebih penting dari script pintar

---

### Skill yang Saya Kunci
- Numeric normalization lintas locale
- Currency handling yang benar
- Quality gate & audit mindset
- Batch processing nyata

---

### Pesan untuk Saya di Masa Depan
Engine ini bukan soal angka,
tapi soal kepercayaan.
