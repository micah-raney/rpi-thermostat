# rpi-thermostat core module
# Micah Raney
#
# Contains core functionality for thermostat:
# temperature detection-adjustment loop,
# hardware pinout assignments

DEG = '°'

import thermostat

fake_temp_f = 70
test_mode = 'heat'

def read_temp_f():
	return fake_temp_f

def main_loop():
	current_temp_f = read_temp_f()
	desired_temp_f = t.get_desired_temp_f()

	print("Current Temp: " + str(current_temp_f) + DEG + " Fahrenheit")
	print("Desired Temperature: " + str(desired_temp_f))

# Program Start

print("\n*Start*\n")

fan = 1
cold = 2
heat = 3
aux = 4
pins = [ fan, cold, heat, aux ]
t = thermostat.Thermostat(pins, test_mode, 'auto', 65)

while t.mode is not 'off' and t.get_desired_temp_f() is not read_temp_f():
	if test_mode == 'heat' or test_mode == 'aux':
		fake_temp_f += 1 # temp raises
	elif test_mode == 'cold':
		fake_temp_f -= 1 # temp lowers
	main_loop()
	t.adjust_temp_f(read_temp_f())
	print()
print("*End*\n")
