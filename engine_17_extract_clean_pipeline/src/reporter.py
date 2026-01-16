import json
from pathlib import Path
from datetime import datetime, timezone
datetime.now(timezone.utc).isoformat()



class PipelineReporter:
    def __init__(self, report_dir="reports"):
        self.report_dir = Path(report_dir)
        self.report_dir.mkdir(parents=True, exist_ok=True)

    def generate(self, pipeline_result):
        report = {
            "status": pipeline_result.status,
            "detail": pipeline_result.detail,
            "generated_at": datetime.utcnow().isoformat()
        }

        report_path = self.report_dir / "run_report.json"
        with open(report_path, "w") as f:
            json.dump(report, f, indent=2)

        return report_path
