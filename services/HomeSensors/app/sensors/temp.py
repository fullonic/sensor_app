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

# Sensors = Base.classes.sensors

db_session = Session(engine)

def run():
    """Start reading date from sensors."""
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
        # print(f"Temperature: {temperature} ºC || Humidity: {humidity} %")
        time.sleep(0.2)

        s = db_session.query(Temp)[-1]
        if s.state is False:
            break


if __name__ == "__main__":
    run()
