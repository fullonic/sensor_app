import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config=None):
    app = Flask(__name__)
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    from .main import create_module as main_create_module

    main_create_module(app)

    db.init_app(app)

    from .models import TemperatureHumidity  # noqa

    @app.shell_context_processor
    def ctx():
        return {"temp_hum": TemperatureHumidity}

    return app
