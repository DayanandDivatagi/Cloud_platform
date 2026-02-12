from fastapi import FastAPI
from common.failure import apply_failure

app = FastAPI()

@app.get("/validate")
def validate():
    apply_failure()
    return {"status": "valid"}
