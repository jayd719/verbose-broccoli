"""
-------------------------------------------------------
Exam Task 2 Function Definitions
Fall 2022
-------------------------------------------------------
Author: Jashandeep Singh
ID:     169018282
Email:  jash8282@mylaurier.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""
# Constants
SENTNAL_VALUE = -500
HOT_DAY_LIMIT = 28
PLEASENT_DAY_LIMIT = 27
COLD_DAY_LIMIT = 15

# Your constants here


def temperatures():
    """
    -------------------------------------------------------
    Asks the user for daily high temperatures (in Celsius) from the keyboard.
    The function stops asking for temperatures when the user enters -500.
    The function returns:
        the total number of hot days (temperatures 28 or higher)
        the total number of pleasant days (temperatures 16 - 27)
        the total number of cold days (temperatures 15 or lower)
        the average temperature for all days (rounted down)
    Do all inputs and calculations in integer.
    Use: cold_days, pleasant_days, hot_days, avg_temp = temperatures()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
        cold_days - number of cold days (int)
        pleasant_days - number of pleasant days (int)
        hot_days - number of hot days (int)
        avg_temp - average temperature of all days (int)
    -------------------------------------------------------
    """
    # Your code here
    cold_days, pleasant_days, hot_days, count, temp = 0, 0, 0, 0, 0
    user_input = int(input('Temperature C (-500 to stop): '))

    while user_input != SENTNAL_VALUE:
        count += 1
        temp += user_input
        if user_input <= COLD_DAY_LIMIT:
            cold_days += 1
        elif user_input < PLEASENT_DAY_LIMIT:
            pleasant_days = +1
        else:
            hot_days = +1
        user_input = int(input('Temperature C (-500 to stop): '))
    avg_temp = temp / count
    return cold_days, pleasant_days, hot_days, avg_temp
