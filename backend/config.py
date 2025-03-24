"""
    Config to load env variables defined in the environment file as well as define config for logging.
"""

import os
import logging.config
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
    top_p: float
    num_cts: Optional[int] = None
    keep_alive: Optional[str] = None

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
            if not self.num_cts:
                raise ValueError(
                    "Define the context window size to use for ollama models"
                )
            if not self.keep_alive:
                raise ValueError("Set the keep alive parameter for ollama.")
        elif self.service.lower() == "openai":
            if not self.openai_key:
                raise ValueError(
                    "You selected openai as the llm service. Provide its API Key"
                )
            if not self.temperature:
                raise ValueError("You must define the temperature to use")
            if not self.top_p:
                raise ValueError("You must define the top_p parameter to use")
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


LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "fastapi_file": {
            "class": "logging.handlers.RotatingFileHandler",  # Use RotatingFileHandler
            "filename": "/var/logs/fastapi.log",
            "formatter": "default",
            "maxBytes": 800 * 1024 * 1024,  # Max file size: 800 MB
            "backupCount": 3,  # Keep last 3 log files
        },
        "celery_file": {
            "class": "logging.handlers.RotatingFileHandler",  # Use RotatingFileHandler
            "filename": "/var/logs/celery_workers.log",
            "formatter": "default",
            "maxBytes": 800 * 1024 * 1024,  # Max file size: 800 MB
            "backupCount": 3,  # Keep last 3 log files
        },
    },
    "loggers": {
        "fastapi": {
            "handlers": ["console", "fastapi_file"],
            "level": os.getenv("LOG_LEVEL", "INFO"),
        },
        "celery": {
            "handlers": ["celery_file"],
            "level": os.getenv("CELERY_LOG_LEVEL", "INFO"),
        },
    },
}


def setup_logging() -> None:
    logging.config.dictConfig(LOG_CONFIG)
