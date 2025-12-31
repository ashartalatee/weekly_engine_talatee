import json
from typing import Dict

def generate_report(summary: Dict, output_path: str) -> None:
    """
    Menyimpan laporan audit format data ke file JSON.
    """
    report = {
        "engine": "Format Anomaly Detecto",
        "status": "COMPLETED",
        "summary": summary
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)