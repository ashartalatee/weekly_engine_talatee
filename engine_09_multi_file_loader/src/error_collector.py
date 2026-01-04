from datetime import datetime


class ErrorCollector:
    def __init__(self):
        self.errors = []

    def add(
        self,
        file_name: str,
        file_path: str,
        stage: str,
        error_message: str
    ):
        error_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "file_name": file_name,
            "file_path": file_path,
            "stage": stage,
            "error_message": error_message
        }
        self.errors.append(error_record)

    def has_errors(self):
        return len(self.errors) > 0

    def summary(self):
        return {
            "total_errors": len(self.errors),
            "by_stage": self._group_by_stage()
        }

    def _group_by_stage(self):
        grouped = {}
        for e in self.errors:
            stage = e["stage"]
            grouped[stage] = grouped.get(stage, 0) + 1
        return grouped

    def to_list(self):
        return self.errors
