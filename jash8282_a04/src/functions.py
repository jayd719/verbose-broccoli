"""
-------------------------------------------------------
Custom Functions Library- Assignment 4
-------------------------------------------------------
Author:  Jashandeep SIngh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-10-29"
-------------------------------------------------------
"""

# Imports

# Constants


def day_of_week(day_number):
    """
    -------------------------------------------------------
    Takes an integer parameter and returns a string representing the corresponding day of the week
    Use: day_name=day_of_week(day_number)
    -------------------------------------------------------
    Parameters:
        day_number - number of day (int)
    Returns:
        result - name of day/ error message if wrong parameter (str)
    ------------------------------------------------------
    """
    if day_number == 1:
        result = 'Monday'
    elif day_number == 2:
        result = 'Tuesday'
    elif day_number == 3:
        result = "Wednesday"
    elif day_number == 4:
        result = 'Thursday'
    elif day_number == 5:
        result = 'Friday'
    elif day_number == 6:
        result = 'Saturday'
    elif day_number == 7:
        result = 'Sunday'
    else:
        result = 'Error'

    return result


def pollution_level(aqi):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if aqi is negative.
    Use: level = pollution_level(aqi)
    -------------------------------------------------------
    Parameters:
        aqi - Air Quality Index (int)
    Returns:
        level - name of pollution level (str)
    ------------------------------------------------------
    """
    if aqi < 0:
        level = 'Error'
    elif aqi < 51:
        level = 'Good'
    elif aqi < 101:
        level = 'Moderate'
    elif aqi < 151:
        level = 'Unhealthy for Sensitive Groups'
    elif aqi < 201:
        level = 'Unhealthy'
    elif aqi < 300:
        level = 'Very Unhealthy'
    else:
        level = 'Hazardous'
    return level


def product_largest(v1, v2, v3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    v1, v2, and v3.
    Use: product = product_largest(v1, v2, v3)
    -------------------------------------------------------
    Parameters:
        v1 - v1 number (float)
        v2 - v1 number (float)
        v3 - v1 number (float)
    Returns:
        product - the product of the two largest values of
            v1, v2, and v3 (float)
    ------------------------------------------------------
    """

    if v1 >= v2:
        largest_one = v1
    else:
        largest_one = v2

    if v2 >= v3:
        largest_two = v2
    else:
        largest_two = v3
    if v1 >= v3:
        largest_one = v1

    product = largest_one * largest_two

    return product


def rgb_mix(rgb1, rgb2):
    """
    -------------------------------------------------------
    Determines the secondary colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: colour = rgb_mix(rgb1, rgb2)
    -------------------------------------------------------
    Parameters:
        rgb1 - a primary RGB colour (str)
        rgb2 - a primary RGB colour (str)
    Returns:
        colour - a secondary RGB colour (str)
    -------------------------------------------------------
    """
    if rgb1 == rgb2:
        color = rgb1
    # "red" + "blue": "fuchsia"
    elif (rgb1 == "red" or rgb1 == "blue") and (rgb2 == "red" or rgb2 == "blue"):
        color = "fuchsia"

    # "red" + "green": "yellow"
    elif (rgb1 == "red" or rgb1 == "green") and (rgb2 == "red" or rgb2 == "green"):
        color = "yellow"

    # "green" + "blue": "aqua"
    elif (rgb1 == "green" or rgb1 == "blue") and (rgb2 == "green" or rgb2 == "blue"):
        color = "aqua"

    else:
        color = 'Error'

    return color


def yee_ha(number):
    """
    -------------------------------------------------------
    Determines output string from a given integer
        "Yee" if number is evenly divisible by 3
        "Ha" if number is evenly divisible by 7
        "Yee Ha" if number is evenly divisible by both 3 and 7
        "Nada" if number is none of the above
    Use: result = yee_ha(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        result - result (str)
    -------------------------------------------------------
    """
    if number % 3 == 0:
        if (number % 3 == 0) and (number % 7 == 0):
            result = "Yee Ha"
        else:
            result = 'Yee'
    elif number % 7 == 0:
        result = 'Ha'

    else:
        result = "Nada"

    return result
