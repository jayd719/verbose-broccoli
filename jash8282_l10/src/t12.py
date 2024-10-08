"""
-------------------------------------------------------
Lab 10, Task 12
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-11-22"
-------------------------------------------------------
"""

# Imports
from functions import find_shortest

# Constants
FILENAME = 'words.txt'

fh = open(FILENAME, "r", encoding="utf-8")

word = find_shortest(fh)
print(word)
