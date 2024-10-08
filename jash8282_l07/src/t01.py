"""
-------------------------------------------------------
Lab 7, Task 1
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-11-01"
-------------------------------------------------------
"""

# Imports
from functions import hi_lo_game

# Constants


count = hi_lo_game(100)
if count >= 2:
    print(f'You made {count} guesses.')
else:
    print(f'You made 1 guess.')
