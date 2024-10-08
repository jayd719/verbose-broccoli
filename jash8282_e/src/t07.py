"""
-------------------------------------------------------
Testing for Task 7: file_split
-------------------------------------------------------
Author: Jd Jashandeep Singh
ID:     169018282
Email:  jash8282@mylaurier.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""
# Imports
from t07_functions import file_split


# Your code here
f_in = open('source.txt', 'r', encoding='utf-8')
f_digits = open('f_digits.txt', 'w', encoding='utf-8')
f_no_digits = open('f_no_digits', 'w', encoding='utf-8')

file_split(f_in, f_digits, f_no_digits)


f_in.close()
f_digits.close()
f_no_digits.close()
