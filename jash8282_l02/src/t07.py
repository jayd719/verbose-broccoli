"""
-------------------------------------------------------
Calculate number of flyers per volunteer and number of flyers left over
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-09-20"
-------------------------------------------------------
"""

# Constants

# Inputs
no_of_flyers = int(input('Number of flyers:'))
no_of_volunteers = int(input('Number of volunteers:'))

# Calculations
# TODO: Calculate Flyers per volunteer:
flyer_per_volunteer = no_of_flyers // no_of_volunteers

# TODO: Calculate left over flyers
left_over_flyeres = no_of_flyers % no_of_volunteers

# Output
print('Flyers per volunteer:', flyer_per_volunteer)
print('Flyers left over:', left_over_flyeres)
