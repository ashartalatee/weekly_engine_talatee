from job_loader import JobLoader
from state_tracker import StateTracker
from logger import log_info, log_error
from reporter import Reporter
import time
from csv_cleaner import clean_csv_folder


class Orchestrator:
    def __init__(self):
        self.loader = JobLoader()
        self.jobs = self.loader.load_jobs()
        self.tracker = StateTracker()

    def run_job(self, job):
        job_name = job["name"]
        max_retry = job.get("retry", 1)
        attempt = 0

        while attempt <= max_retry:
            try:
                self.tracker.set_status(job_name, "running")
                log_info(f"Menjalankan job: {job_name} (attempt {attempt+1})")

                clean_csv_folder(
                    job["input_path"],
                    job["output_path"]
                )

                self.tracker.set_status(job_name, "done")
                log_info(f"Job selesai: {job_name}")
                return

            except Exception as e:
                attempt += 1
                log_error(f"Job gagal: {job_name} | {e}")

                if attempt > max_retry:
                    self.tracker.set_status(job_name, "failed")
                    log_error(f"Job {job_name} gagal setelah retry")


    def run(self):
        for job in self.jobs:
            self.run_job(job)

        log_info("Batch selesai")
        reporter = Reporter(self.tracker)
        summary = reporter.generate_report()
        print("Summary:", summary)

if __name__ == "__main__":
    orch = Orchestrator()
    orch.run()
