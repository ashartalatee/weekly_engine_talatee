# ENGINE 08 — Date & Time Harmonization
## Day 1 — Masalah Dunia Nyata

Hari ini fokus memahami:
- Tanggal tidak pernah berdiri sendiri
- Format adalah asumsi
- Timezone adalah konteks

Masalah utama yang ditemukan:
1. Format ambigu (01/02/2024)
2. Locale tidak jelas (ID / US / EU)
3. Timezone bercampur
4. Jam & tanggal tidak masuk akal
5. Banyak sistem menganggap tanggal = string

Kesimpulan penting:
Tanggal bukan masalah parsing,
tapi masalah kejujuran waktu.

Engine ini tidak akan:
- menebak sembarangan
- membuang data

Engine ini akan:
- mendeteksi
- menormalisasi
- melaporkan

## Day 2 — Deteksi Format Tanggal

Pelajaran penting:
- Deteksi ≠ parsing
- Format adalah hipotesis, bukan fakta
- Prioritas membantu memilih, bukan memaksa

Engine ini tidak akan:
- memaksa parse
- menganggap satu format paling benar

Engine ini akan:
- mencoba
- menilai
- menyerahkan keputusan ke tahap berikutnya

## Day 3 — Parsing & Normalization

Pelajaran penting:
- Parsing hanya boleh dilakukan setelah deteksi
- Normalisasi adalah keputusan sistem, bukan tebakan
- Output konsisten lebih penting dari data lengkap

Engine ini memilih:
- None daripada salah
- konsistensi daripada ego parsing

## Day 4 — Timezone Handling

Pelajaran penting:
- Datetime tanpa timezone adalah asumsi
- Asumsi waktu = laporan salah
- Lebih baik pakai default eksplisit daripada diam

Keputusan engine:
- Semua output ke UTC
- Default timezone didefinisikan
- Timezone ambigu tidak disembunyikan

## Day 5 — Validasi Logis

Pelajaran penting:
- Data yang lolos bukan berarti benar
- Validasi adalah keberanian, bukan kekejaman
- Menandai lebih baik daripada menghapus

Engine ini:
- berani bilang STOP
- memberi alasan
- menjaga kepercayaan laporan

## Ringkasan Engine 08

Engine ini mengajarkan bahwa:
- waktu adalah konteks
- asumsi adalah musuh
- laporan adalah produk

Engine ini akan dipakai ulang
di pipeline extract–clean–report selanjutnya.

Status:
✅ Siap dipakai
✅ Siap diintegrasikan
✅ Siap dipamerkan
