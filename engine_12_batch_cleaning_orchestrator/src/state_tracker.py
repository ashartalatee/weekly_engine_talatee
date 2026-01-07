class StateTracker:
    def __init__(self):
        self.job_status = {}  # job_name: status

    def set_status(self, job_name, status):
        self.job_status[job_name] = status

    def get_status(self, job_name):
        return self.job_status.get(job_name, "pending")

    def summary(self):
        return self.job_status

class StateTracker:
    def __init__(self):
        self.states = {}

    def set_status(self, job_name, status):
        self.states[job_name] = status

    def summary(self):
        return self.states

