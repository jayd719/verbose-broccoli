"""
-------------------------------------------------------
Assignment 3, Task 1
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-10-23"
-------------------------------------------------------
"""

# Imports
from functions import feet_to_acres


# Input
# TODO: ask user to enter square foot
square_footage = float(input('Square footage: '))

# Calculations
# TODO: convert given square foot into acres.
acres = feet_to_acres(square_footage)

# Output
# TODO: print out calculated result.
print('')
print(f'{acres:,.2f} acres is equivalent to {square_footage:,.2f} square feet')
