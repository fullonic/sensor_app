"""Main page for sensor controller and reads."""

from flask import Flask, render_template
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)


class TemperatureHumidity(db.Model):
    """Temperature and Humidity table."""

    __tablename__ = "temp_hum"
    temperature = db.Column(db.Float(8), nullable=False)
    humidity = db.Column(db.Float(8), nullable=False)
    date = db.Column(db.DateTime(), default=func.now())


# Sensors scripts


@app.route("/")
def home():
    """Landing Page."""
    temp = 30
    humidity = 54
    return render_template("home.html", temperature=temp, humidity=humidity)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
