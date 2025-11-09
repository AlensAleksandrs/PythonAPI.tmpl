
# Python API Template (FastAPI + Celery + Redis + Docker + K8s)

[![license: LGPL v3.0 or later](https://img.shields.io/badge/License-LGPL%20v3.0%2B-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0.html)

A production-ready backend starter template for building scalable APIs and microservices using **FastAPI**, **Celery**, **Redis**, and **Docker**. It supports asynchronous task processing, pluggable file storage (local or S3), and includes **Kubernetes deployment manifests** for cloud-ready deployments.

---

### Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Development](#development)
- [Task Processing (Celery)](#task-processing-celery)
- [File Upload & Storage](#file-upload--storage)
- [Docker](#docker)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Environment Variables](#environment-variables)
- [Features](#features)
- [License](#license)

---

## Prerequisites

- Python 3.12+
- Docker & Docker Compose
- (Optional) Kubernetes Cluster + `kubectl`
- (Optional) S3-compatible storage (MinIO, AWS S3, etc.)

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd python-api-template
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
.env\Scriptsctivate   # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Development

Start the API locally:

```bash
uvicorn app.main:app --reload
```

> Your API will be available at `http://localhost:8000`

---

## Task Processing (Celery)

To start a Celery worker:

```bash
celery -A celery_worker.celery_app worker --loglevel=info
```

Test endpoint:

```
GET /add?a=2&b=3  → returns task_id  
GET /tasks/<task_id> → returns status & result
```

---

## File Upload & Storage

Upload a file:

```
POST /files/upload (form-data: file=@example.pdf)
```

Retrieve a file:

```
GET /files/example.pdf
```

Storage backends:
- `local` → saved in `storage/uploads/`
- `s3` → saved in configured bucket

---

## Docker

Build & run with Docker Compose:

```bash
docker-compose up --build
```

Services included:
- `api` - FastAPI application
- `worker` - Celery background worker
- `redis` - Message broker & result backend

---

## Kubernetes Deployment

Build and push Docker image:

```bash
docker build -t <docker-username>/python-api:latest .
docker push <docker-username>/python-api:latest
```

Apply manifests:

```bash
kubectl apply -f k8s/
```

This deploys:
- API Deployment + Service
- Celery Worker Deployment
- Redis Deployment + Service
- ConfigMap + Secret
- Optional Ingress

---

## Environment Variables

Example `.env`:

```
PROJECT_NAME=Python API Template
ENVIRONMENT=development
REDIS_URL=redis://redis:6379/0
STORAGE_BACKEND=local
LOCAL_STORAGE_PATH=storage/uploads

# For S3:
# S3_BUCKET_NAME=your-bucket
# S3_ACCESS_KEY=your-access-key
# S3_SECRET_KEY=your-secret
# S3_REGION=eu-central-1
# S3_ENDPOINT_URL=https://s3.amazonaws.com
```

---

## Features

✔ FastAPI for high-performance APIs  
✔ Celery for asynchronous background tasks  
✔ Redis as task broker/result backend  
✔ File storage (local or S3)  
✔ Docker Compose for local development  
✔ Kubernetes manifests for deployment  
✔ Clean and extensible project structure  

---

## License

This template is available under the **GPL-3.0 License**.

---

Developed by [Alens Aleksandrs Čerņa](https://www.alens.lv)
