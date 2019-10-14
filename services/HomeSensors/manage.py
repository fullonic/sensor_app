# import os
# from threading import Thread
# import time
# import requests
from flask.cli import FlaskGroup

from app import create_app

# Sensors scripts
app = create_app()
cli = FlaskGroup(create_app=create_app)


if __name__ == "__main__":
    # make_first_request()
    cli()
