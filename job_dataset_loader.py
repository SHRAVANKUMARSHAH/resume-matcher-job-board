import os
import csv

def load_jobs(file_path="jobs.csv"):
    jobs = []
    # ✅ Make path absolute: from current script's folder
    abs_path = os.path.join(os.path.dirname(__file__), file_path)

    try:
        with open(abs_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                job = {
                    "job_id": int(row["job_id"]),
                    "title": row["title"].strip(),
                    "description": row["description"].lower().strip()
                }
                jobs.append(job)
    except FileNotFoundError:
        print(f"❌ File not found: {abs_path}")
    except Exception as e:
        print("❌ Error reading jobs.csv:", e)

    print(f"✅ Total jobs loaded: {len(jobs)}")
    return jobs
