"""
-------------------------------------------------------
Assigment 3, Task 4
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-10-23"
-------------------------------------------------------
"""

# Imports
from functions import multiply_fractions

# Input
# TODO: prompt user to enter Num and den for fractions.
num1 = int(input('Numerator 1: '))
denom1 = int(input('Denominator 1: '))
num2 = int(input('Numerator 2: '))
denom2 = int(input('Denominator 2: '))

# Calculations
# Calculate product.
numerator, denominator, product = multiply_fractions(
    num1, denom1, num2, denom2)

# Output
# TODO: print out calculated result
print('')
print(f'Result: {numerator}/{denominator} = {product:.3f}')
