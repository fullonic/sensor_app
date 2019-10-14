"""APP main configurations."""

import os
from datetime import timedelta


class Config:
    SECRET_KEY = "HOME SENSOR APP"
    DEBUG = True

    CACHE_TYPE = "simple"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    # CELERY CONFIGURATION
    CELERY_BROKER_URL = "amqp://rabbitmq:rabbitmq@localhost//"
    CELERY_RESULT_BACKEND = "amqp://rabbitmq:rabitmq@localhost//"

    CELERYBEAT_SCHEDULE = {
        "log-10-sec":{
            "task": "app.main.tasks.log",
            "schedule": timedelta(seconds=10),
            "args": ("this is a test",)
        }
    }

    TIMEZONE = 'UTC'
