"""
-------------------------------------------------------
Lab 10, Task 9
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-11-22"
-------------------------------------------------------
"""

# Imports
from functions import count_frequency_value

# Constants
FILENAME = 'numbers.txt'


fh = open(FILENAME, "r", encoding="utf-8")

print(f"file '{FILENAME}' open for reading")
value = int(input('Value to count: '))
count = count_frequency_value(fh, value)

print('')
print(f'{value} appears {count} time(s)')
