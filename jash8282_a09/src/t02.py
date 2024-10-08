"""
-------------------------------------------------------
Assignment 9, Task 2
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-12-03"
-------------------------------------------------------
"""

# Imports
from functions import file_integers

fh = open("numbers.txt", "r", encoding="utf-8")
numbers = file_integers(fh)
fh.close()


print(numbers)
