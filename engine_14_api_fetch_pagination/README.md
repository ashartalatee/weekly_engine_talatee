# Engine 14 — API Fetch & Pagination Engine

Engine ini bertujuan mengambil data dari API
dengan dukungan pagination, retry, dan logging
yang stabil untuk kebutuhan data agency.

## Fokus Masalah
- Pagination API
- Error handling
- Reusability lintas klien

## Struktur Singkat
- config/ → aturan API & pagination
- src/ → logic engine
- examples/ → contoh penggunaan

# Engine 14 — API Fetch & Pagination Engine

Engine ini dirancang untuk mengambil data dari API secara stabil,
lengkap, dan dapat diulang, dengan fokus pada pagination,
retry, dan konfigurasi fleksibel.

Engine ini dibangun sebagai bagian dari **Talatee Data Engine Suite**
untuk kebutuhan data extraction agency.

---

## Masalah Dunia Nyata yang Diselesaikan
- Data API hanya terambil sebagian tanpa disadari
- Pagination berbeda di tiap API
- Script mati saat API error / rate limit
- Sulit dipakai ulang untuk klien berbeda

---

## Prinsip Desain
- **Config > Code**
- Pagination adalah inti, bukan detail
- Retry & logging adalah kewajiban
- Setiap komponen berdiri sendiri

---

---

## Cara Menjalankan (Contoh)
```bash
python -m examples.public_api_case

