"""
-------------------------------------------------------
Assignment 1, Task 1
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-10-07"
-------------------------------------------------------
"""

# Imports

# Constants
# TODO: Define annual tax rate
ANNUAL_TAX_RATE = 18.5  # %

# Inputs
total_sales = float(input('Enter the total sales: $'))

# Calculations
# TODO: Calculate tax amount
tax = total_sales * (ANNUAL_TAX_RATE / 100)

# Output
# TODO: print out projected tax report
print('')
print('Projected Tax Report')
print('--------------------------')
print(f'Total sales:   $ {total_sales:,.2f}')
print(f'Annual tax:    % {ANNUAL_TAX_RATE}')
print('--------------------------')
print(f'Tax:           $  {tax:,.2f}')
