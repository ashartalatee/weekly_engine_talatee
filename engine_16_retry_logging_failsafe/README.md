# Engine 16 — Retry, Logging & Fail-Safe

Engine ini adalah fondasi stabilitas untuk semua
data extraction & batch processing system.

## Masalah Dunia Nyata
- Job mati total karena 1 error
- Tidak ada log yang bisa diaudit
- Tidak tahu data mana yang gagal

## Solusi
Engine ini menyediakan:
- Retry terkontrol dengan backoff
- Error classification (retryable vs fatal)
- Logging terstruktur (JSON)
- Fail-safe execution (job lanjut walau sebagian gagal)

## Komponen Utama
- `retry_policy.py` — retry & backoff
- `error_classifier.py` — klasifikasi error
- `logger_setup.py` — logger terpusat
- `failsafe_wrapper.py` — fail-safe execution

## Contoh Penggunaan

```python
result = failsafe_execute(
    task_function,
    job_context={"job_id": 1}
)
