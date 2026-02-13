from fastapi import FastAPI, HTTPException
import requests
from common.failure import apply_failure
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI()

WORKER_URL = "http://build-worker:8000/build"

REQUEST_COUNT = Counter("pipeline_requests_total", "Total pipeline requests")
REQUEST_LATENCY = Histogram("pipeline_request_latency_seconds", "Pipeline request latency")

@app.get("/run-pipeline")
def run_pipeline():
    apply_failure()
    REQUEST_COUNT.inc()
    try:
        with REQUEST_LATENCY.time():
            response = requests.get(WORKER_URL, timeout=5)
            response.raise_for_status()
            return {
                "pipeline": "executed",
                "worker_response": response.json()
            }
    except Exception:
        raise HTTPException(status_code=500, detail="Worker failure")

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
