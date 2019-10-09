from sqlalchemy import func

from app import db


class Sensors(db.Model):
    """Base sensor class."""

    __tablename__ = "sensors"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    frequency = db.Column(db.Float(32), default=1)
    running = db.Column(db.Boolean(), default=True)

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

    def __repr__(self):
        """Represent the state of all sensors."""
        return {sensor[0]: sensor[1] for sensor in self.query.all()}


class Data(db.Model):
    """Base sensor class."""

    __abstract__ = True
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.DateTime(), default=func.now())


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
