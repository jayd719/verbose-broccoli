"""
-------------------------------------------------------
Assignment 3, Task 2
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-10-22"
-------------------------------------------------------
"""

# Imports
from functions import mow_lawn

# Inputs
# TODO: prompt user to enter width and length of lawn.
width = float(input('Width (m): '))
length = float(input('Length (m): '))
speed = float(input('Speed (m^2/minute): '))

# Calculations
# TODO: calculate how long it would take to mow lawn.
time = mow_lawn(width, length, speed)

# Output
print('')
print(f'Mowing the lawn takes {time:.0f} minutes')
