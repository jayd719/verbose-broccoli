"""
-------------------------------------------------------
Custom Function Library- Lab 5
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-10-18"
-------------------------------------------------------
"""


# Imports

# Constants
OVERTIME_RATE = 1.5
TAX_RATE = 3.625
OVER_TIME_HOURS = 40

MIN_SALARY = 30000
MIN_YEARS = 5

INFANT_AGE = 3
SENIOR_AGE = 65
STUDENT_AGE = 10
ADULT_AGE = 18


def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """
    # TODO: Check if day times month equal to year
    if (day * month) == year:
        magic = True
    else:
        magic = False

    return magic


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    # TODO: Calculate distance of both values from target.
    distance_v1 = v1 - target
    distance_v2 = v2 - target

    # TODO: compare the two calculated distances.
    if abs(distance_v1) <= abs(distance_v2):
        result = v1
    else:
        result = v2

    return result


def get_pay(hourly_rate, hours_worked):
    """
    -------------------------------------------------------
    Calculates an employee's net wage given hours and pay.
    Each employee is paid 1.5 times their regular hourly rate for
    all hours over 40. A tax amount of 3.625 percent of gross salary
    is deducted.
    Use: net_payment = get_pay(hourly_rate, hours_worked)
    -------------------------------------------------------
    Parameters:
        hourly_rate - hourly rate of pay (float)
        hours_worked - total hours worked (float)
    Returns:
        net_payment - description (float)
    ------------------------------------------------------
    """
    # Calculations
    # TODO: Calculate sub total based on number of hours worked
    if hours_worked > OVER_TIME_HOURS:
        sub_total = (OVER_TIME_HOURS * hourly_rate) + \
            ((hours_worked - OVER_TIME_HOURS) * OVERTIME_RATE * hourly_rate)
    else:
        sub_total = hours_worked * hourly_rate

    # TODO: Calculate Net Pay.
    net_payment = sub_total - (sub_total * (TAX_RATE / 100))

    return net_payment


def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    # Input
    years_worked = int(input('Years employed: '))

    qualified = False
    # TODO: Check if user qualifies or load or not
    if years_worked >= MIN_YEARS:
        annual_salary = int(input('Annual salary: '))
        if annual_salary >= MIN_SALARY:
            qualified = True
    else:
        qualified = False

    return qualified


def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    # Input
    # TODO: Ask user their age
    age = int(input('How old are you? '))

    if age < INFANT_AGE:
        price = 0
    elif age >= SENIOR_AGE:
        price = 4
    elif(age >= STUDENT_AGE) and (age < ADULT_AGE):
        user_input = input('Are You Student of this School? Y/N  ')
        if user_input == "Y":
            price = 1
        else:
            price = 3
    elif age >= ADULT_AGE and age < SENIOR_AGE:
        price = 5
    else:
        price = 2

    return price
