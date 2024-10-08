"""
-------------------------------------------------------
Assignment 9, Task 1
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-12-03"
-------------------------------------------------------
"""

# Imports
from functions import file_head


fh = open("functions.py", "r", encoding="utf-8")
file_head(fh, 5)
fh.close()
