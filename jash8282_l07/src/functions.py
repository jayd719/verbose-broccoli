"""
-------------------------------------------------------
Custom Function Library Lab 7
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-11-02"
-------------------------------------------------------
"""

# Imports
from random import randint

# Constants


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)
    count = 0
    user_input = None
    while user_input != number:
        user_input = int(input('Guess: '))
        if user_input > number:
            print('Too high, try again.')
        elif user_input < number:
            print('Too low, try again.')
        count += 1
    print('Congratulations - good guess!')

    return count


def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    square = 0
    number = 1
    final = 0
    while final <= target:
        square = number * number
        final += square
        number += 1
    return final


def num_categories():
    """
    -------------------------------------------------------
    Asks a user to enter a series of numbers, then counts and returns
    how may positives, negatives, and zeroes there are.
    Stop processing values when the user enters -999.
    Use: negatives, zeroes, positives = num_categories()
    -------------------------------------------------------
    Returns:
        negatives - number of negative values (int)
        zeroes - number of zero values (int)
        positives - number of positive values (int)
    ------------------------------------------------------
    """

    user_input = int(input('First value: '))
    negatives, zeroes, positives = 0, 0, 0
    while user_input != -999:
        if user_input < 0:
            negatives += 1
        elif user_input > 0:
            positives += 1
        else:
            zeroes += 1
        user_input = int(input('Next value: '))

    return negatives, zeroes, positives


def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    away_for_another_day = 'Y'
    day = 1
    b_total, l_total, s_total, a_total = 0, 0, 0, 0

    while away_for_another_day == 'Y':
        print(f'For Day {day}\n')

        breakfast_cost = float(input('How much was breakfast?'))
        b_total += breakfast_cost

        lunch_cost = float(input('How much was lunch?'))
        l_total += lunch_cost

        supper_cost = float(input('How much was supper?'))
        s_total += supper_cost

        day_total = breakfast_cost + lunch_cost + supper_cost
        a_total += day_total

        print(f'Your total for the day was ${day_total}\n')
        away_for_another_day = input('Were you away another day (Y/N)?')
        day += 1
        print('')
    return b_total, l_total, s_total, a_total


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    value = int(input(f'Enter a value between {low} and high {high}: '))

    while (value < low) or (value > high):
        if value < low:
            value_entered = 'low'
        elif value > high:
            value_entered = 'high'
        print(f'Value entered is too {value_entered}')
        value = int(input(f'Enter a value between {low} and high {high}: '))

    return value
