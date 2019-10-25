"""
Script to run app on raspberry pi start up.

This script will be called using the rc.local file.

Edit the file:
sudo nano /etc/rc.local

Add startup script to the rc.local. Must be the full path:

# SENSOR APP STARTUP SCRIPT
python3 /home/pi/Desktop/sensor_app/startup_script.py

"""

import subprocess


command = "docker-compose -f /home/pi/Desktop/sensor_app/docker-compose.yml up -d"
subprocess.Popen(command, shell=True)
