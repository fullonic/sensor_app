"""Main page for sensor controller and reads."""

import os
import subprocess
import signal

from flask import Blueprint, render_template, redirect, url_for, session

from app import cache
from app.models import TemperatureHumidity, Sensors
from app.sensors.temp import sensor_test


main_blueprint = Blueprint(
    "main",
    __name__,
    template_folder="../templates",
    static_folder="../static",
    url_prefix="/main",
)


@main_blueprint.route("/")
def home(state="OFF"):
    """Landing Page."""
    temp = cache.get("real_temp")
    humidity = cache.get("real_hum")

    state = "ON"

    return render_template(
        "home.html", temperature=temp, humidity=humidity, state=state
    )


@main_blueprint.route("/dht/<n>", methods=["POST", "GET"])
def dht(n):
    """Landing Page."""
    dht = Sensors.query.filter_by(name="DHT").first()
    if n == "on":
        dht.turn_on()
        cache.set("dht_running", True)
        sensor_test()
    elif n == "off":
        dht.turn_off()
        cache.set("dht_running", False)
        cache.set("real_temp", None)
        cache.set("real_hum", None)
        sensor_test()
    return redirect(url_for("main.home"))


@main_blueprint.route("/sensor")
def sensor():
    data = TemperatureHumidity().query.all()[-1]

    return {
        "Temp": f"{data.temperature} ºC",
        "Humidity": f"{data.humidity} %",
        "Date Time": str(data.date),
    }


# if __name__ == "__main__":
#     db.create_all()
#     app.run(debug=True)
