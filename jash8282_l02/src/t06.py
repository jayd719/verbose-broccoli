"""
-------------------------------------------------------
Calculate the monthly payment for a mortgage
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-09-20"
-------------------------------------------------------
"""

# Constants
# TODO: define months in an year
MONTHS_IN_YEAR = 12

# Inputs
mortage_principle = int(input("Mortgage principal ($):"))
no_of_years = int(input('Number of years:'))
yearly_interest_rate = float(input('Yearly interest rate (%):'))

# Calculations
# TODO: Calculate number of months
no_of_months = no_of_years * MONTHS_IN_YEAR

# TODO: Convert decimal value into percentage
yearly_interest_rate = yearly_interest_rate / 100

# TODO: calculate monthly interest rate
monthly_interest_rate = yearly_interest_rate / MONTHS_IN_YEAR

# TODO: Calculate Total Number Of Payments
total_no_payments = no_of_years * MONTHS_IN_YEAR

# TODO: Calculate Monthly Payments

monthly_payment = mortage_principle * (((monthly_interest_rate * (((1 + monthly_interest_rate)
                                                                   ** total_no_payments)))) / ((((1 + monthly_interest_rate) ** total_no_payments)) - 1))

# outputs
print()
print(monthly_payment)
