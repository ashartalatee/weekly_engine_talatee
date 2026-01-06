# Engine 11 — Versioned Cleaning Engine

## Apa Ini?
Versioned Cleaning Engine adalah sistem untuk
mencatat, membandingkan, dan mempertanggungjawabkan
setiap perubahan data selama proses cleaning.

Engine ini dirancang untuk kebutuhan:
- Data Cleaning Agency
- Audit data
- Revisi data klien yang berulang

## Masalah yang Diselesaikan
- Klien tidak tahu apa yang berubah pada data mereka
- Data lama tertimpa tanpa histori
- Sulit menjelaskan dampak cleaning

## Solusi
Engine ini:
- menyimpan snapshot setiap versi data
- memberi ID versi otomatis
- membandingkan kualitas data antar versi
- menghasilkan laporan siap kirim ke klien

## Komponen Utama
- Data Snapshot Engine
- Version Tracker
- Diff Engine
- Metadata & Logging
- Client Diagnostic Report

## Output
- JSON snapshot & diff
- Audit log
- Laporan non-teknis untuk klien

## Cocok Untuk
- Data Cleaning Agency
- Data Extraction Agency
- Workflow ETL skala kecil–menengah

> Prinsip utama:
> "Kami tidak hanya membersihkan data,
> kami mencatat dan mempertanggungjawabkan setiap perubahan."
