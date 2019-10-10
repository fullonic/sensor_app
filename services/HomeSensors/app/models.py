from sqlalchemy import func
from datetime import datetime

from app import db


class Sensors(db.Model):
    """Base sensor class."""

    __tablename__ = "sensors"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    frequency = db.Column(db.Float(32), default=1)
    running = db.Column(db.Boolean(), default=True)

    def __init__(self, name, frequency, running):  # noqa
        self.name = name
        self.frequency = frequency
        self.running = running

    def turn_on(self):
        """Turn ON a sensor."""
        self.running = True
        db.session.add(self)
        db.session.commit()

    def turn_off(self):
        """Turn OFF a sensor."""
        self.running = False
        db.session.add(self)
        db.session.commit()

    @property
    def to_json(self):
        """JSON representation of sensor config."""
        return {
            "sensor_name": self.name,
            "config": {"frequency": self.frequency, "running": self.running},
        }

    def __repr__(self):
        """Represent the state of all sensors."""
        return str(self.to_json)


class Data(db.Model):
    """Base sensor class."""

    __abstract__ = True
    id = db.Column(db.Integer(), primary_key=True)
    hour = db.Column(db.Integer(), default=datetime.now().hour)
    date = db.Column(db.DateTime(), default=datetime.now())


class TemperatureHumidity(Data):
    """Temperature and Humidity table."""

    __tablename__ = "temp_hum"
    temperature = db.Column(db.Float(8))
    humidity = db.Column(db.Float(8))

    def __ini__(self, temperature, humidity):  # noqa
        self.temperature = temperature
        self.humidity = humidity

    def __repr__(self):
        """Item information representation."""
        return f"Temp: {self.temperature} ºC || Hum: {self.humidity} % at {str(self.date)} "

    def daily_resume(self):
        daily = None


class LDR(Data):
    """Model for LDR sensor."""

    __tablename__ = "ldr"
    fase = db.Column(db.String(32), default="Day")


class Historic(db.Model):
    """Base model for Historic Records."""

    __abstract__ = True
    id = db.Column(db.Integer(), primary_key=True)
    hour = db.Column(db.Integer(), nullable=False)
    day = db.Column(db.Integer(), nullable=False)
    month = db.Column(db.Integer(), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    value = db.Column(db.Float(), nullable=False)


class Temperature(Historic):
    """Temperature Historic Records."""

    __tablename__ = "historic_temperature"

    unit = db.Column(db.String(4), default="ºC")

    @property
    def to_json(self):
        """JSON representation of sensor config."""
        return {
            "sensor_name": "Temperature",
            "data": {
                "hour": self.hour,
                "day": self.day,
                "month": self.month,
                "year": self.year,
                "value": self.value,
            },
        }


class Humidity(Historic):
    """Temperature Historic Records."""

    __tablename__ = "historic_humidity"

    unit = db.Column(db.String(4), default="%")

    @property
    def to_json(self):
        """JSON representation of sensor config."""
        return {
            "sensor_name": "Temperature",
            "data": {
                "hour": self.hour,
                "day": self.day,
                "month": self.month,
                "year": self.year,
                "value": self.value,
            },
        }
