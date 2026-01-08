import json
import os
from typing import Callable, Any, Dict
from logger_setup import get_logger

logger = get_logger("failsafe")


FAILED_JOBS_FILE = "logs/failed_jobs.json"


def save_failed_job(job_info: Dict[str, Any]):
    os.makedirs("logs", exist_ok=True)

    if os.path.exists(FAILED_JOBS_FILE):
        with open(FAILED_JOBS_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(job_info)

    with open(FAILED_JOBS_FILE, "w") as f:
        json.dump(data, f, indent=2)


def failsafe_execute(
    func: Callable,
    job_context: Dict[str, Any],
    *args,
    **kwargs
):
    try:
        logger.info(f"Executing job: {job_context}")
        return func(*args, **kwargs)

    except Exception as e:
        logger.error(
            f"Job failed safely: {str(e)} | Context: {job_context}"
        )

        save_failed_job(
            {
                "job": job_context,
                "error": str(e),
                "function": func.__name__,
            }
        )

        return None  # fail-safe: tidak lempar error
