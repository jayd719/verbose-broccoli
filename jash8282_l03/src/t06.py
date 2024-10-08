"""
-------------------------------------------------------
Lab 3, Task 6
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-09-27"
-------------------------------------------------------
"""
# Inputs
cost = float(input('Enter cost: $'))
quantity = int(input('Enter quantity: '))


# Calculations
# TODO: Calculate total cost
total_cost = cost * quantity

# Output
print(
    f'Given a cost of ${cost:.2f} and a quantity of {quantity} the total is ${total_cost:.2f}')
