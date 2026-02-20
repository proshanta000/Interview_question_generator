import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Using a consistent package name
project_name = "Interview_question_generator"

list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    "artifacts/.gitkeep",
    "vectorstore/.gitkeep",
    
    # Main package structure
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",
    
    # Components
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_config.py", # Centralized LLM/Embeddings
    
    # Pipelines
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/generation_pipeline.py",
    f"src/{project_name}/pipelines/rag_pipeline.py",
    
    # Utils (common.py removed, prompts.py added)
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/prompts.py",
    
    # Web UI files (templates and static)
    "templates/index.html",
    "templates/result.html",
    "static/style.css",
    "static/js/main.js",
    
    # Root level files
    "app.py",
    "requirements.txt",
    "setup.py",
    ".env",
    "README.md",
    "research/trials.ipynb" # Good to have a place for your notebook experiments
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")