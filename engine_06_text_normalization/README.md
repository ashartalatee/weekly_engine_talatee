# Engine 06 — Text Normalization Engine

Engine ini berfungsi untuk menstandarkan data text yang tidak konsisten
seperti nama, alamat, kategori, dan teks bebas yang berasal dari berbagai sumber.

## Masalah Dunia Nyata
- Nama pelanggan ditulis berbeda-beda
- Kategori produk tidak konsisten
- Alamat penuh singkatan & typo
- Text tidak bisa dipakai untuk join, grouping, atau analisis

## Tujuan Engine
- Membuat text konsisten dan dapat dipakai ulang
- Menggunakan rule-based normalization (bukan hardcode)
- Bisa dikonfigurasi per klien

## Output
- Data text yang sudah dinormalisasi
- Ringkasan perubahan (before–after)
# Engine 06 — Text Normalization Engine

Engine ini menstandarkan data text yang tidak konsisten
(nama, kategori, alamat) agar siap dipakai untuk analisis,
operasional, dan sistem bisnis.

Engine ini dibuat sebagai bagian dari **Talatee Data Engine Suite**.

---

## 🎯 Masalah Dunia Nyata

Di data klien, text sering rusak karena:
- Input manual
- Sistem berbeda
- Tidak ada standar penulisan

Akibatnya:
- Join data gagal
- Kategori tidak konsisten
- Analisis & reporting salah

---

## 🧠 Solusi Engine Ini

Engine ini:
- Menggunakan **rule-based normalization**
- Tidak hardcode logic
- Bisa dikonfigurasi per klien via YAML
- Aman (tidak agresif, tidak sok pintar)

---

## ⚙️ Fitur Utama

- General text normalization (spasi, casing)
- Name normalization (typo ringan, simbol, title case)
- Category normalization (mapping konsisten)
- Address normalization (singkatan & format dasar)
- Output report perubahan data

---


---

## ▶️ Cara Menjalankan

```bash
python src/runner.py
