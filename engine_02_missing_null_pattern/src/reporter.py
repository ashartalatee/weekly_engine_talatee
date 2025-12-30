from datetime import datetime
from pathlib import Path


def generate_markdown_report(
    dataset_name: str,
    missing_summary: dict,
    pattern_analysis: dict,
    output_dir: str = "reports"
) -> str:
    """
    Generate human-readable markdown report for missing & null patterns.
    """
    Path(output_dir).mkdir(exist_ok=True)

    report_path = Path(output_dir) / "null_pattern.md"
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# Missing & Null Pattern Report\n\n")
        f.write(f"**Dataset:** {dataset_name}\n\n")
        f.write(f"**Generated at:** {now}\n\n")
        f.write("---\n\n")

        # Ringkasan umum
        f.write("## 1. Ringkasan Umum\n\n")
        f.write(f"- Total baris data: **{missing_summary['total_rows']}**\n")
        f.write(f"- Total kolom data: **{missing_summary['total_columns']}**\n\n")

        # Missing per kolom
        f.write("## 2. Missing per Kolom\n\n")
        for col, count in missing_summary["missing_by_column"].items():
            f.write(f"- **{col}**: {count} nilai kosong\n")
        f.write("\n")

        # Pola missing dominan
        f.write("## 3. Pola Missing Dominan\n\n")
        if pattern_analysis["top_missing_patterns"]:
            for pattern in pattern_analysis["top_missing_patterns"]:
                cols = ", ".join(pattern["missing_columns"])
                f.write(
                    f"- Kombinasi kolom kosong (**{cols}**) "
                    f"muncul sebanyak **{pattern['count']} kali**\n"
                )
        else:
            f.write("Tidak ditemukan pola missing yang signifikan.\n")
        f.write("\n")

        # Kolom paling bermasalah
        f.write("## 4. Kolom Paling Bermasalah\n\n")
        for col in pattern_analysis["most_problematic_columns"]:
            f.write(
                f"- **{col['column']}** terlibat dalam "
                f"{col['missing_occurrences']} kasus missing\n"
            )
        f.write("\n")

        # Catatan bisnis
        f.write("## 5. Catatan Bisnis\n\n")
        f.write(
            "- Missing yang berpola menandakan potensi masalah proses input data.\n"
            "- Kolom yang sering kosong perlu ditinjau di sumber pengumpulan data.\n"
            "- Disarankan dilakukan investigasi sebelum data digunakan untuk analisis lanjutan.\n"
        )

    return str(report_path)
