"""
-------------------------------------------------------
Midterm B Task 2 Function Definitions
-------------------------------------------------------
Author: Jd Jashandeep Singh
ID:     169018282
Email:  jash8282@mylaurier.ca
__updated__ = "2022-11-02"
-------------------------------------------------------
"""


def comic_condition(rating):
    """
    -------------------------------------------------------
    Determines the condition condition given an Air Quality Index (rating).
        If rating is 9.0 or greater, the condition is "near mint".
        If rating is 5.5 or greater but less than 9.0, the condition is "fine".
        If rating is 3.0 or greater but less than 5.5, the condition is "good".
        If rating is 1.5 or greater but less than 3.0, the condition is "fair".
        If rating is 0 or greater but less than 1.5 the condition is "poor".
        If rating is less than 0, return "Error"
    Use: condition = comic_condition(rating)
    -------------------------------------------------------
    Parameters:
        rating - air quality index (int >= 0)
    Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
        condition - description of comic book condition (str)
    -------------------------------------------------------
    """
    # TODO: get the comic condition using the rating
    if rating < 0:
        condition = 'Error'
    elif rating < 1.5:
        condition = 'poor'
    elif rating < 3:
        condition = 'fair'
    elif rating < 5.5:
        condition = 'good'
    elif rating < 9:
        condition = 'fine'
    else:
        condition = 'near mint'

    return condition
