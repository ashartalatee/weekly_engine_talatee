# Missing & Null Pattern Engine

## Masalah Dunia Nyata
Banyak organisasi tidak sadar bahwa data mereka rusak
karena nilai kosong tersebar tidak merata dan berpola.

Akibatnya:
- Analisis bias
- Laporan menyesatkan
- Keputusan salah

## Solusi
Engine ini menganalisis missing & null values
untuk menemukan:
- Lokasi kerusakan data
- Pola kerusakan
- Risiko bisnis tersembunyi

## Fokus Engine
- Deteksi missing berbasis rule
- Analisis pola missing
- Laporan siap dibaca klien

> Engine ini tidak membersihkan data.  
> Engine ini memberi kesadaran.


# Missing & Null Pattern Engine

Engine ini membantu mengungkap kerusakan data tersembunyi
yang sering tidak disadari oleh tim bisnis maupun teknis.

Bukan untuk membersihkan data,
melainkan untuk memahami *di mana* dan *kenapa* data rusak.

---

## Masalah Dunia Nyata

Banyak organisasi:
- Tidak sadar kolom penting sering kosong
- Mengira missing terjadi acak
- Mengambil keputusan dari data yang bias

Akibatnya:
- Laporan menyesatkan
- Insight salah arah
- Risiko bisnis meningkat

---

## Solusi yang Ditawarkan

Engine ini:
- Mendeteksi missing & null values berbasis rule
- Mengungkap pola missing yang berulang
- Menghasilkan laporan non-teknis siap dibaca klien

---

## Output Utama

- Missing per kolom
- Pola missing dominan (missing bersamaan)
- Kolom paling bermasalah
- Laporan Markdown siap kirim

Contoh output:


---

## Cara Menjalankan

Dari folder engine:

```bash
python -m src.runner
engine_02_missing_null_pattern/
├── config/        # Definisi missing berbasis rule
├── data/          # Contoh data rusak
├── reports/       # Laporan hasil analisis
├── src/           # Inti engine
├── tests/         # Pengujian dasar
├── note.md        # Catatan pemahaman internal
└── README.md


---

## POSISI ENGINE 02 DI TALATEE ECOSYSTEM

 Engine 02 berfungsi sebagai:
- **Sensor kerusakan data**
- **Bahan komunikasi awal ke klien**
- **Gerbang sebelum cleaning & transformasi**

 Di proposal agency, engine ini bisa kamu sebut:
> *“Data Health & Missing Pattern Diagnostic”*

---

## UPDATE FINAL `note.md` — HARI 7

Tambahkan bagian penutup:

```md
---

## Hari 7 — Engine Ini Selesai

Engine ini mengajarkan saya satu hal penting:
Data yang rusak jarang berteriak.
Ia hanya diam.

Dengan engine ini,
saya bisa menunjukkan kerusakan data
tanpa asumsi,
tanpa debat,
tanpa opini.

Ini bukan latihan.
Ini aset.
