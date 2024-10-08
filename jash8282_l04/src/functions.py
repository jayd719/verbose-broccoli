"""
-------------------------------------------------------
Custom Function Library
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-10-04"
-------------------------------------------------------
"""

# Imports
from math import sqrt


# Constants
# TODO:define value of PI
PI = 3.141592653589793238

# TODO: define freezing point of water
WATER_FREEZING_POINT = 32

# TODO: define conversion factor from c to f
CONV_FACTOR = (9 / 5)

# TODO: define seconds in day
SECONDS_IN_DAY = 60 * 60 * 24

# TODO: define seconds in hour
SECONDS_IN_HOUR = 60 * 60


# TODO: define seconds in minutes
SECONDS_IN_MINUTE = 60


def area(radius):
    """
    -------------------------------------------------------
    Calculates and returns area of a circle.
    Use: ar = area(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        ar - area of a circle (float)
    ------------------------------------------------------
    """
    # Calculations
    # TODO: Calculate area of circle
    ar = PI * radius ** 2

    return ar


def pythag(s1, s2):
    """
    -------------------------------------------------------
    Calculates and returns the radius, diameter, circumference,
    and area of circle defined by a right triangle.
    Use: radius, diam, circ, area = pythag(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - length of side 1 of a right triangle (float > 0)
        s2 - length of side 2 of a right triangle (float > 0)
    Returns:
        radius - radius of the resulting circle (float)
        diam - diameter of the resulting circle (float)
        circ - circumference of the resulting circle (float)
        area - area of the resulting circle (float)
    ------------------------------------------------------
    """
    # Calculations
    # TODO: Calculate Radius of Circle
    radius = sqrt((s1**2 + s2**2))

    # TODO: Calculate Diameter of circle
    diam = 2 * radius

    # TODO: Calculate circumference of circle
    circ = 2 * PI * radius

    # TODO: Calculate Area of Circle
    area = PI * radius**2

    return radius, diam, circ, area


def fraction_product(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = fraction_product(num1, den1, num2, den2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of first fraction (int)
        den1 - denominator of first fraction (int != 0)
        num2 - numerator of second fraction (int)
        den2 - denominator of second fraction (int != 0)
    Returns:
        num - numerator of product (int)
        den - denominator of product (int)
        product - num / den (float)
    -------------------------------------------------------
    """
    # Calculations
    # TODO: Calculate numerator of product
    num = num1 * num2

    # TODO: Calculate denominator of product
    den = den1 * den2

    # TODO: calculate num/den
    product = num / den

    return num, den, product


def c_to_f(celsius):
    """
    -------------------------------------------------------
    Converts temperatures in celsius to fahrenheit.
    Use: fahrenheit = c_to_f(celsius)
    -------------------------------------------------------
    Parameters:
        celsius - temperature in celsius (int >= -273)
    Returns:
        fahrenheit - equivalent to celsius (float)
    -------------------------------------------------------
    """
    # Calculations
    # TODO: convert celsius to fahrenheit
    fahrenheit = (CONV_FACTOR * celsius) + WATER_FREEZING_POINT

    return fahrenheit


def time_split(initial_seconds):
    """
    -------------------------------------------------------
    Converts total seconds into days, hours, minutes, and seconds.
    Use: days, hours, minutes, seconds = time_split(initial_seconds)
    -------------------------------------------------------
    Parameters:
        initial_seconds - time elapsed (int >= 0)
    Returns:
        days - number of days in initial_seconds (int)
        hours - remaining hours in initial_seconds (int)
        minutes - remaining minutes in initial_seconds (int)
        seconds - remaining seconds in initial_seconds (int)
    -------------------------------------------------------
    """
    # Calculations
    # TODO: Calculate Days
    days = initial_seconds // SECONDS_IN_DAY

    # TODO: Calculate Hours
    hours = ((initial_seconds - (days * SECONDS_IN_DAY)) // SECONDS_IN_HOUR)

    # TODO: Calculate Minutes
    minutes = (initial_seconds - (days * SECONDS_IN_DAY) -
               (hours * SECONDS_IN_HOUR)) // SECONDS_IN_MINUTE

    # TODO: Calculate Seconds
    # seconds = initial_seconds - \
    #   (days * SECONDS_IN_DAY) - (hours * SECONDS_IN_HOUR) - \
    #  (minutes * SECONDS_IN_MINUTE)
    seconds = initial_seconds % SECONDS_IN_MINUTE

    return days, hours, minutes, seconds
