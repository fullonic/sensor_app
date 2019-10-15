# import os
# from threading import Thread
# import time
import json
from flask.cli import FlaskGroup

from app import create_app, db
from app.models import Sensors

# Sensors scripts
app = create_app()
cli = FlaskGroup(create_app=create_app)


# CLICK COMMANDS
@cli.command("recreate_db")
def recreate_db():
    """Create command for recreate db."""
    db.drop_all()
    print("CREATING DB")
    db.create_all()
    db.session.commit()


@cli.command("update_sensors_table")
def update_sensors_table():
    """Create populate sensors table data."""
    with open("app/sensors/config.json", "r") as f:
        conf_file = json.load(f)
    sensors = conf_file.get("sensors")
    for s in sensors:
        new_entry = Sensors(
            name=s["sensor_name"],
            running=s["config"]["running"],
            read_frequency=s["config"]["read_frequency"],
            write_to_db=s["config"]["write_to_db"],
        )
        db.session.add(new_entry)
        db.session.commit()


if __name__ == "__main__":
    # make_first_request()
    cli()
