# Engine 04 — Format Anomaly Detector

## Masalah Dunia Nyata
Dalam banyak kasus, klien tidak sadar bahwa data mereka rusak bukan karena nilainya,
tetapi karena **format yang tidak konsisten**.

Contoh nyata:
- Tanggal: `2023-01-02`, `02/01/23`, `Jan 2 2023`
- Angka: `1.000`, `1,000`, `1000`, `Rp 1.000`
- Teks: `Jakarta`, `jakarta`, `JAKARTA`, `Jakarta.`

Masalah ini:
- Tidak langsung error
- Tapi merusak analisis, reporting, dan sistem downstream

---

## Tujuan Engine
Engine ini bertugas untuk:
1. Mendeteksi anomali format pada data
2. Mengelompokkan pola kerusakan format
3. Menghasilkan laporan yang bisa dipahami klien non-teknis

Engine ini **tidak melakukan cleaning**.
Engine ini adalah **alat audit & diagnosis format data**.

---

## Output Utama
- Laporan JSON berisi:
  - Jenis kolom
  - Pola format yang ditemukan
  - Contoh data bermasalah
  - Tingkat risiko

---

## Filosofi
> “Jika kamu tidak bisa menjelaskan di mana data rusak,
> kamu tidak pantas membersihkannya.”

Engine ini melatih insting berpikir seperti **Data Auditor**, bukan sekadar programmer.

---

## Cara Menjalankan Engine

```bash
cd engine_04_format_anomaly_detector/src
python runner.py
