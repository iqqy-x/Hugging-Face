import os
from dotenv import load_dotenv
from huggingface_hub import create_repo, upload_folder

load_dotenv()

token = os.getenv("HF_TOKEN")

REPO_ID = "iqqy/vit-gambling-finetune"
LOCAL_MODEL_DIR = "./v2-vit-gambling-finetune"

create_repo(
    repo_id=REPO_ID,
    repo_type="model",
    private=False,
    exist_ok=True,
    token=token
)

upload_folder(
    repo_id=REPO_ID,
    repo_type="model",
    folder_path=LOCAL_MODEL_DIR,
    commit_message="upload ViT gambling fine-tuned model",
    token=token
)

print(f"Done: https://huggingface.co/{REPO_ID}")
