# NOTE — Engine 03 Duplicate & Near-Duplicate
Hari 1 — Struktur & Cara Berpikir

Hari ini aku BELUM menulis logic duplicate.

Fokus hari ini adalah:
- memahami masalah dunia nyata: data ganda & mirip
- menyusun struktur engine agar tidak chaos di tengah jalan

Aku menyadari:
- duplicate bukan cuma soal hapus baris
- tapi soal MENILAI tingkat kemiripan & risiko

File-file yang kubuat hari ini punya peran:
- loader.py → semua engine butuh data masuk yang konsisten
- exact_duplicate.py → baseline masalah paling dasar
- similarity.py → jembatan insting manusia ke angka
- near_duplicate.py → logika bisnis (bukan matematika murni)
- scorer.py → keputusan TIDAK hitam putih
- reporter.py → klien tidak baca dataframe
- runner.py → agar engine bisa dijalankan ulang

Hari ini engine belum pintar.
Tapi hari ini aku membuatnya SIAP tumbuh.

---

Hari 2 — Exact Duplicate Detection

Hari ini aku mengerjakan duplicate PALING DASAR:
baris yang sama persis.

Aku belajar bahwa:
- exact duplicate adalah bukti tercepat ke klien
- ini baseline sebelum bicara kemiripan

Aku sengaja:
- tidak langsung menghapus data
- hanya MEMBERI TANDA

Engine ini tidak mengambil keputusan.
Engine ini membuka mata.

---

Hari 3 — String Similarity Core

Hari ini aku membuat jembatan
antara insting manusia dan mesin.

Aku tidak menentukan:
"ini duplikat atau bukan"

Aku hanya menjawab:
"SEBERAPA MIRIP mereka?"

Aku belajar:
- similarity bukan kebenaran mutlak
- tapi bahan diskusi & keputusan

Engine ini mulai berpikir,
bukan sekadar menghitung.

---

Hari 4 — Near-Duplicate Logic

Hari ini aku membuat logic
yang paling sering diperdebatkan di dunia nyata.

Aku sadar:
- tidak ada threshold yang “benar”
- yang ada: threshold yang BISA DIJELASKAN

Engine ini tidak memaksa keputusan.
Engine ini menyiapkan bahan diskusi.

Near-duplicate adalah soal risiko,
bukan hitam-putih.

---

Hari 5 — Scoring & Decision Layer

Hari ini aku berhenti berpikir sebagai coder.
Aku mulai berpikir sebagai auditor data.

Aku sadar:
- klien tidak butuh similarity score
- klien butuh: MANA YANG BERISIKO

Scoring mengubah data mentah
menjadi bahasa keputusan.

Engine ini tidak memutuskan untuk manusia,
tapi membuat manusia percaya diri saat memutuskan.

---

Hari 6 — Report Generator

Hari ini engine ini resmi berbicara
dengan bahasa klien.

Aku sadar:
- data rusak itu teknis
- dampaknya itu bisnis

Report ini bukan hiasan.
Ini alat komunikasi & kepercayaan.

Tanpa report, engine ini hanya milikku.
Dengan report, engine ini milik klien.


---

## `note.md` — PENUTUP ENGINE (HARI 7)

Tambahkan di bawah Hari 6:

Hari 7 — Engine Final & Publish

Hari ini aku tidak menambah fitur.
Aku memastikan mesin ini:
- bisa dijalankan ulang
- bisa dipahami orang lain
- bisa dipertanggungjawabkan

Engine ini mengajarkanku:
- data cleaning adalah soal kepercayaan
- bukan soal menghapus baris

Engine ini mungkin sederhana,
tapi ini fondasi dari semua pipeline besar.

Aku tidak membuat script.
Aku membuat mesin.
