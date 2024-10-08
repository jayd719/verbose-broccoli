"""
-------------------------------------------------------
Custom Functions Library Assignment 7
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-11-20"
-------------------------------------------------------
"""

# Imports


def list_factors(num):
    i, factors = 1, []
    while i < num:
        if num % i == 0:
            factors.append(i)
        i += 1
    return factors


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: numbers = list_positives()
    -------------------------------------------------------
    Returns:
        numbers - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    user_input, numbers = None, []
    while user_input != 0:
        user_input = int(input('Enter a positive number: '))
        if user_input > 0:
            numbers.append(user_input)
    return numbers


def list_indexes(values, target):
    """
    -------------------------------------------------------
    Finds the indexes of target in values.
    Use: indexes = list_indexes(values, target)
    -------------------------------------------------------
    Parameters:
        values - list of value (list of int)
        target - value to look for in num_list (int)
    Returns:
        locations - list of indexes of target (list of int)
    -------------------------------------------------------
    """
    indexes = []
    for i in range(len(values)):
        if values[i] == target:
            indexes.append(i)
    return indexes


def subtract_lists(minuend, subtrahend):
    """
    -------------------------------------------------------
    Updates the list minuend removing from it the values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are not included in the updated list.
    subtrahend is unchanged
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to remove from minuend (list)
    Returns:
        None
    ------------------------------------------------------
    """
    indexes, j = [], 0
    for i in range(len(minuend)):
        if minuend[i] in subtrahend:
            indexes.append(i)
    for index in indexes:
        minuend.pop(int(f"{index-j}"))
        j += 1
    return None


def is_sorted(values):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = is_sorted(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list)
    Returns:
        in_order - True if values is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    i = 0
    while (i + 1) < len(values):
        if values[i] < values[i + 1]:
            in_order = True
            index = -1
        else:
            in_order = False
            index = i
        i += 1
    return in_order, index
