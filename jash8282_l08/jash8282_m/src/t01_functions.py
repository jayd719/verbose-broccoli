"""
-------------------------------------------------------
Midterm B Task 1 Function Definitions
-------------------------------------------------------
Author: Jd Jashandeep Singh
ID:     169018282
Email:  jash8282@mylaurier.ca
__updated__ = "2022-11-02"
-------------------------------------------------------
"""
# Constants
# TODO: Define values for each case
ONE_PENNY = 1
TWO_PENCE = 3
FIVE_PENCE = 5
TEN_PENCE = 10

# your code here


def total_coins(pennies, two_pence, five_pence, ten_pence):
    """
    -------------------------------------------------------
    Determines total amount of money in coins in cents.
        1 penny coin = 1 pence
        1 two pence coin = 3 pence
        1 five pence coin = 5 pence
        1 ten pence coin = 10 pence
    Use: total = total_coins(penny, two_pence, five_pence, ten_pence)
    -------------------------------------------------------
    Parameters:
        pennies - number of penny coins (int >= 0)
        two_pence - number of two pence coins (int >= 0)
        five_pence - number of five pence coins (int >= 0)
        ten_pence - number of ten pence coins (int >= 0)
    Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
        total - total value of coins in pence (int)
    -------------------------------------------------------
    """

    # Calculations
    # TODO: Calculate the total
    total = (pennies * ONE_PENNY) + (two_pence * TWO_PENCE) + \
        (five_pence * FIVE_PENCE) + (ten_pence * TEN_PENCE)

    return total
