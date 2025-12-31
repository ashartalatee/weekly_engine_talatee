# Engine 03 — Duplicate & Near-Duplicate Detection

Engine ini digunakan untuk mendeteksi:
- Exact duplicate (baris sama persis)
- Near-duplicate (data mirip tapi tidak identik)

Tujuan utama engine ini:
- Mengungkap kerusakan data yang sering tidak disadari klien
- Memberi dasar keputusan berbasis skor, bukan asumsi

Engine ini adalah bagian dari Talatee Data Engine Suite.

# Engine 03 — Duplicate & Near-Duplicate Detection

Engine ini mendeteksi:
- Exact duplicate (baris identik)
- Near-duplicate (data mirip dengan typo / variasi penulisan)

## Masalah Dunia Nyata
Banyak organisasi tidak sadar bahwa:
- data mereka berisi duplikat
- duplikat tidak selalu identik
- laporan & keputusan jadi bias

Engine ini membantu mengungkap masalah tersebut
secara terukur dan dapat dijelaskan.

## Fitur Utama
- Exact duplicate detection
- String similarity scoring (RapidFuzz)
- Near-duplicate pairing dengan threshold
- Risk labeling (safe / medium / high / exact)
- JSON audit report siap kirim ke klien

## Cara Menjalankan

```bash
python src/runner.py
