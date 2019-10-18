"""Basic tests for main app and other services."""

import random
from datetime import datetime, timedelta


from app import db
from app.main import tasks
from app.models import TemperatureHumidity


def test_tasks():
    """Tests if celery and broker are working properly."""
    return tasks.log.apply_async(["This is a test"], countdown=1)


def create_fake():
    now = datetime.now()
    for hour in range(0, 24):
        for i in range(0, 10):
            data = dict(
                hour=hour,
                temperature=random.randint(15, 25),
                humidity=random.randint(50, 75),
                date=now,
            )
            dht = TemperatureHumidity(**data)
            db.session.add(dht)
            db.session.commit()



if __name__ == "__main__":
    test_tasks()
    create_fake()
