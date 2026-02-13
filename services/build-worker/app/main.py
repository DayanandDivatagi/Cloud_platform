# from fastapi import FastAPI
# import time
# import math
# from common.failure import apply_failure

# app = FastAPI()

# def cpu_heavy_task(duration=5):
#     start = time.time()
#     while time.time() - start < duration:
#         for i in range(10000):
#             math.sqrt(i * 987654)

# @app.get("/build")
# def run_build():
#     apply_failure()
#     cpu_heavy_task()
#     return {"build": "completed"}

from fastapi import FastAPI
import time
import math
from common.failure import apply_failure
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI()

REQUEST_COUNT = Counter("worker_requests_total", "Total worker requests")
REQUEST_LATENCY = Histogram("worker_request_latency_seconds", "Worker request latency")

def cpu_heavy_task(duration=5):
    start = time.time()
    while time.time() - start < duration:
        for i in range(10000):
            math.sqrt(i * 987654)

@app.get("/build")
def run_build():
    apply_failure()
    REQUEST_COUNT.inc()
    with REQUEST_LATENCY.time():
        cpu_heavy_task()
    return {"build": "completed"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

