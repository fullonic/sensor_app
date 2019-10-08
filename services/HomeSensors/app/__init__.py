"""Home Sensor Pi."""

import os
import subprocess

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

db = SQLAlchemy()
cache = Cache()


def create_app(config=None):
    """Flask APP."""
    app = Flask(__name__)
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    from .main import create_module as main_create_module

    main_create_module(app)

    db.init_app(app)
    cache.init_app(app)

    from .models import TemperatureHumidity  # noqa
    from .models import Sensor  # noqa

    @app.before_first_request
    def start_sensors():
        # if cache.get("temp_process"):
        #     pass
        # else:
        process_ = subprocess.Popen(
            "python3 app/sensors/temp.py", preexec_fn=os.setsid, shell=True
        )
        cache.set("temp_process", os.getpgid(process_.pid))



    @app.shell_context_processor
    def ctx():
        return {"db": db, "temp_hum": TemperatureHumidity}

    return app
