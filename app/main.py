from fastapi import FastAPI
from app.core.config import settings
import redis

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