"""
-------------------------------------------------------
Exam Task 6 Function Definitions
Fall 2022
-------------------------------------------------------
Author: Jd Jashandeep Singh
ID:     169018282
Email:  jash8282@mylaurier.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""


def rotate_list(values, n):
    """
    -------------------------------------------------------
    Rotates the elements in values n places:
        A positive n rotates elements from the front to the rear of values.
        A negative n rotates elements from the rear to the front of values.
    Use: rotate_list(values, n)
    -------------------------------------------------------
    Parameters:
        values - list of elements to rotate (list of *)
        n - number of places to rotate values (int)
    Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
        None
    -------------------------------------------------------
    """
    # Your code here

    if n != 0:
        if n > 0:
            list1 = values[:n]
            list2 = values[n:]
            new_list = list2 + list1
        else:
            n = abs(n)
            list1 = values[n + 1:]
            list2 = values[:n + 1]
            new_list = list1 + list2

    else:
        new_list = values

    return new_list
