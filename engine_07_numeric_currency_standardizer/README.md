# Engine 07 — Numeric & Currency Standardizer

## Masalah Dunia Nyata
Angka dalam data bisnis sering terlihat rapi,
namun secara sistem tidak konsisten:
- Locale berbeda
- Currency bercampur
- Multiplier (K/M/B)
- Accounting negative
- Missing & ambiguous values

Kesalahan kecil di angka → keputusan bisnis salah.

---

## Solusi
Engine ini menormalkan angka & currency secara sadar:
- Deteksi format
- Normalisasi numeric
- Pisahkan currency
- Validasi kualitas data
- Batch processing + report

Engine **lebih memilih menolak data**
daripada menghasilkan angka menipu.

---

## Fitur Utama
- Locale-aware numeric normalization
- Currency separation (config-driven)
- Multiplier parsing (K / M / B)
- Validation & quality gate
- Batch CSV processing
- JSON report untuk audit

---

## Contoh Penggunaan

```python
from src.runner import run

run(
  input_csv="data/sample_dirty.csv",
  output_csv="data/sample_clean.csv",
  report_path="reports/standardization_report.json"
)
