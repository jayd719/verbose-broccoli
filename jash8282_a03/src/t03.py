"""
-------------------------------------------------------
Assignment 3, Task 3
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-10-23"
-------------------------------------------------------
"""

# Imports
from functions import date_extract

# Inputs
# TODO: prompt user to enter date.
date_number = int(input('Enter a date in the format MMDDYYYY: '))

# Calculations
# TODO: reformat date
year, month, day = date_extract(date_number)

# Output
# TODO: print re-formated date.
print('')
print(f'The reformatted date: {year}/{month:02d}/{day:02d}')
