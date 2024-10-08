"""
-------------------------------------------------------
Midterm B Task 1 Testing
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-11-02"
-------------------------------------------------------
"""
# Imports
from t01_functions import total_coins

CASES = (
    (0, 0, 0, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (1, 1, 1, 1),
    (10, 10, 10, 10)
)
for case in CASES:
    pennies = case[0]
    two_pence = case[1]
    five_pence = case[2]
    ten_pence = case[3]
    total = total_coins(pennies, two_pence, five_pence, ten_pence)
    print(f"total_coins{case} → {total}")
