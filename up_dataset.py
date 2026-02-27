import os
from dotenv import load_dotenv
from huggingface_hub import create_repo, snapshot_download, upload_folder

load_dotenv()

token = os.getenv("HF_TOKEN")

DEST_REPO_ID    = "aitfindonesia/KomdigiUB-RTDETR-R50-Dataset"
# DEST_REPO_ID    = "aitfindonesia/KomdigiUB-ViT-Dataset"
# DEST_REPO_ID    = "iqqy-x/rtdetr-gambling-dataset"
LOCAL_DIR       = "./v3-gambling-dataset"
# LOCAL_DIR       = "./v2-gambling-dataset-bersih"

print(f"Creating / verifying repo {DEST_REPO_ID} ...")
create_repo(
    repo_id=DEST_REPO_ID,
    repo_type="dataset",
    private=True,
    exist_ok=True,
    token=token,
)

print(f"Uploading {LOCAL_DIR} → {DEST_REPO_ID} ...")
upload_folder(
    repo_id=DEST_REPO_ID,
    repo_type="dataset",
    folder_path=LOCAL_DIR,
    commit_message=f"upload {DEST_REPO_ID} dataset",
    token=token,
)

print(f"Done: https://huggingface.co/{DEST_REPO_ID}")
