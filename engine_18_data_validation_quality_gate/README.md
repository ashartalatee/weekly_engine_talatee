# Engine 18 — Data Validation & Quality Gate

Engine ini bertugas MENILAI apakah data layak dipakai
sebelum masuk ke pipeline cleaning, analisis, atau reporting.

Engine ini tidak memperbaiki data.
Engine ini menentukan apakah data BOLEH DIPAKAI.

## Masalah Dunia Nyata
Banyak sistem memproses data tanpa tahu apakah data tersebut
cukup aman untuk dijadikan dasar keputusan bisnis.

## Solusi
Engine ini menerapkan serangkaian validation rules
dan quality threshold untuk menghasilkan keputusan:
PASS, WARN, atau FAIL.

## Prinsip Utama
- Lebih baik STOP daripada salah
- Tidak semua error punya bobot yang sama
- Kualitas data adalah keputusan, bukan angka
