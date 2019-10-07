from sqlalchemy import func

from app import db

class TemperatureHumidity(db.Model):
    """Temperature and Humidity table."""

    __tablename__ = "temp_hum"
    id = db.Column(db.Integer(), primary_key=True)
    temperature = db.Column(db.Float(8), nullable=False)
    humidity = db.Column(db.Float(8), nullable=False)
    date = db.Column(db.DateTime(), default=func.now())
