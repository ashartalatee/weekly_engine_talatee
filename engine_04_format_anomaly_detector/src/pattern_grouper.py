from typing import Dict

def group_anomaly_patterns(reports: Dict) -> Dict:
    """
    Menggabungkan temuan dari berbagai detektor
    menjadi satu ringkasan pola kerusakan.
    """
    summary = {}

    for field, report in reports.items():
        summary[field] = {
            "total": report.get("total_values", 0),
            "patterns": report.get("pattern_distribution", {})
        }

    return summary