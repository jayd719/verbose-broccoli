"""
-------------------------------------------------------
Exam Task 4 Function Definitions
Fall 2022
-------------------------------------------------------
Author: Jd Jashandeep Singh
ID:     169018282
Email:  jash8282@mylaurier.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""


def wide_triangle(width):
    """
    -------------------------------------------------------
    Prints a triangle in which each succeeding line is 3 characters
    longer than the previous line.
    Use: wide_triangle(width)
    -------------------------------------------------------
    Parameters:
        width - maximum width in characters of triangle (int >= 1)
    Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
        None
    -------------------------------------------------------
    """

    # Your code here
    lines = []
    org_width = width
    while width > 0:
        width -= 3
        lines.append(width)

    lines.sort()
    lines.pop(0)
    lines.append(org_width)

    if len(lines) > 1:
        for each in lines:
            print('#' * each)
        for i in range((len(lines) - 2), -1, -1):
            print('#' * lines[i])

    return None
