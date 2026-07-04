FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends git curl ca-certificates && rm -rf /var/lib/apt/lists/*
COPY requirements.txt pyproject.toml /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY shared /app/shared
COPY services /app/services
COPY config /app/config
COPY domains /app/domains
CMD ["uvicorn", "services.hub.app:app", "--host", "0.0.0.0", "--port", "8080"]
