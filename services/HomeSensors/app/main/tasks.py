"""Application background tasks executed by celery."""

from .. import celery
from app import db
from app.models import TemperatureHumidity
from app.sensors.temp import sensor_test


@celery.task()
def log(msg):
    """For TESTING."""
    return msg


@celery.task(ignore_result=True)
def generate_daily_resume():
    """Generate the daily resume."""
    # Create daily resume
    TemperatureHumidity.daily_resume()
    return "Created"


@celery.task()
def write_to_db():
    """Write DHT data to DB model."""
    reads = sensor_test()
    data = TemperatureHumidity(**reads)
    db.session.add(data)
    db.session.commit()
