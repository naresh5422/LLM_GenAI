import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "LLM_GenAI_project"
app = 'app'
workers = 'workers'
eval = 'eval'
test = 'test'
scripts = 'scripts'
deploy = 'deploy'


list_of_files = [".github/workflows/.gitkeep",
                 f"src/{app}/__init__.py",
                 f"src/{app}/main.py",
                 f"src/{app}/config.py",
                 f"src/{app}/deps.py",
                 f"src/{app}/llm/__init__.py",
                 f"src/{app}/llm/provider.py",
                 f"src/{app}/llm/openai_provider.py",
                 f"src/{app}/rag/__init__.py",
                 f"src/{app}/rag/ingest.py",
                 f"src/{app}/rag/index.py",
                 f"src/{app}/rag/retrieve.py",
                 f"src/{app}/routers/__init__.py",
                 f"src/{app}/routers/health.py",
                 f"src/{app}/routers/chat.py",
                 f"src/{app}/routers/admit.py",
                 f"src/{app}/guards/__init__.py",
                 f"src/{app}/guards/filters.py",
                 f"src/{app}/guards/rate_limit.py",
                 f"src/{app}/telemetry/__init__.py",
                 f"src/{app}/telemetry/metrics.py",
                 f"src/{app}/telemetry/tracing.py",
                 f"src/{app}/utils/__init__.py",
                 f"src/{app}/utils/text.py",
                 f"src/{workers}/__init__.py",
                 f"src/{workers}/celery_worker.py",
                 f"src/{eval}/__init__.py",
                 f"src/{eval}/harness.py",
                 f"src/{eval}/datasets/",
                 f"{test}/__init__.py",
                 f"{test}/test_chat.py",
                 f"{test}/test_rag.py",
                 f"{scripts}/bootstrap_local.sh",
                 f"{scripts}/run_evals.sh",
                 f"{deploy}/ecs-task.json",
                 f"{deploy}/ecs-service.json",
                 f"{deploy}/terraform/",
                 "Dockerfile",
                 "docker-compose.yaml",
                 "pyproject.toml",
                 "Makefile",
                 ".env.example",
                 ".github/workflows/ci.yml"]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating Empty file: {filepath}")
    else:
        logging.info(f"{filename} is already existed")
