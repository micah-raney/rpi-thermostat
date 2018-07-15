import time
import RPi.GPIO as GPIO    # Import GPIO handling library for Raspberry Pi

GPIO.setmode(GPIO.BCM)     # Set pinout numbering system to BCM
'''
pin1 = 23
pin2 = 24
pin3 = 25
pin4 = 26

GPIO.setup(pin1, GPIO.OUT)   # Set pin 1 as an output pin
GPIO.setup(pin2, GPIO.OUT)   # Set pin 2 as an output pin
GPIO.setup(pin3, GPIO.OUT)   # Set pin 3 as an output pin
GPIO.setup(pin4, GPIO.OUT)   # Set pin 4 as an output pin

GPIO.output(pin1, GPIO.HIGH) # Write high to pin 1
time.sleep(1)              # Wait one second
GPIO.output(pin1, GPIO.LOW)  # Write low to pin 1
GPIO.output(pin2, GPIO.HIGH) # Write high to pin 2
time.sleep(1)              # Wait one second
GPIO.output(pin2, GPIO.LOW)  # Write low to pin 2
GPIO.output(pin3, GPIO.HIGH) # Write high to pin 3
time.sleep(1)              # Wait one second
GPIO.output(pin3, GPIO.LOW)  # Write low to pin 3
GPIO.output(pin4, GPIO.HIGH) # Write high to pin 4
time.sleep(1)              # Wait one second
GPIO.output(pin4, GPIO.LOW)  # Write low to pin 4
time.sleep(1)

GPIO.cleanup()             # Clean all GPIO connections, circuit draws, etc.
'''

class Pinout:
    '''Handles hardware interaction and relay switching'''
    def __init__(self, fan_pin, cold_pin, heat_pin, aux_pin):
        self.fan_pin = fan_pin
        self.cold_pin = cold_pin
        self.heat_pin = heat_pin
        self.aux_pin = aux_pin

    def pinout_exists(self):
        return True

    def fan_toggle(self, state):
        # write HIGH or LOW to self.fan_pin depending on state being 0 or 1
        print("Fan switched to " + str(state))
    
    def cold_toggle(self, state):
        # write HIGH or LOW to self.cold_pin depending on state being 0 or 1
        print("Cold switched to " + str(state))
    
    def heat_toggle(self, state):
        # write HIGH or LOW to self.heat_pin depending on state being 0 or 1
        print("Heat switched to " + str(state))
    
    def aux_toggle(self, state):
        # write HIGH or LOW to self.aux_pin depending on state being 0 or 1
        print("Aux switched to " + str(state))
    
