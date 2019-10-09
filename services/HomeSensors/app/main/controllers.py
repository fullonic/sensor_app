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


@main_blueprint.route("/dht/<switch>", methods=["POST", "GET"])
def dht(switch):
    """Landing Page."""
    dht = Sensors.query.filter_by(name="DHT").first()
    if switch == "on":
        dht.turn_on()
        cache.set("dht_running", True)
        sensor_test()
    elif switch == "off":
        dht.turn_off()
        cache.set("dht_running", False)
        cache.set("real_temp", None)
        cache.set("real_hum", None)
        sensor_test()
    return redirect(url_for("main.home"))


@main_blueprint.route("/ldr", methods=["POST", "GET"])
def ldr():
    """Get LDR Information."""
    from app.sensors.ldr import manual_read  # noqa
    pass
