import os
import logging.config

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
