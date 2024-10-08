"""
-------------------------------------------------------
Lab 3, Task 10
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-09-27"
-------------------------------------------------------
"""

# Inputs
year = int(input('Enter a year: '))
month = int(input('Enter a month:'))
day = int(input('Enter a day: '))

# TODO: re-format date
date = f'{year}/{month:02d}/{day:02d}'

# Output
print(date)
