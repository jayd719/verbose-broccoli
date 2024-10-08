"""
-------------------------------------------------------
Lab 10, Task 2
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-11-21"
-------------------------------------------------------
"""

# Imports
from functions import customer_by_id

print('Find customer by id_number')
id_number = input('Enter an ID: ')

fh = open('customers.txt', "r", encoding="utf-8")
result = customer_by_id(fh, id_number)

print(result)
