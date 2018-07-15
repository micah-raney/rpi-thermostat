import time
import RPi.GPIO as GPIO    # Import GPIO handling library for Raspberry Pi

GPIO.setmode(GPIO.BCM)     # Set pinout numbering system to BCM
'''
GPIO.setup(19, GPIO.OUT)   # Set pin 19 as an output pin

GPIO.output(19, GPIO.HIGH) # Write high to pin 19
time.sleep(1)              # Wait one second
GPIO.output(19, GPIO.LOW)  # Write low to pin 19

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
    
