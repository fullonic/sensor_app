import time
import os
import random

import sqlalchemy as db
import datetime

# import Adafruit_DHT

from app import db
from app.models import TemperatureHumidity


# class DataBase:
#     engine = db.create_engine(os.environ.get("DATABASE_URL"))
#
#     def __init__(self):
#         self.connection = self.engine.connect()
#         print("DB Created")
#
#     def save_data(self, data):
#         self.connection.execute(
#             f"""INSERT INTO temp_hum(temperature, humidity, date) VALUES(
#             {TempHum.temperature},{TempHum.humidity},{TempHum.date})
#         """
#         )
#
#
# class TempHum:
#     def __init__(self, temperature, humidity):
#         self.temperature = temperature
#         self.humidity = humidity
#         self.date = datetime.datetime.now()
#

def run():
    for i in range(10):
        data = TemperatureHumidity()
        # humidity, temperature = Adafruit_DHT.read_retry(11, 17)
        temperature = random.randint(10, 21)
        humidity = random.randint(50, 88)
        data.temperature = temperature
        data.humidity = humidity
        db.session.add(data)
        db.session.commit()
        # print(f"Temperature: {temperature} ºC || Humidity: {humidity} %")
        print("writed")
        time.sleep(2)
    return "NONE"


if __name__ == "__main__":
    run()
