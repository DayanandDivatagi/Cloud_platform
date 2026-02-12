FROM python:3.10-slim

WORKDIR /app

# Copy requirements from service folder
COPY services/auth-service/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy service code
COPY services/auth-service/app ./app

# Copy shared common module
COPY common ./common

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
