# rpi-thermostat core module
# Micah Raney
#
# Contains core functionality for thermostat:
# temperature detection, mode changes, and hardware interface.

DEG = '°'

import thermostat

fake_temp_f = 70

def read_temp_f():
	return fake_temp_f

def main_loop():
	current_temp_f = read_temp_f()
	desired_temp_f = t.get_desired_temp_f()

	print("Current Temp: " + str(current_temp_f) + DEG + " Fahrenheit")
	print("Desired Temperature: " + str(desired_temp_f))

#Program Start

print("\n*Start*\n")

t = thermostat.Thermostat(mode = 'heat')

for i in range(3):
	main_loop()
	fake_temp_f += 3 # temp rises

print("\n*End*\n")
