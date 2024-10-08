"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-10-07"
-------------------------------------------------------
"""

# Imports

# Constants

# Inputs
foundation_len = float(input('Foundation length (m): '))
foundation_width = float(input('Foundation width (m): '))
foundation_height = float(input('Foundation height (m): '))
wall_height = float(input('Wall height (m): '))
concrete_cost = float(input('Cost of concrete ($/m^3): '))
brick_cost = float(input('Cost of bricks ($/m^2): '))

# Calculations
# TODO: Calculate concrete needed for foundation
concrete_needed = foundation_len * foundation_width * foundation_height

# TODO: Calculate cost of concrete
cost_of_concrete = concrete_needed * concrete_cost

# TODO: Calculate Brick needed for wall
bricks_needed = 2 * (foundation_len * wall_height +
                     wall_height * foundation_width)

# TODO: Calculate Cost of Bricks
cost_of_bricks = bricks_needed * brick_cost

# TODO:Calculate Total Cost
total_cost = cost_of_concrete + cost_of_bricks


# Output
# TODO: print out calculated results
print(f"""
Concrete needed for foundation (m^3): {concrete_needed:.2f}
Cost of concrete: ${cost_of_concrete:,.2f}
Bricks needed for walls (m^2): {bricks_needed:.2f}
Cost of bricks: ${cost_of_bricks:,.2f}
Total cost: ${total_cost:,.2f}
""")
