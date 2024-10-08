"""
-------------------------------------------------------
Midterm B Task 4 Function Definitions
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-10-29"
-------------------------------------------------------
"""


def yes_no(response):
    """
    DO NOT CHANGE THE CONTENTS OF THIS FUNCTION
    -------------------------------------------------------
    Determines whether an response is 'Y' (for Yes), 'N' (for No),
    or any other response.
    Use: answer = yes_no(response)
    -------------------------------------------------------
    Parameters:
        response - a response to categorize (str)
    Returns:
        answer - whether value is 'Y', 'N', or otherwise (str)
    -------------------------------------------------------
    """
    if response == 'Y':
        answer = 'Yes'
    elif response == 'N':
        answer = 'No'
    else:
        answer = 'unknown'
    return answer
