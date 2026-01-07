# Engine 12 — Daily Note

## Day 1 — Memahami Masalah Batch Cleaning

### Apa masalah utamanya?
Batch cleaning bukan soal membersihkan data,
tapi soal mengelola kegagalan dalam jumlah besar.

### Hal yang sering bikin batch gagal di dunia nyata
- Satu file rusak menghentikan semuanya
- Tidak tahu file mana yang gagal
- Tidak ada ringkasan untuk klien
- Semua error terlihat sama (padahal tidak)

### Insight hari ini
Batch engine = sistem pengendali stres.
Bukan soal cepat, tapi soal tetap jalan walau ada yang rusak.

### Pertanyaan untuk hari berikutnya
- Informasi apa yang wajib diketahui sebelum batch jalan?
- Apa yang harus ditolak sejak awal?

## Day 2 — Desain Batch Config

### Insight utama hari ini
Batch engine yang baik dikontrol oleh config,
bukan oleh kondisi if di dalam kode.

### Kenapa job harus eksplisit?
Karena di dunia nyata:
- file bisa sama
- tapi perlakuan bisa beda
- tanggung jawab harus jelas

### Kesalahan yang ingin kuhindari
- Config terlalu fleksibel tapi tidak jelas
- Menyembunyikan logika bisnis di kode

### Pertanyaan untuk Day 3
- Informasi apa yang HARUS ada sebelum job dijalankan?
- Error apa yang harus ditolak sejak awal?

# DAY 3 — Job Loader & Validator

## Insight
- Validator penting untuk batch aman sebelum dijalankan.
- Loader memisahkan **logika eksekusi** dan **definisi job**.
- Batch bisa dipakai ulang cukup dengan edit config.

## Risiko
- Tanpa loader → error muncul saat batch running.
- Hardcode path → batch tidak fleksibel.
- Tidak ada validasi engine → bisa crash di runtime.

## Action Besok
- Buat **Orchestrator Core (`orchestrator.py`)**
- Gunakan jobs dari loader untuk dijalankan berurutan.

# DAY 4 — Orchestrator Core

## Insight
- Orchestrator mengubah batch dari sekadar loop menjadi **engine yang bisa di-track**.
- Status tiap job penting untuk debugging & retry.
- Urutan job = workflow nyata dunia agency.
- Batch mulai terlihat hidup, bisa di-observe & report.

## Risiko
- Tidak track status → gagal tidak ketahuan.
- Jalur job tidak berurutan → data kacau.
- Hardcode job → tidak reusable.

## Action Besok
- Tambahkan **Retry, Fail-Safe & Logging**
- Job yang gagal tidak menghentikan batch.
- Logging lebih lengkap per job.

# DAY 5 — Retry, Fail-Safe & Logging

## Insight
- Retry otomatis mengurangi risiko gagal sementara (misal network/API timeout).
- Fail-safe membuat batch tetap berjalan meski ada job gagal.
- Logging penting untuk audit & debugging.
- Dengan setup ini, batch bisa **dipakai di dunia nyata tanpa pengawasan terus-menerus**.

## Risiko
- Tanpa retry → batch mudah gagal karena masalah sementara.
- Tanpa fail-safe → batch berhenti & menunda deliverable.
- Logging minimal → sulit tracking kesalahan.

## Action Besok
- Buat **Report & Summary**
- Batch harus bisa menghasilkan ringkasan job sukses/gagal.
- Klien tidak perlu baca log teknis.

# DAY 6 — Report & Summary

## Insight
- Klien ingin **ringkasan**, bukan log teknis.
- JSON report memudahkan integrasi ke dashboard atau laporan PDF.
- Memisahkan eksekusi & reporting membuat engine **modular & profesional**.
- Sekarang batch siap dijalankan tanpa pengawasan terus-menerus.

## Risiko
- Tanpa report → klien tidak bisa menilai hasil batch.
- Report terlalu teknis → membingungkan klien.
- Tidak modular → sulit integrasi ke pipeline lain.

## Action Besok
- Polishing & GitHub ready
- Pastikan README, folder, dan note.md lengkap
- Buat test minimal untuk batch

# DAY 7 — Polishing & GitHub Ready

## Insight
- Setelah 7 hari, engine berjalan **end-to-end**:
  - Loader
  - Orchestrator core
  - Retry & fail-safe
  - Logging
  - Report summary
- Batch sekarang **reusable & modular**
- Engine siap untuk dipakai agency atau klien

## Risiko
- Update config harus valid
- Tambahan job baru harus di-test
- Logging & report harus selalu dicek

## Tips Pemeliharaan
- Update VALID_ENGINES saat engine baru ditambahkan
- Backup logs & reports secara periodik
- Review note.md setiap perubahan besar
