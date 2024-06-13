import os
import subprocess
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to download a model using huggingface-cli
def download_model(model_name, base_dir):
    model_dir = os.path.join(base_dir, model_name)
    print(f"Downloading model: {model_name} to {model_dir}")
    subprocess.run([
        "huggingface-cli", "download", model_name, "--local-dir", model_dir
    ], check=True)

# List of models to download from environment variable
models = os.getenv("MODEL_NAMES").split(',')

# Base directory to save the models
base_model_dir = os.getenv("BASE_MODEL_DIR")

# Download each model into its respective directory under the base model directory
for model in models:
    download_model(model, base_model_dir)

print("All models downloaded.")
