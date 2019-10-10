"""Home Sensor Pi."""

import os
import datetime
from threading import Thread

from flask import Flask
from werkzeug.serving import is_running_from_reloader
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache

db = SQLAlchemy()
cache = Cache()
migrate = Migrate()


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

    from .models import TemperatureHumidity  # noqa
    from .models import Sensors  # noqa
    from app.sensors.temp import sensor_test

    # TODO: CRETE HERE A THREAD TO START SENSORS
    @app.before_first_request
    def start_sensors():
        def run(app):
            with app.app_context():
                sensor_test()

        Thread(target=run, args=(app,)).start()
        with open("log.txt", "w") as f:
            f.write(f"RUNNING FIRST:  {str(cache.get('dht_running'))}")
            f.write(str(datetime.datetime.now()))


    @app.shell_context_processor
    def ctx():
        return {"db": db, "temp_hum": TemperatureHumidity, "Sensors": Sensors}

    return app
