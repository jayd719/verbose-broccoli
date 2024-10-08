"""
-------------------------------------------------------
Lab 9, Task 10
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-11-15"
-------------------------------------------------------
"""

# Imports
from functions import text_analyze

uppr, lowr, dgts, whtspc = text_analyze(
    'Python uses whitespace indentation, rather than curly brackets or keywords, to delimit blocks.')


print(f'{uppr},{lowr},{dgts},{whtspc}')
