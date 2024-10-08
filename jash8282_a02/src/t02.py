"""
-------------------------------------------------------
Assignment 2, Task 2
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-10-08"
-------------------------------------------------------
"""

# Inputs
number = int(input('Enter a positive digit number: '))

# Calculations
# TODO: extract digits from given integer
first_digit = number % 10
second_digit = number // 10

# TODO: Calculate product of two digits of given integer.
product = first_digit * second_digit

# Output
# TODO: print out calculated result
print('')
print(f'The product of the digits of {number} is {product}')
