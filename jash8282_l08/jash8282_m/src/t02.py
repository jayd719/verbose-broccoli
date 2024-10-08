"""
-------------------------------------------------------
Midterm B Task 2 Testing
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-11-02"
-------------------------------------------------------
"""
# Imports
from t02_functions import comic_condition

cases = (-1, 1.0, 1.8, 3.5, 7.5, 9.8)

for case in cases:
    condition = comic_condition(case)
    print(f"comic_condition({case}) → {condition}")
