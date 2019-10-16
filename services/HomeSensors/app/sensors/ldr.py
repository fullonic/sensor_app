#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# define the pin that goes to the circuit
GPIO_LDR = 4


def rc_time(GPIO_LDR):
    """Calculate capacitor recharge time."""
    count = 0

    # Output on the pin for
    GPIO.setup(GPIO_LDR, GPIO.OUT)
    GPIO.output(GPIO_LDR, GPIO.LOW)
    time.sleep(0.5)

    # Change the pin back to input
    GPIO.setup(GPIO_LDR, GPIO.IN)

    # Count until the pin goes high
    while GPIO.input(GPIO_LDR) == GPIO.LOW:
        count += 1

    return count


def manual_read():
    light = rc_time(GPIO_LDR)
    if light < 100:
        fase = "Dark"
    else:
        fase = "Light"
    # GPIO.cleanup()
    return f"fase: {light}"
