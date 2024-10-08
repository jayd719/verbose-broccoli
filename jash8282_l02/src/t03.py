"""
-------------------------------------------------------
Calculate Total Money Made
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-09-20"
-------------------------------------------------------
"""

# Constants
# TODO: define rates for large and small dog.
RATE_LARGE_DOG = 75
RATE_SMALL_DOG = 50

# Inputs
no_of_large_dogs = int(input('Number of large dogs groomed: '))
no_of_small_dogs = int(input('Number of small dogs groomed: '))

# Calculations
# TODO: calculate total money made
total_money_made = (RATE_LARGE_DOG * no_of_large_dogs) + \
    (RATE_SMALL_DOG * no_of_small_dogs)

# Output
print()
print('Total Money Made: $', total_money_made)
