"""Data Base models."""

import csv
import json

from datetime import datetime

from sqlalchemy import func
from app import db


class Sensors(db.Model):
    """Base sensor class."""

    __tablename__ = "sensors"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    read_frequency = db.Column(db.Float(32), default=1)
    write_to_db = db.Column(db.Float(32), default=60)
    running = db.Column(db.Boolean(), default=True)

    def __init__(self, name, running, read_frequency, write_to_db):  # noqa
        self.name = name
        self.running = running
        self.read_frequency = read_frequency
        self.write_to_db = write_to_db

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
            "config": {
                "running": self.running,
                "read_frequency": self.read_frequency,
                "write_to_db": self.write_to_db,
            },
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

    @classmethod
    def daily_resume(self):
        """Generate the daily average by hour of Temperature and Humidity.

        This method runs every day at 23:59
        """
        # Create a base information to populate historic tables with actual day of the year
        date = datetime.now()
        year = date.year
        month = date.month
        day = date.day
        date_values = dict(day=day, month=month, year=year)
        # All day hours
        hours = [i for i in range(24)]
        for hour in hours:
            # Avoids error when app runs for the first and there is no records for all hours
            temp_value = (
                self.query.with_entities(func.avg(self.temperature))
                .filter_by(hour=hour)
                .first()
            )
            hum_value = (
                self.query.with_entities(func.avg(self.humidity))
                .filter_by(hour=hour)
                .first()
            )

            if hum_value[0] is not None:
                temp = Temperature(
                    **date_values, hour=hour, value=round(temp_value[0], 2)
                )
                hum = Humidity(**date_values, hour=hour, value=round(hum_value[0], 2))

                db.session.add(temp)
                db.session.add(hum)
                db.session.commit()
        self.clean_up()

    @classmethod
    def clean_up(self):
        """Clean up old information after daily resume."""
        data = self.query.filter(self.date < datetime.now()).all()
        for rec in data:
            db.session.delete(rec)
            db.session.commit()


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

    def __repr__(self):
        """Item information representation."""
        return str(self.to_json)

    @property
    def to_json(self):
        """JSON representation of sensor config."""
        return [
            {
                "hour": rec.hour,
                "day": rec.day,
                "month": rec.month,
                "year": rec.year,
                "value": rec.value,
                "unit": rec.unit,
            }
            for rec in self.query.all()
        ]

    @classmethod
    def backup(self, format="json"):
        """Generate Historic data backups."""
        fname = f"[BACKUP:]{self.__name__}_{str(datetime.now())}.{format}"

        if format == "json":
            with open(f"./app/static/data-backups/{fname}", "w") as f:
                json.dump({self.__name__: self().to_json}, f)


class Temperature(Historic):
    """Temperature Historic Records."""

    __tablename__ = "historic_temperature"

    unit = db.Column(db.String(4), default="ºC")


class Humidity(Historic):
    """Temperature Historic Records."""

    __tablename__ = "historic_humidity"

    unit = db.Column(db.String(4), default="%")
