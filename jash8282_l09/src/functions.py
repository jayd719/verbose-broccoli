"""
-------------------------------------------------------
Custom Function Library- Lab 8
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-11-15"
-------------------------------------------------------
"""

# Imports

# Constants

SPECIAL_CHARACTERS = ["#", "@", "$", "%", "&", "!"]
VOWELS = 'AEIOU'
OPERATORS = ['+', '-', '*', '/', '%']

LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Parameters:
        chemical - a chemical formula (str)
    Returns:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """
    return chemical.endswith('OH')


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:]
    return pc, pi, pq


def count_special_chars(s):
    """
    -------------------------------------------------------
    Counts the number of special characters in s.
    The special characters are: "#", "@", "$", "%", "&", "!".
    Use: count = count_special_chars(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - number of special characters in s (int)
    ------------------------------------------------------
    """
    count = 0
    for char in s:
        if char in SPECIAL_CHARACTERS:
            count += 1

    return count


def dsmvwl(string):
    """
    -------------------------------------------------------
    Disemvowels a string. Returns a copy of s with all the vowels
    removed. Y is not treated as a vowel. Preserves case.
    Use: out = dsmvwl(sstring)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        out - string with its vowels removed (str)
    -------------------------------------------------------
    """
    out = ''
    for alpha in string:
        if alpha.upper() not in VOWELS:
            out += alpha
    return out


def total_digits(string):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in string.
    Use: total = total_digits(string)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in string (int)
    ------------------------------------------------------
    """
    i, total = 0, 0
    while i < len(string):
        if string[i].isdigit():
            total += int(string[i])
        i += 1
    return total


def str_distance(s1, s2):
    """
    -------------------------------------------------------
    Finds the distance between the s1 and s2. The distance between two
    strings of the same length is the number of positions in the strings
    at which their characters are different. If two strings are not the
    same length, the distance is unknown (-1). If the distance is zero,
    then two strings are equal.
    Use: d = str_distance(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - first string (str)
        s2 - second string (str)
    Returns:
        d - the distance between s1 and s2 (int)
    ------------------------------------------------------
    """
    d = 0
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                d += 1
    else:
        d = -1
    return d


def calculate(expr):
    """
    -----------------------------------------------------------------
    Treats expr as a math expression and evaluates it.
    expr must have the following format:
        operand1 operator operand2
    operators are: +, -, *, /, %
    operands are one-digit integer numbers
    Return None if second operand is zero for division.
    Use: result = calculate(expr)
    -----------------------------------------------------------------
    Parameters:
        expr - an arithmetic expression to be calculated (str)
    Returns:
        result - The result of arithmetic expression (float)
    -----------------------------------------------------------------
    """
    digits = []
    for each in expr:
        if each.isdigit():
            digits.append(int(each))
        elif each in OPERATORS:
            operator = each
        else:
            pass

    if operator == '+':
        result = digits[0] + digits[1]
    elif operator == '-':
        result = digits[0] - digits[1]
    elif operator == '*':
        result = digits[0] * digits[1]
    elif operator == '/':
        if digits[1] == 0:
            result = None
        else:
            result = digits[0] / digits[1]
    elif operator == '%':
        if digits[1] == 0:
            result = None
        else:
            result = digits[0] % digits[1]
    return result


def comma_period_replace(string):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        out - string with all commas replaced by a period (str)
    ------------------------------------------------------
    """
    return string.replace(',', '.')


def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    uppr, lowr, dgts, whtspc = 0, 0, 0, 0
    for each in txt:
        if each in LETTERS:
            lowr += 1
        elif each in LETTERS.upper():
            uppr += 1
        elif each.isdigit():
            dgts += 1
        elif each == ' ':
            whtspc += 1
    return uppr, lowr, dgts, whtspc


def digit_count(s):
    """
    -------------------------------------------------------
    Counts the number of digits in a string.
    Use: count = digit_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of digits in s (int)
    -------------------------------------------------------
    """
    i, count = 0, 0
    while i < len(s):
        if s[i].isdigit():
            count += 1
        i += 1
    return count


def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
    count = 0
    for each in s:
        if each.upper() in VOWELS:
            count += 1
    return count
