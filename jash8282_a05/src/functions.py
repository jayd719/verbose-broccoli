"""
-------------------------------------------------------
Custom Function Library Assignment 5
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-11-05"
-------------------------------------------------------
"""

# Imports

# Constants
FIRST_VALUE = 5


def factorial(num):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of num.
    Use: product = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - number to factorial (int > 0)
    Returns:
        product - num! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(num, 1, - 1):
        product = product * i
    return product


def calories_burned(per_minute, minutes):
    """
    -------------------------------------------------------
    Calculates and returns calories burned every five minutes for 
    given the number of calories burned per minute an for the total 
    number of minutes run
    Use:calories_burned(per_minute, minutes)
    -------------------------------------------------------
    Parameters:
        per_minute - the number of calories burned per minute(float > 0)
        minutes    - total number of minutes run(int>0)
    Returns:
       None
    ------------------------------------------------------
    """
    for i in range(FIRST_VALUE, minutes + 1, 5):
        print(f'{i:>3}:  {i*per_minute:>6.1f}')
    return None


def open_triangle(num_rows):
    """
    Prints a triangle of # characters with an empty center
    Use: open_triangle(num_rows)
    -------------------------------------------------------
    Parameters:
        num_rows - number of rows of triangle(int > 0)
    Returns:
       None
    ------------------------------------------------------
    """
    for i in range(num_rows):
        print(f'#{" "*i}#')
    return None


def multiplication_table(start, stop):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start to stop.
    Use: multiplication_table(start, stop)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        stop - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f'{"":>5s}', end='')
    for m in range(start, stop + 1):
        print(f'{m:>5d}', end='')
    print(f'\n{"":>5s}{"-----"*(stop-1)}')
    for i in range(start, (stop + 1)):
        print(f' {i:>2d} |', end='')
        for j in range(start, (stop + 1)):
            print(f' {i*j:>4d}', end='')
        print('')
    return None


def range_total(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start by increment.
    Use: total = range_total(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(start, (start * count) + 1, increment):
        total += i
    return total
