"""APP main configurations."""

import os
from datetime import timedelta

from celery.schedules import crontab


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
        "write-to-db": {
            "task": "app.main.tasks.write_to_db",
            "schedule": timedelta(seconds=60),
        },
        "daily-resume": {
            "task": "app.main.tasks.generate_daily_resume",
            "schedule": crontab(day_of_week="*", hour="23", minute="59"),
        },
    }

    TIMEZONE = "UTC"
