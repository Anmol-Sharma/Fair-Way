from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import json
from typing import Optional
from pydantic import model_validator


class EnvSettings(BaseSettings):
    service: str
    ollama_url: Optional[str] = None
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
    zenodo_access_token: Optional[str] = None

    # feedback db
    feedback_db_path: str

    # Keys
    openai_key: Optional[str] = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @model_validator(mode="after")
    def check_conditional_requirements(self):
        # Example: If llm_model is 'gpt-4' or starts with 'gpt', openai_key must be provided
        if self.service.lower() == "ollama":
            if not self.ollama_url:
                raise ValueError(
                    "You selected ollama as the llm service. Provide its end point URL"
                )
        elif self.service.lower() == "openai":
            if not self.openai_key:
                raise ValueError(
                    "You selected openai as the llm service. Provide its API Key"
                )
        else:
            raise ValueError(
                "Only OLLAMA and OPENAI as LLM service providers supported"
            )
        return self


@lru_cache
def get_env_settings():
    return EnvSettings()


@lru_cache
def get_global_settings():
    with open("../configs/global_config.json") as f:
        settings = json.load(f)
        return settings
