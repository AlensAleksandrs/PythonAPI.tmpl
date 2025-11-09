import os
from abc import ABC, abstractmethod
from botocore.client import Config
import boto3
from app.core.config import settings

class StorageBackend(ABC):
    @abstractmethod
    def save_file(self, file_path: str, file_data: bytes) -> str:
        pass

    @abstractmethod
    def get_file(self, file_path: str) -> bytes:
        pass

class LocalStorage(StorageBackend):
    def __init__(self, base_path: str):
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)

    def save_file(self, file_path: str, file_data: bytes) -> str:
        full_path = os.path.join(self.base_path, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "wb") as f:
            f.write(file_data)
        return full_path

    def get_file(self, file_path: str) -> bytes:
        full_path = os.path.join(self.base_path, file_path)
        with open(full_path, "rb") as f:
            return f.read()

class S3Storage(StorageBackend):
    def __init__(self):
        self.s3 = boto3.client(
            "s3",
            endpoint_url=settings.S3_ENDPOINT_URL,
            aws_access_key_id=settings.S3_ACCESS_KEY,
            aws_secret_access_key=settings.S3_SECRET_KEY,
            region_name=settings.S3_REGION,
            config=Config(signature_version="s3v4")
        )
        self.bucket = settings.S3_BUCKET_NAME

    def save_file(self, file_path: str, file_data: bytes) -> str:
        self.s3.put_object(Bucket=self.bucket, Key=file_path, Body=file_data)
        return file_path

    def get_file(self, file_path: str) -> bytes:
        obj = self.s3.get_object(Bucket=self.bucket, Key=file_path)
        return obj["Body"].read()

def get_storage_backend() -> StorageBackend:
    if settings.STORAGE_BACKEND == "local":
        return LocalStorage(settings.LOCAL_STORAGE_PATH)
    elif settings.STORAGE_BACKEND == "s3":
        return S3Storage()
    else:
        raise ValueError("Unsupported storage backend")