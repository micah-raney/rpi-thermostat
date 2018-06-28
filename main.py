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

t = thermostat.Thermostat(mode='heat', desired_temp_f=75)

while t.get_desired_temp_f() is not read_temp_f():
	fake_temp_f += 1 # temp rises
	main_loop()
	t.adjust_temp_f(read_temp_f())
	print()
print("*End*\n")
