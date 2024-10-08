"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-10-08"
-------------------------------------------------------
"""

# Inputs
user_entered_date = int(input('Enter a date in the format DDMMYYYY: '))

# Calculations
# TODO: Calculate Year from given date
year = user_entered_date % 10000
month = (user_entered_date // 10000) % 100
day = (user_entered_date // 10000) // 100

# Output
# TODO: print out re-formatted date.
print('')
print(f'The reformatted date: {year}/{month:02d}/{day:02d}')
