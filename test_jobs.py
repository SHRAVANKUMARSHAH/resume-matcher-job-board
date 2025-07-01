# test_jobs.py
from job_dataset_loader import load_jobs

jobs = load_jobs()
print(f"✅ Total Jobs Loaded: {len(jobs)}")
for job in jobs:
    print(job)
