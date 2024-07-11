import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.insert(0, root_dir)

from src.config.settings import settings

if not os.path.exists(settings.LOG_PATH):
    os.makedirs(settings.LOG_PATH)

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s [product-registration-api] %(module)s.%(funcName)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "default",
            "filename": f"{settings.LOG_PATH}/{settings.LOG_FILE_NAME}",
            "when": "midnight",
            "interval": 1,
            "backupCount": 30,
            "encoding": "utf-8"
        }
    },
    "loggers": {
        "fastapi": {
            "level": "INFO",
            "handlers": ["console", "file"],
            "propagate": False
        },
        "uvicorn": {
            "level": "INFO",
            "handlers": ["console", "file"],
            "propagate": False
        },
        "uvicorn.error": {
            "level": "INFO",
            "handlers": ["console", "file"],
            "propagate": False
        },
        "uvicorn.access": {
            "level": "CRITICAL",
            "handlers": ["console", "file"],
            "propagate": False
        }
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO"
    }
}