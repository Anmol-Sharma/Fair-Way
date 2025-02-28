from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import json


class EnvSettings(BaseSettings):
    ollama_url: str
    role_user: str
    role_model: str

    # Have to moved to the global config
    llm_model: str
    temperature: float
    num_cts: int

    # Celery Configuration
    broker_url: str
    result_backend: str
    worker_concurrency: int
    worker_prefetch_multiplier: int
    timezone: str
    enable_utc: bool
    task_track_started: bool
    task_rate_limit_add: str
    broker_connection_retry_on_startup: bool
    result_expires: int
    task_acks_late: bool
    task_reject_on_worker_lost: bool
    task_time_limit: int
    worker_max_memory_per_child: int

    # access endpoint
    base_doi_resolver: str
    base_zenodo_resolver: str
    base_dryad_resolver: str
    base_hugging_face_resolver: str

    # Acess tokens
    zenodo_access_token: str

    # feedback db
    feedback_db_path: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_env_settings():
    return EnvSettings()


@lru_cache
def get_global_settings():
    with open("../configs/global_config.json") as f:
        settings = json.load(f)
        return settings
