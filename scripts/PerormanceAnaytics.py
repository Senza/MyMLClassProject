import requests
import pandas as pd

BASE_URL = "http://localhost:4040/api/v1"

# Get App ID
apps = requests.get(f"{BASE_URL}/applications").json()
app_id = apps[0]['id']

# Fetch jobs
jobs = requests.get(f"{BASE_URL}/applications/{app_id}/jobs").json()
jobs_df = pd.json_normalize(jobs)

# Convert timestamps
jobs_df['submissionTime'] = pd.to_datetime(jobs_df['submissionTime'])
jobs_df['completionTime'] = pd.to_datetime(jobs_df['completionTime'])

# Calculate duration in seconds
jobs_df['jobDurationSeconds'] = (
    jobs_df['completionTime'] - jobs_df['submissionTime']
).dt.total_seconds()

# Optional: duration in minutes
jobs_df['jobDurationMinutes'] = jobs_df['jobDurationSeconds'] / 60

# Save for Tableau
jobs_df.to_csv("spark_jobs_with_duration.csv", index=False)

print("Job duration calculated successfully!")