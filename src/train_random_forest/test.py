import wandb
import pandas as pd

# Start a run
run = wandb.init(project="nyc_airbnb", job_type="test_artifact_download")

# Download the artifact
artifact = run.use_artifact("cnob11-wgu/nyc_airbnb/clean_sample:latest", type="clean_sample")
artifact_path = artifact.file()

# Now read the CSV
df = pd.read_csv(artifact_path)

print(df.head())