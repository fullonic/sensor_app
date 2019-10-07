"""Main page for sensor controller and reads."""

import os

from flask import current_app, Blueprint, render_template
from app import db

main_blueprint = Blueprint(
    "main",
    __name__,
    template_folder="../templates",
    static_folder="../static",
    url_prefix="/main",
)


@main_blueprint.route("/")
def home():
    """Landing Page."""
    db.create_all()
    temp = 30
    humidity = 54
    return render_template("home.html", temperature=temp, humidity=humidity)


@main_blueprint.route("/ldr")
def ldr():
    """Landing Page."""
    from app.sensors.temp import run

    ldr = run()
    # return render_template("home.html", temperature=temp, humidity=humidity)
    return ldr


# if __name__ == "__main__":
#     db.create_all()
#     app.run(debug=True)
