from celery.result import AsyncResult
from fastapi import FastAPI, HTTPException
from app.core.config import settings
import redis

from celery_worker import add, celery_app

app = FastAPI(title=settings.PROJECT_NAME)

redis_client = redis.Redis.from_url(settings.REDIS_URL)

@app.get("/health")
def health_check():
    redis_ok = True
    try:
        redis_client.ping()
    except:
        redis_ok = False

    return {
        "status": "ok",
        "environment": settings.ENVIRONMENT,
        "redis": redis_ok
    }

@app.get("/add")
def run_add(a: int = 1, b: int = 2):
    task = add.delay(a, b)
    return {"task_id": task.id, "message": "Task submitted"}

@app.get("/tasks/{task_id}")
def get_task_status(task_id: str):
    task = AsyncResult(task_id, app=celery_app)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    response = {
        "task_id": task.id,
        "status": task.status,
    }

    if task.successful():
        response["result"] = task.result
    elif task.failed():
        response["error"] = str(task.result)

    return response