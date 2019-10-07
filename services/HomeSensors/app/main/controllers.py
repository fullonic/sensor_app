"""Main page for sensor controller and reads."""

import os

from flask import Blueprint, render_template, redirect, url_for
from app import db

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
    temp = 30
    humidity = 54

    return render_template(
        "home.html", temperature=temp, humidity=humidity, state=state
    )


@main_blueprint.route("/ldr/<n>")
def ldr(n):
    """Landing Page."""
    from app.sensors.temp import sensor
    switch = TemperatureHumidity()
    if n == "1":
        sensor()
        switch.turn_on()
    elif n == "0":
        switch.turn_off()
        # TODO:  Needs to solve problem with last entry empty
        last = switch.query.all()[-1]
        db.session.delete(last)
        db.session.commit()

    return redirect(url_for("main.home"))


# if __name__ == "__main__":
#     db.create_all()
#     app.run(debug=True)
