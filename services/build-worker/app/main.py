from fastapi import FastAPI
import time
import math
from common.failure import apply_failure

app = FastAPI()

def cpu_heavy_task(duration=5):
    start = time.time()
    while time.time() - start < duration:
        for i in range(10000):
            math.sqrt(i * 987654)

@app.get("/build")
def run_build():
    apply_failure()
    cpu_heavy_task()
    return {"build": "completed"}

