"""
-------------------------------------------------------
Exam Task 3 Function Definitions
Fall 2022
-------------------------------------------------------
Author: Jashandeep Singh
ID:     169018282
Email:  jash8282@mylaurier.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""


def alternate_case(string):
    """
    -------------------------------------------------------
    Converts letters in a string to alternate case. Letters
    at an even index are converted to (or left as) upper-case,
    Letters at an odd index are converted to (or left as)
    lower-case. Non-letters are ignored.
    Use: alternating = alternate_case(string)
    -------------------------------------------------------
    Parameters:
        width - maximum width in characters of triangle (int >= 1)
    Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
        alternating - the resulting string (str)
    -------------------------------------------------------
    """
    # Your code here
    i = 0
    alternating = ''

    while i < len(string):
        if string[i].isdigit()is False:
            if i % 2 == 0:
                alternating += f'{string[i].upper()}'
            else:
                alternating += f'{string[i].lower()}'
        else:
            alternating += f'{string[i]}'
        i += 1
    return alternating
