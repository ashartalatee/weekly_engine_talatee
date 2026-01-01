# Engine 05 — Rule-Based Cleaning Engine

## Apa Ini?
Engine ini adalah sistem pembersihan data berbasis aturan (rule-based)
yang dirancang untuk kebutuhan dunia nyata:
- data klien yang berantakan
- aturan berbeda tiap proyek
- kebutuhan konsistensi jangka panjang

Engine ini **tidak membersihkan data secara manual**,
melainkan **mengeksekusi standar pembersihan** yang didefinisikan lewat konfigurasi.

---

## Masalah Dunia Nyata
Dalam banyak proyek data:
- cleaning dilakukan manual
- aturan tidak terdokumentasi
- hasil tidak konsisten
- pekerjaan selalu diulang dari nol

Engine ini menyelesaikan masalah tersebut
dengan memisahkan:
**aturan pembersihan** dan **kode eksekusi**.

---

## Prinsip Utama
1. Semua keputusan cleaning berasal dari rules (YAML)
2. Kode tidak mengenal konteks klien
3. Rules dapat dipakai ulang lintas proyek
4. Engine berhenti jika aturan atau data tidak valid

---

---

## Cara Kerja Singkat
1. Tentukan aturan pembersihan di `cleaning_rules.yaml`
2. Jalankan `runner.py`
3. Engine akan:
   - memvalidasi rules
   - membersihkan data sesuai urutan aksi
   - menghentikan proses jika terjadi kesalahan
   - menghasilkan data bersih yang konsisten

---

## Contoh Kasus Penggunaan
- Normalisasi nama pelanggan
- Standarisasi nilai transaksi
- Penyamaan format tanggal lintas sistem
- Cleaning dataset klien berulang dengan aturan tetap

---

## Kenapa Engine Ini Berbeda
- Tidak hard-coded
- Tidak tergantung dataset
- Tidak mengandalkan intuisi
- Siap dipakai ulang sebagai sistem

Engine ini cocok untuk:
- Data Cleaning Agency
- Data Extraction Pipeline
- Operasional & Finance Data Processing

---

## Status
 Stable  
 Reusable  
 Rule-Driven  

