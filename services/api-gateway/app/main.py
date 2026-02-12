from fastapi import FastAPI
import requests
from common.failure import apply_failure

app = FastAPI()

# AUTH_URL = "http://auth-service:8000/validate"

# @app.get("/login")
# def login():
#     apply_failure()
#     response = requests.get(AUTH_URL)
#     return {
#         "gateway": "ok",
#         "auth_response": response.json()
#     }


PIPELINE_URL = "http://pipeline-service:8000/run-pipeline"

@app.get("/login")
def login():
    apply_failure()
    response = requests.get(PIPELINE_URL)
    return {
        "gateway": "ok",
        "pipeline_response": response.json()
    }