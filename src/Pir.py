#!/usr/bin/python

import RPi.GPIO as GPIO
import time

class Pir:
    """A class for detecting Motion through the PIR"""
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.pir_pin = 18
        GPIO.setup(self.pir_pin, GPIO.IN)
    
    def detectMotion(self):
        if GPIO.input(self.pir_pin):
            return True;
        else:
            return False; 
