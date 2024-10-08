"""
-------------------------------------------------------
Custom Functions Library- Assignment 6
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-11-12"
-------------------------------------------------------
"""

# Imports

# Constants
TEAM_1 = 'blue'
TEAM_2 = 'grey'


def winner():
    """
    -------------------------------------------------------
    Determines how  many times string appears in user input.
    Use: results = winner()
    -------------------------------------------------------
    Parameters:

    Returns:
        count_blue - how many times string blue appeared. (int)
        count_grey - how many times string grey appeared. (int)
    ------------------------------------------------------
    """
    user_input, count_blue, count_grey = 0, 0, 0
    while user_input != '':
        user_input = input('Enter the winning team: ')
        if user_input == TEAM_1:
            count_blue += 1
        elif user_input == TEAM_2:
            count_grey += 1
        else:
            pass
    return count_blue, count_grey


def is_prime(num):
    """
    -------------------------------------------------------
    Determines if num is a prime number.
    Use: prime = is_prime(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        prime - True if num is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    i = 2
    prime = True
    while i < num:
        if num % i == 0:
            prime = False
            break
        i += 1

    return prime


def interest_table(principal, rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        principal - original value of a loan (float > 0)
        rate - yearly interest rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f'Principal:   ${principal:.2f}')
    print(f'Interest rate : {rate:.2f}%')
    print(f'Monthly payment: ${payment:.2f}')
    print('-' * 34)
    print(f'Month Interest   Payment   Balance')
    print('-' * 34)

    balance = principal
    month = 1
    while balance > 0:
        interest_paid_monthly = balance * ((rate / 100) / 12)
        if balance < payment:
            payment = balance + interest_paid_monthly

        balance = balance + interest_paid_monthly - payment

        print(
            f'{month:>5d} {interest_paid_monthly:>8.2f} {payment:>9.2f} {balance:>9.2f}')
        month += 1
    return None


def digit_count(num):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: count = digit_count(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int)
    Returns:
        count - the number of digits in num (int)
    ------------------------------------------------------
    """
    digits = 0
    while num > 0:
        num = num // 10
        digits += 1
    return digits


def sum_factors(num):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int >= 1)
    Returns:
        total - the total of num's factors (int)
    ------------------------------------------------------
    """
    total = 0
    i = 1
    while i < num:
        if num % i == 0:
            total += i
        i += 1
    return total
