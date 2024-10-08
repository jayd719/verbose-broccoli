"""
-------------------------------------------------------
Assignment 8 Custom Functions Library
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-11-26"
-------------------------------------------------------
"""

# Imports

# Constants
UPPER_CASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

RULE1 = ['sh', 'ch']
RULE2 = ['y', 'ay', 'oy']


def add_spaces(string):
    """
    -------------------------------------------------------
    Create a new string with added space between words. Words start
    with upper-case characters.
    Use: new_string = add_spaces(string)
    -------------------------------------------------------
    Parameters:
        string - string that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is upper case. string has at least one
            character (str)
    Returns:
        new_string - new string in which the words are separated
            by spaces and only the first word starts with
            an upper case character (str)
    -------------------------------------------------------
    """
    i, j, split_indexes, words = 0, 0, [], []

    while i < len(string):
        if string[i] in UPPER_CASE_LETTERS:
            split_indexes.append(i)
        i += 1
    split_indexes.append(len(string))

    string_temp = ''
    while j + 1 < len(split_indexes):
        words.append(string[split_indexes[j]:split_indexes[j + 1]])
        string_temp = string_temp + \
            f' {string[split_indexes[j]:split_indexes[j + 1]].lower()}'
        j += 1
    new_string = f'{string_temp[1].upper()}{string_temp[2:len(string_temp)]}'
    return new_string


def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: plural = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        plural - a plural version of string (str)
    -------------------------------------------------------
    """
    if string.endswith('s') or string.endswith('sh') or string.endswith('ch'):
        plural = f'{string}es'
    elif string.endswith('y') and string.endswith('ay')is False and string.endswith('oy') is False:
        plural = string.replace('y', 'ies')
    else:
        plural = f'{string}s'
    return plural


def common_ending(string1, string2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: common = common_ending(string1, string2)
    -------------------------------------------------------
    Parameters:
        string1 - first string for ending comparison (str)
        string2 - second string for ending comparison (str)
    Returns:
        common - the longest common ending of string1 and string2 (str)
    -------------------------------------------------------
    """
    i = len(string1) - 1
    while i >= 0:
        if string1[i:len(string1)] in string2:
            common = string1[i:len(string1)]
        i -= 1
    return common


def is_valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: valid = is_valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    str = isbn.split('-')
    valid = False
    if (len(isbn) == 17) and (isbn.replace('-', '')).isdigit():
        if len(str) == 5 and (str[0] == '978' or str[0] == '979') and len(str[len(str) - 1]) == 1:
            if len(str[1]) >= 1 and len(str[2]) >= 1 and len(str[3]) >= 1:
                valid = True
    return valid


def is_word_chain(word_list):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = is_word_chain(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if word_list is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    i = 0
    while i + 1 < len(word_list):
        if word_list[i][len(word_list[i]) - 1] == word_list[i + 1][0]:
            word_chain = True
        else:
            word_chain = False
            break
        i += 1
    return word_chain
