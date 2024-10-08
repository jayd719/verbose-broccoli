"""
-------------------------------------------------------
Lab 10, Task 14
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-11-22"
-------------------------------------------------------
"""

# Imports
from functions import file_copy_n

file1 = 'words.txt'
file2 = 'words_new.txt'

fh_1 = open(file1, "r", encoding="utf-8")
fh_2 = open(file2, "a", encoding="utf-8")


print(f"Copying '{file1}' to '{file2}'")
n = input('Number of lines to copy: ')

file_copy_n(fh_1, fh_2, n)
