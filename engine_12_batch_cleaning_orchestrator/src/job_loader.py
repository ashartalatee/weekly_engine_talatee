import os
import yaml

class JobLoader:
    def __init__(self):
        # BASE DIR = engine_12_batch_cleaning_orchestrator
        self.base_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")
        )

        self.config_path = os.path.join(
            self.base_dir, "config", "batch_jobs.yaml"
        )

        print(f"Menggunakan config path: {self.config_path}")

    def load_jobs(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config tidak ditemukan: {self.config_path}")

        with open(self.config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        jobs = config.get("jobs", [])

        for job in jobs:
            job["input_path"] = os.path.normpath(
                os.path.join(self.base_dir, job["input_path"])
            )
            job["output_path"] = os.path.normpath(
                os.path.join(self.base_dir, job["output_path"])
            )

            if not os.path.exists(job["input_path"]):
                raise FileNotFoundError(
                    f"Input path tidak ada: {job['input_path']}"
                )

            os.makedirs(job["output_path"], exist_ok=True)

        return jobs
