import random
from retry_policy import retry_with_backoff, RetryExceededError
from error_classifier import (
    NetworkError,
    DataFormatError
)
from failsafe_wrapper import failsafe_execute
from logger_setup import get_logger

logger = get_logger("engine16_runner")


# Simulasi task extraction
def fetch_data(job_id: int):
    rnd = random.random()

    if rnd < 0.3:
        raise NetworkError("Temporary network issue")
    elif rnd < 0.4:
        raise DataFormatError("Invalid data format")

    return {"job_id": job_id, "data": "OK"}


jobs = [{"job_id": i} for i in range(1, 11)]
results = []

for job in jobs:
    job_id = job["job_id"]

    def task(job_id=job_id):
        return retry_with_backoff(
            lambda: fetch_data(job_id),
            exceptions=(NetworkError,),
            max_attempts=3,
            base_delay=1
        )

    result = failsafe_execute(task, job_context=job)
    results.append(result)

logger.info(f"Final results: {results}")
print("DONE RUNNER")
