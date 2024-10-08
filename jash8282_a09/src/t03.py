"""
-------------------------------------------------------
Assigment 9 ,Task 3
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-12-03"
-------------------------------------------------------
"""

# Imports
from functions import file_stats

fh = open("address.txt", "r", encoding="utf-8")
ucount, lcount, dcount, wcount = file_stats(fh)
fh.close()

print(ucount, lcount, dcount, wcount)
