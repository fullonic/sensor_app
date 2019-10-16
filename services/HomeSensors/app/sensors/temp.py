import random
from datetime import datetime
import time

try:
    import Adafruit_DHT  # only works when running on pi
except ModuleNotFoundError:
    pass


def dht_sensor():
    """Temperature and Humidity sensor.

    Reads data from the sensor and directly and it to the DB.
    """
    # noqa
    humidity, temperature = Adafruit_DHT.read_retry(11, 17)
    return dict(temperature=temperature, humidity=humidity, date=datetime.now())


def sensor_test():
    """Generate fake data for testing purposes."""
    temperature = random.randint(10, 21)
    humidity = random.randint(50, 88)

    return dict(temperature=temperature, humidity=humidity, date=datetime.now())
