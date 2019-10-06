import time

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# Define GPIO to use on Pi
GPIO_PIR = 7
GPIO.setup(GPIO_PIR, GPIO.IN)  # Read output from PIR motion sensor
# GPIO.setup(3, GPIO.OUT)         #LED output pin


print("Starting....")
try:
    while True:
        if GPIO.input(GPIO_PIR) == 1:  # When output from motion sensor is LOW
            print("MOTION DETECTED")
        else:
            print("NO MOTION")

        time.sleep(0.1)

except KeyboardInterrupt:
    print(" Quit")
    # Reset GPIO settings
    GPIO.cleanup()
