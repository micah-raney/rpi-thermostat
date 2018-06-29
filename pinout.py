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
        return "Fan switched to " + str(state)
    
    def cold_toggle(self, state):
        # write HIGH or LOW to self.cold_pin depending on state being 0 or 1
        return "Cold switched to " + str(state)
    
    def heat_toggle(self, state):
        # write HIGH or LOW to self.heat_pin depending on state being 0 or 1
        return "Heat switched to " + str(state)
    
    def aux_toggle(self, state):
        # write HIGH or LOW to self.aux_pin depending on state being 0 or 1
        return "Aux switched to " + str(state)
    