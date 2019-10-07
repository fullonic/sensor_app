from sqlalchemy import func

from app import db


class Sensor(db.Model):
    """Base sensor class."""

    __abstract__ = True
    id = db.Column(db.Integer(), primary_key=True)
    state = db.Column(db.Boolean(), default=True)
    date = db.Column(db.DateTime(), default=func.now())

    def turn_on(self):
        """Turn ON a sensor."""
        self.state = True
        db.session.add(self)
        db.session.commit()

    def turn_off(self):
        """Turn OFF a sensor."""
        # s = Sensors.query.filter_by(id=self.id)
        # self = self.query.all()[-1]
        self.state = False
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        """Represent the state of all sensors."""
        return f"<Temp_Hum: {self.temp_hum} || LDR: {self.ldr} || PIR: {self.pir}"


class TemperatureHumidity(Sensor):
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
