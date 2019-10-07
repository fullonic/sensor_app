from sqlalchemy import func

from app import db


class TemperatureHumidity(db.Model):
    """Temperature and Humidity table."""

    __tablename__ = "temp_hum"
    id = db.Column(db.Integer(), primary_key=True)
    temperature = db.Column(db.Float(8), nullable=False)
    humidity = db.Column(db.Float(8), nullable=False)
    date = db.Column(db.DateTime(), default=func.now())

    def __ini__(self, temperature, humidity):  # noqa
        self.temperature = temperature
        self.humidity = humidity

    def __repr__(self):
        """Item information representation."""
        return f"Temp: {self.temperature} ºC || Hum: {self.humidity} % at {str(self.date)} "
