"""
-------------------------------------------------------
Assignment 1, Task 3
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-10-01"
-------------------------------------------------------
"""
# Constants
# TODO: define conversion factor from inches to m
CONVERSION_FACTOR = 0.0254

# Inputs
len_inches = int(input('Length in inches: '))

# Calculations
# TODO: Convert inches into meters
length_in_meters = len_inches * CONVERSION_FACTOR

# Output
# TODO: print length in meters
print('')
print(f'Length in m: {length_in_meters}')
