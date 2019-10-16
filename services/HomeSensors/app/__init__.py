"""Home Sensor Pi."""

import os
import datetime
from threading import Thread

from flask import Flask
from werkzeug.serving import is_running_from_reloader
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from flask_celery import Celery

db = SQLAlchemy()
cache = Cache()
migrate = Migrate()
celery = Celery()


def create_app(config=None):
    """Flask APP."""
    app = Flask(__name__)
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    from .main import create_module as main_create_module

    main_create_module(app)

    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    celery.init_app(app)

    from .models import TemperatureHumidity, Sensors, Temperature, Humidity  # noqa
    from app.sensors.temp import sensor_test, dht_sensor  # noqa

    # FOR CELERY TEST ONLY
    from app.main.tasks import log

    @app.shell_context_processor
    def ctx():
        return {
            "db": db,
            "temp_hum": TemperatureHumidity,
            "Sensors": Sensors,
            "Temperature": Temperature,
            "Humidity": Humidity,
            "log": log,
        }

    return app
