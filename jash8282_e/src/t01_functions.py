"""
-------------------------------------------------------
Exam Task 1 Function Definitions
Fall 2022
-------------------------------------------------------
Author: Jashandeep Singh
ID:     169018282
Email:  jash8282@mylaurier.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""


def max_diff(values):
    """
    -------------------------------------------------------
    Returns largest absolute difference between adjacent
    values in a list. Returns 0 if values has fewer than two elements.
    Use: md = max_diff(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
        md - the largest absolute difference between adjacent numbers in values (int)
    -------------------------------------------------------
    """

    # Your code here
    md = 0
    if len(values) >= 2:
        i = 0
        while i + 1 < len(values):
            if abs(values[i] - values[i + 1]) > md:
                md = abs(values[i] - values[i + 1])
            i += 1
    return md
