"""
-------------------------------------------------------
Determine the cost of producing an open-top cylindrical container
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-09-20"
-------------------------------------------------------
"""
# Constants
# TODO: Define PI
PI = 3.14

# inputs
diameter_of_base = float(input('Diameter of container base (cm):'))
height_of_container = float(input('Height of container (cm):'))
cost_of_material = float(input('Cost of material ($/cm^2):'))
no_of_containers = int(input('Number of containers:'))

# Calculations
# TODO: calculate radius of base
radius = diameter_of_base / 2

# TODO: calculate area of base
area_of_base = PI * radius**2

# TODO: Calculate area of outside
outside_area = 2 * PI * radius * height_of_container

# TODO: Calculate Total Area
total_area = area_of_base + outside_area

# TODO: Calculate cost per unit
cost_per_unit = total_area * cost_of_material

# TODO: Calculate cost for all containers
cost_all_containers = no_of_containers * cost_per_unit


# Outputs
print('The total cost of one containers is $', cost_per_unit)
print('The total cost of all containers is $', cost_all_containers)
