import RPi.GPIO as GPIO
import time

relay_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

try:
    while True:
        # set low
        print("Setting low - LED ON")
        GPIO.output(relay_pin, 0)
        time.sleep(2)
        # set high
        print("Setting high - LED OFF")
        GPIO.output(relay_pin, 1)
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Bye")
