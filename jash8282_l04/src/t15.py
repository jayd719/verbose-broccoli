"""
-------------------------------------------------------
Lab 4, Task 15
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-10-04"
-------------------------------------------------------
"""

# Imports
from functions import time_split


# Calculations
# TODO: Calculate days, hours, minutes and seconds
days, hours, minutes, seconds = time_split(956000)

# Output
# print out returned values
print(f'{days},{hours},{minutes},{seconds}')
