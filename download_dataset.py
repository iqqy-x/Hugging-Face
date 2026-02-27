import os
from dotenv import load_dotenv
from huggingface_hub import create_repo, snapshot_download, upload_folder

load_dotenv()

token = os.getenv("HF_TOKEN")

# SOURCE_REPO_ID  = "prd5/v2-gambling-dataset-bersih"
SOURCE_REPO_ID  = "prd5/v3-gambling-dataset"
# LOCAL_DIR       = "./v2-gambling-dataset-bersih"
LOCAL_DIR       = "./v3-gambling-dataset"

if not os.path.exists(LOCAL_DIR):
    print(f"Downloading {SOURCE_REPO_ID} → {LOCAL_DIR} ...")
    snapshot_download(
        repo_id=SOURCE_REPO_ID,
        repo_type="dataset",
        local_dir=LOCAL_DIR,
        token=token,
    )
    print("Download complete.")
else:
    print(f"Local directory '{LOCAL_DIR}' already exists, skipping download.")
