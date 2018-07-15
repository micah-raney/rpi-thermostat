import time
import RPi.GPIO as GPIO    # Import GPIO handling library for Raspberry Pi

GPIO.cleanup()             # Clean all GPIO connections, circuit draws, etc.
GPIO.setmode(GPIO.BCM)     # Set pinout numbering system to BCM

class Pinout:
    '''Handles hardware interaction and relay switching'''
    def __init__(self, fan_pin, cold_pin, heat_pin, aux_pin):
        self.fan_pin = fan_pin
        self.cold_pin = cold_pin
        self.heat_pin = heat_pin
        self.aux_pin = aux_pin
        GPIO.setup(fan_pin, GPIO.OUT)
        GPIO.setup(cold_pin, GPIO.OUT)
        GPIO.setup(heat_pin, GPIO.OUT)
        GPIO.setup(aux_pin, GPIO.OUT)

    def pinout_exists(self):
        return True

    def fan_toggle(self, state):
        # write HIGH or LOW to self.fan_pin depending on state being 0 or 1
        if state == 0:
            GPIO.output(self.fan_pin, GPIO.LOW)
        elif state == 1:
            GPIO.output(self.fan_pin, GPIO.HIGH)
        print("Fan switched to " + str(state))
    
    def cold_toggle(self, state):
        # write HIGH or LOW to self.cold_pin depending on state being 0 or 1
        if state == 0:
            GPIO.output(self.cold_pin, GPIO.LOW)
        elif state == 1:
            GPIO.output(self.cold_pin, GPIO.HIGH)
        print("Cold switched to " + str(state))
    
    def heat_toggle(self, state):
        if state == 0:
            GPIO.output(self.heat_pin, GPIO.LOW)
        elif state == 1:
            GPIO.output(self.heat_pin, GPIO.HIGH)
        print("Heat switched to " + str(state))
    
    def aux_toggle(self, state):
        # write HIGH or LOW to self.aux_pin depending on state being 0 or 1
        if state == 0:
            GPIO.output(self.aux_pin, GPIO.LOW)
        elif state == 1:
            GPIO.output(self.aux_pin, GPIO.HIGH)
        print("Aux switched to " + str(state))
    
