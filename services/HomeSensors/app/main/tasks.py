"""Application background tasks executed by celery."""

from .. import celery
from app import db
from app.models import TemperatureHumidity, Humidity, Temperature

try:  # only works when running on pi
    import Adafruit_DHT  # noqa
    from app.sensors.temp import dht_sensor as sensor
except ModuleNotFoundError:
    from app.sensors.temp import sensor_test as sensor


@celery.task()
def log(msg):
    """For TESTING."""
    return msg


@celery.task()
def generate_daily_resume():
    """Generate the daily resume."""
    # Create daily resume
    TemperatureHumidity.daily_resume()
    return "Created"


@celery.task()
def generate_daily_backup():
    """Generate the daily backup."""
    # Create daily resume
    Humidity.backup()
    Temperature.backup()
    return "BACKUP CREATED"


@celery.task()
def write_to_db():
    """Write DHT data to DB model."""
    data = TemperatureHumidity(**sensor())
    db.session.add(data)
    db.session.commit()
