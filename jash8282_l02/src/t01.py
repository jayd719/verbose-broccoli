"""
-------------------------------------------------------
Convert a Celsius Temperature To Fahrenheit
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-09-20"
-------------------------------------------------------
"""

# Constants
# TODO: define freezing point of water
WATER_FREEZING_POINT = 32

# Inputs
temp_in_celsius = int(input("Enter Temperature(C): "))

# Calculations
# TODO: Convert fahrenheit into celsius
temp_in_fahrenheit = ((9 / 5) * temp_in_celsius) + WATER_FREEZING_POINT

# Output
print()
print('Temperature in Fahrenheit:', temp_in_fahrenheit)
