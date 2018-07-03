import pinout

class Thermostat:
    modes = ['off', 'heat', 'cold' 'aux'] # precise mode?
    fan_modes = ['auto', 'on']

    def __init__(self, pins, mode = 'off', fan_mode = 'auto', desired_temp_f = 75):
        self.pinout = pinout.Pinout(pins[0],pins[1],pins[2],pins[3])
        self.mode = mode
        self.fan_mode = fan_mode
        self.desired_temp_f = desired_temp_f
        self.fan_status='off'
        self.heat_status='off'
        self.cold_status='off'
        self.aux_status='off'
        print("Current Mode: " + str(self.mode))
        print("Current Fan Mode: " + str(self.fan_mode))
        print("Desired Temperature: " + str(self.desired_temp_f))
    
    def set_temp_f(self, temp_f):
        self.desired_temp_f = temp_f
        print("New desired temp: " + str(self.desired_temp_f))

    def get_desired_temp_f(self):
        return self.desired_temp_f

    def go_inactive(self):
        self.turn_fan_off()
        self.turn_heat_off()
        self.turn_cold_off()
        self.turn_aux_off()

    def turn_fan_on(self):
        if self.fan_status is not 'on':
            #turn fan on
            self.pinout.fan_toggle(1)
            self.fan_status = 'on'
            
    def turn_fan_off(self):
        if self.fan_status is not 'off':
            #turn fan off
            self.pinout.fan_toggle(0)
            self.fan_status = 'off'

    def turn_heat_on(self):
        if self.heat_status is not 'on':
            #turn heat on
            self.pinout.heat_toggle(1)
            self.heat_status = 'on'
            
    def turn_heat_off(self):
        if self.heat_status is not 'off':
            #turn heat off
            self.pinout.heat_toggle(0)
            self.heat_status = 'off'

    def turn_cold_on(self):
        if self.cold_status is not 'on':
            #turn cold on
            self.pinout.cold_toggle(1)
            self.cold_status = 'on'
            
    def turn_cold_off(self):
        if self.cold_status is not 'off':
            #turn cold off
            self.pinout.cold_toggle(0)
            self.cold_status = 'off'

    def turn_aux_on(self):
        if self.aux_status is not 'on':
            #turn aux on
            self.pinout.aux_toggle(1)
            self.aux_status = 'on'
            
    def turn_aux_off(self):
        if self.aux_status is not 'off':
            #turn aux off
            self.pinout.aux_toggle(0)
            self.aux_status = 'off'

    def adjust_temp_f(self, current_temp_f):
        if (self.desired_temp_f == current_temp_f) or (self.mode == 'off'):
            self.go_inactive()
        elif self.mode == 'heat':
            if self.desired_temp_f < current_temp_f:
                self.go_inactive()
            else:
                self.turn_fan_on()
                self.turn_heat_on()
        elif self.mode == 'cold':
            if self.desired_temp_f > current_temp_f:
                self.go_inactive()
            else:
                self.turn_fan_on()
                self.turn_cold_on()
        elif self.mode == 'aux':
            if self.desired_temp_f < current_temp_f:
                self.go_inactive()
            else:
                self.turn_fan_on()
                self.turn_aux_on()

