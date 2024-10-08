"""
-------------------------------------------------------
Assignment 9, Task 5
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-12-03"
-------------------------------------------------------
"""

# Imports
from functions import student_info

students = open("students.txt", "r", encoding="utf-8")
l_id, h_id, avg = student_info(students)

print(l_id, h_id, avg)
