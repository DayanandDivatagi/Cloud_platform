from fastapi import FastAPI
import requests
from common.failure import apply_failure

app = FastAPI()

WORKER_URL = "http://build-worker:8000/build"

@app.get("/run-pipeline")
def run_pipeline():
    apply_failure()
    response = requests.get(WORKER_URL)
    return {
        "pipeline": "executed",
        "worker_response": response.json()
    }

