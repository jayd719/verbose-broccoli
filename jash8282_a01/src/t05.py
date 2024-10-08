"""
-------------------------------------------------------
Assignment 1, Task 5
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-10-01"
-------------------------------------------------------
"""

# Inputs
principle_amount = float(input('Principal: $'))  # p
interest = float(input('Interest (decimal): '))  # r
time = int(input('Number of years: '))  # t
# the number of times the interest is compounded per year
no_of_times = int(input('Number of times interest compounded per year: '))  # n

# Calculations
# TODO: calculate total balance
balance = principle_amount * \
    (1 + (interest / no_of_times))**(no_of_times * time)


# Output
# TODO: print out calculated balance
print('')
print(f"Balance: $ {balance}")
