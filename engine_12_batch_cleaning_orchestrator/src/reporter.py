import os
import json
from datetime import datetime

class Reporter:
    def __init__(self, tracker):
        self.tracker = tracker

        # BASE DIR = engine_12_batch_cleaning_orchestrator
        self.base_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")
        )

        self.report_dir = os.path.join(self.base_dir, "reports")
        os.makedirs(self.report_dir, exist_ok=True)

    def generate_report(self):
        report = {
            "timestamp": datetime.now().isoformat(),
            "total_jobs": len(self.tracker.states),
            "jobs_done": [
                name for name, state in self.tracker.states.items()
                if state == "done"
            ],
            "jobs_failed": [
                name for name, state in self.tracker.states.items()
                if state == "failed"
            ]
        }

        report_path = os.path.join(self.report_dir, "batch_summary.json")

        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)

        print(f"Report tersimpan: {report_path}")
        return report
