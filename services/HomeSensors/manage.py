# import os
# from threading import Thread
# import time
# import requests
from flask.cli import FlaskGroup

from app import create_app

# Sensors scripts
app = create_app()
cli = FlaskGroup(create_app=create_app)


# def make_first_request():
#     def check():
#         status_code = 0
#         while status_code != 200:
#             try:
#                 req = requests.get("http://localhost:80/main/real_time")
#                 status_code = req.status_code
#                 if req.status_code == 200:
#                     requests.get("http://localhost:80/main/real_time")
#                     status_code = 200
#                     print("DONE")
#                     break
#                 print("FAILED")
#             except:
#                 time.sleep(1)
#             print("RETRY")
#
#     # url = "http://localhost:5001/main/real_time"
#     Thread(target=check).start()

if __name__ == "__main__":
    # make_first_request()
    cli()
