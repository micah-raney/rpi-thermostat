class Thermostat:
    modes = ['off', 'cold', 'heat', 'aux'] # exact mode?
    fan_modes = ['auto', 'on']

    def __init__(self, mode = 'off', fan_mode = 'auto', desired_temp_f = 75):
        self.mode = mode
        self.fan_mode = fan_mode
        self.desired_temp_f = desired_temp_f
        self.fan_status='off'
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

    def turn_fan_on(self):
        if self.fan_status is not 'on':
            #turn fan on
            print("fan turns on")
            self.fan_status = 'on'
            
    def turn_fan_off(self):
        if self.fan_status is not 'off':
            #turn fan off
            print("fan turns off")
            self.fan_status = 'off'

    def adjust_temp_f(self, current_temp_f):
        if (self.desired_temp_f == current_temp_f) or (self.mode == 'off'):
            self.go_inactive()
        elif self.mode == 'heat':
            if self.desired_temp_f < current_temp_f:
                self.go_inactive()
            else:
                self.turn_fan_on()
                # turn on heat
        elif self.mode == 'aux':
            if self.desired_temp_f < current_temp_f:
                self.go_inactive()
            else:
                self.turn_fan_on()
                # turn on aux heat
        elif self.mode == 'cold':
            if self.desired_temp_f > current_temp_f:
                self.go_inactive()
            else:
                self.turn_fan_on()
                # turn on cooler

