import time
import random
import Adafruit_DHT

from controllers import db, TemperatureHumidity


while True:
    data = TemperatureHumidity()
    # humidity, temperature = Adafruit_DHT.read_retry(11, 17)
    temperature = random.randint()
    humidity = random.randint()
    data.temperature = temperature
    data.humidity = humidity
    db.session.add(data)
    db.session.commit()
    # print(f"Temperature: {temperature} ºC || Humidity: {humidity} %")
    time.sleep(15)
