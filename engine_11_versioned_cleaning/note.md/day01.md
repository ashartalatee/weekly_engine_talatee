# Engine 11 — Day 01
## Konsep Versioned Cleaning Engine

### Masalah Dunia Nyata
Klien sering mengirim revisi data tanpa tahu:
- apa yang berubah
- apakah data makin baik atau makin rusak
- apakah cleaning sebelumnya masih relevan

Tanpa versioning:
- kerja diulang dari nol
- tidak ada bukti profesional
- sulit menjelaskan ke klien

### Tujuan Engine Ini
Membuat sistem yang:
- menyimpan setiap versi data
- membandingkan perubahan antar versi
- menghasilkan laporan yang bisa dijelaskan ke non-teknis

### Insight Hari Ini
Cleaning tanpa versioning = kerja tukang.
Cleaning dengan versioning = kerja engineer.

Engine ini bukan untuk membersihkan data,
tapi untuk MEMPERTANGGUNGJAWABKAN perubahan data.

### Risiko Jika Diskip
- Engine 17–24 tidak punya fondasi
- Tidak bisa audit
- Tidak bisa scale ke agency
