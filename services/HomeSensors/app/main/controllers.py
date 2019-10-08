"""Main page for sensor controller and reads."""

import os
import subprocess
import signal

from flask import Blueprint, render_template, redirect, url_for, session

from app import cache
from app.models import TemperatureHumidity


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
    data = TemperatureHumidity().query.all()[-1]
    temp = data.temperature
    humidity = data.humidity
    state = "ON"

    return render_template(
        "home.html", temperature=temp, humidity=humidity, state=state
    )


@main_blueprint.route("/ldr/<n>")
def ldr(n):
    """Landing Page."""
    # from app.sensors.temp import test_sensor
    if n == "1":
        process_ = subprocess.Popen(
            "python3 app/sensors/temp.py", preexec_fn=os.setsid, shell=True
        )
        cache.set("temp_process", os.getpgid(process_.pid))
    elif n == "0":
        try:
            os.killpg(cache.get("temp_process"), signal.SIGTERM)
            cache.delete("temp_process")
        except TypeError:
            pass

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
