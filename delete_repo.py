import os
from dotenv import load_dotenv
from huggingface_hub import delete_repo

load_dotenv()

token = os.environ["HF_TOKEN"]

delete_repo(
    repo_id="iqqy/vit-gambling-finetune",
    repo_type="model",
    token=token
)
