class Thermostat:
    modes = ['off', 'cold', 'heat', 'aux']
    fan_modes = ['auto', 'on']

    def __init__(self, mode = 'off', fan_mode = 'auto', desired_temp_f = 75):
        self.mode = 'off'
        self.fan_mode = 'auto'
        self.set_temp_f(75)
        print("initiated new instance")
    
    def set_temp_f(self, temp_f):
        self.desired_temp_f = temp_f
        print("New desired temp: " + str(self.desired_temp_f))

    def get_desired_temp_f(self):
        return self.desired_temp_f