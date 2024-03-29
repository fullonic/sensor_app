"""Temperature and Humidity sensor read data."""

import random
import time
from datetime import datetime

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()


engine = create_engine("postgres://postgres:postgres@172.19.0.2:5432/sensors_dev")

Base.prepare(engine, reflect=True)

Temp = Base.classes.temp_hum
DHT = Base.classes.sensors

# Sensors = Base.classes.sensors
db_session = Session(engine)


def sensor():
    """Temperature and Humidity sensor.

    Reads data from the sensor and directly and it to the DB.
    """
    import Adafruit_DHT  # noqa

    s = db_session.query(DHT).filter_by(name="DHT").first()
    freq = s.frequency
    while True:
        data = Temp()
        # humidity, temperature = Adafruit_DHT.read_retry(11, 17)
        humidity, temperature = Adafruit_DHT.read_retry(11, 17)

        data.temperature = temperature
        data.humidity = humidity
        data.date = datetime.now()
        db_session.add(data)
        db_session.commit()
        time.sleep(freq)

        s = db_session.query(DHT).filter_by(name="DHT").first()
        if s.running is False:
            break


def test_sensor():
    """Generate fake data in order to test data insert to DB."""
    s = db_session.query(DHT).filter_by(name="DHT").first()
    freq = s.frequency

    while True:
        data = Temp()
        # humidity, temperature = Adafruit_DHT.read_retry(11, 17)
        temperature = random.randint(10, 21)
        humidity = random.randint(50, 88)
        data.temperature = temperature
        data.humidity = humidity
        data.date = datetime.now()
        db_session.add(data)
        db_session.commit()
        time.sleep(0.2)

        s = db_session.query(DHT).filter_by(name="DHT").first()
        if s.running is False:
            break


def run(host):
    if host == "pi":
        test_sensor()
    else:
        test_sensor()


if __name__ == "__main__":
    run(host=None)
