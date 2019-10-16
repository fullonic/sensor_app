"""Generate celery base app for background tasks."""

import os

from celery import Celery

from app import create_app
from app.config import Config


def make_app(app):
    """Create celery app."""
    app.config["CELERY_IMPORTS"] = ("app.main.tasks", )  # Points to tasks file
    celery = Celery(
        app.import_name,
        broker=app.config["CELERY_BROKER_URL"],
        backend=app.config["CELERY_RESULT_BACKEND"],
    )

    celery.conf.update(app.config)

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery


flask_app = create_app(Config)

celery = make_app(flask_app)
