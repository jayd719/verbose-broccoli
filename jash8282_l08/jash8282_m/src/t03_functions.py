"""
-------------------------------------------------------
Midterm B Task 3 Function Definitions
-------------------------------------------------------
Author: Jd Jashandeep Singh
ID:     169018282
Email:  jash8282@mylaurier.ca
__updated__ = "2022-11-02"
-------------------------------------------------------
"""
# Constants
# TODO: define prices for base service and extras
BASE_COST = 100.0
EXTRA_SERVICE_COST = 40.0
# TODO: define the discount rate for extra services
EXTRA_CARE_DISCOUNT = (10 / 100)  # 10%

# This information here is different here than that given on the web site.
# going with the info given here in the function


def tire_change():
    """
    -------------------------------------------------------
    Determines the cost of changing tires. The cost is made up of:
        base cost: $100.00
        cost per extra service: $40.00
        Extra Care discount 10% only if:
            more than 1 extra service purchased
            and purchaser is an Extra Care customer
    Use: cost = tire_change()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
        cost - cost of a tire change based upon the base cost,
            the number of extra services purchased, and Extra Care discount
            if applicable (float)
    -------------------------------------------------------
    """
    # your code here
    extra_services = int(input('How many extra services are you purchasing? '))
    if extra_services == 0:
        cost = BASE_COST
    elif extra_services == 1:
        cost = BASE_COST + EXTRA_SERVICE_COST
    else:
        extra_care_customer = input('Are you an Extra Care customer (Y/N)?')
        if extra_care_customer == 'Y':
            cost = (BASE_COST + (EXTRA_SERVICE_COST * extra_services)
                    ) * (1 - EXTRA_CARE_DISCOUNT)
        else:
            cost = BASE_COST + (EXTRA_SERVICE_COST * extra_services)
    return cost
