import random
from datetime import datetime
import time

from app import cache, db
from app.models import Sensors, TemperatureHumidity


def dht_sensor():
    """Temperature and Humidity sensor.

    Reads data from the sensor and directly and it to the DB.
    """
    import Adafruit_DHT  # noqa

    dht = Sensors.query.filter_by(name="dht").first()
    freq = dht.frequency
    while cache.get("dht_running"):
        hum, temp = Adafruit_DHT.read_retry(11, 17)
        data = TemperatureHumidity(temperature=temp, humidity=hum)
        data.date = datetime.now()
        db.session.add(data)
        db.session.commit()
        time.sleep(freq)

    else:
        print("STOPPED")


def sensor_test():
    """Generate fake data for testing purposes."""
    # dht = Sensors.query.filter_by(name="dht").first()
    freq = 1  # frequency of reading data for real time information
    write_to_db = 10  # frequency of saving to db
    count = 0  # flag variable
    while cache.get("dht_running"):
        temperature = random.randint(10, 21)
        humidity = random.randint(50, 88)
        cache.set("real_temp", temperature)
        cache.set("real_hum", humidity)
        if count == write_to_db:
            data = TemperatureHumidity()
            # humidity, temperature = Adafruit_DHT.read_retry(11, 17)
            temperature = random.randint(10, 21)
            humidity = random.randint(50, 88)
            data.temperature = temperature
            data.humidity = humidity
            data.date = datetime.now()

            db.session.add(data)
            db.session.commit()
            write_to_db += count
        count += 1
        time.sleep(freq)
        dht = Sensors.query.filter_by(name="DHT").first()
        if not dht.running:
            break

    else:
        print("STOPPED")


if __name__ == "__main__":
    sensor_test()
