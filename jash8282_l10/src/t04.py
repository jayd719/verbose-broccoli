"""
-------------------------------------------------------
Lab 10, Task 4
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-11-21"
-------------------------------------------------------
"""

# Imports
from functions import customer_first

fh = open('customers.txt', "r", encoding="utf-8")
result = customer_first(fh)

print(result)
