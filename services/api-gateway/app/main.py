# from fastapi import FastAPI
# import requests
# from common.failure import apply_failure

# app = FastAPI()

# AUTH_URL = "http://auth-service:8000/validate"

# @app.get("/login")
# def login():
#     apply_failure()
#     response = requests.get(AUTH_URL)
#     return {
#         "gateway": "ok",
#         "auth_response": response.json()
#     }


# PIPELINE_URL = "http://pipeline-service:8000/run-pipeline"

# @app.get("/login")
# def login():
#     apply_failure()
#     response = requests.get(PIPELINE_URL)
#     return {
#         "gateway": "ok",
#         "pipeline_response": response.json()
#     }

from fastapi import FastAPI
import requests
from common.failure import apply_failure
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI()

PIPELINE_URL = "http://pipeline-service:8000/run-pipeline"

REQUEST_COUNT = Counter("gateway_requests_total", "Total gateway requests")
REQUEST_LATENCY = Histogram("gateway_request_latency_seconds", "Gateway request latency")

@app.get("/login")
def login():
    apply_failure()
    REQUEST_COUNT.inc()
    with REQUEST_LATENCY.time():
        response = requests.get(PIPELINE_URL)
        return {
            "gateway": "ok",
            "pipeline_response": response.json()
        }

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
