"""
-------------------------------------------------------
Assignment 2, Task 4
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-10-08"
-------------------------------------------------------
"""

# Imports

# Constants

# Inputs
pieces_of_cake = int(input('Number of pieces of cake: '))
party_goers = int(input('Number of party-goers: '))

# Calculations
# TODO: Calculate number of pieces for each party goer.
pieces_per_head = pieces_of_cake // party_goers

# TODO: Calculate remaining pieces of cake
left_over_pieces = pieces_of_cake % party_goers

# Output
# TODO: print out calculated results
print('')
print(f'Each party-goer receives {pieces_per_head} pieces of cake')
print(f'Pieces of cake that won’t be distributed: {left_over_pieces} ')
