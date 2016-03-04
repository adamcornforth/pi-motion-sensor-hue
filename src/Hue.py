# Install gpiozero: 
# sudo apt-get update & sudo apt-get install python-gpiozero
# https://gpiozero.readthedocs.org/en/v1.1.0/

# Install python-dev:
# sudo apt-get install python2.7-dev

# Install spidev wrapper: 
# http://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/
# wget https://github.com/Gadgetoid/py-spidev/archive/master.zip
# unzip master.zip
# rm master.zip
# cd py-spidev-master
# sudo python setup.py install

# Install pip:
# sudo apt-get install python-pip

# Install phue 
# sudo pip install phue

from gpiozero import LED
from time import sleep
from phue import Bridge
import logging
import time

class Hue:
    """A class for controlling the hue lights"""

    def __init__(self):
        logging.basicConfig()
        self.b = Bridge('192.168.1.100')
        self.b.connect()

        self.lights = [3, 4]
        self.led = LED(17)

        self.light_on = False
        self.timeout_seconds = 5
        self.last_motion = time.time()

    def lights_on(self):
        """Turns the hue lights on"""
        print 'on'
        self.b.set_light(self.lights, 'on', True)
        self.b.set_light(self.lights, 'bri', 254)
        self.light_on = True

    def lights_off(self):
        """Turns the hue lights off"""
        print 'off'
        self.b.set_light(self.lights, 'on', False)
        self.light_on = False

    def is_light_on(self):
        """Returns whether the lights are on"""
        return self.light_on

    def timeout_elapsed(self):
        """Returns whether the last time motion occured was long enough ago"""
        return (time.time() - self.last_motion > self.timeout_seconds)

    def report_motion(self):
        """Is used for reporting motion - lights will turn on if they
        haven't been turned off recently"""
        self.led.on()  

        print "motion: time since motion {}".format((time.time() - self.last_motion))

        # time since last motion
        diff = time.time() - self.last_motion

        # set new time for last motion
        # but only if the last motion was
        # a positive number of seconds ago,
        # otherwise we need to wait it out
        if(diff > 0):
            self.last_motion = time.time()

        # we only want to turn lights off if they're off and the last
        # motion report was a positive number of seconds ago
        if not self.is_light_on() and diff > 0:
            self.lights_on()
            return True
        else:
            return False

    def report_no_motion(self):
        """Is used for reporting no motion - lights will turn off if the
        last motion was long enough ago"""
        self.led.off()

        print "time since motion {}".format((time.time() - self.last_motion))

        if(self.is_light_on() and self.timeout_elapsed()):

            self.last_motion = time.time() + 5  # reset motion time but put it in the negative
                                                # so that the lights turning off don't trigger 
                                                # motion which turns them back on again
            self.lights_off()
            return True 

        return False