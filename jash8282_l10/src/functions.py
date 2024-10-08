"""
-------------------------------------------------------
Custom Functions Library Lab 10
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-11-22"
-------------------------------------------------------
"""

# Imports


def customer_by_id(fh, id_number):
    """
    -------------------------------------------------------
    Find the record for a given ID in a sequential file.
    Use: result = customer_by_id(fh, id_number)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        id_number - the id_number to match (str)
    Returns:
        result - the record with id_number if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    result, line = [], '-'
    while line != "":
        line = fh.readline()
        customer_info = line.strip().split(',')
        print(customer_info)
        if customer_info[0] == id_number:
            result = customer_info

    return result


def customer_first(fh):
    """
    -------------------------------------------------------
    Find the customer with the earliest sign-up date.
    Assumes file is not empty.
    Use: result = customer_first(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the earliest sign-in date (list)
    -------------------------------------------------------
    """
    date, line = '9999-12-31', '-'
    result = 1
    while line != '':
        line = fh.readline()
        customer_info = line.strip().split(',')
        if len(customer_info) > 1:
            if customer_info[4] < date:
                date = customer_info[4]
                result = customer_info
    return result


def count_frequency_value(fh, value):
    """
    -------------------------------------------------------
    Counts the number of appearances of value in fh.
    Use: count = count_frequency_value(fh, value)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        value - the value to count (int)
    Returns:
        count - the number of appearance of value in fh (int)
    ------------------------------------------------------
    """
    count = 0
    for line in fh:
        line = line.strip()
        if int(line) == value:
            count += 1
    return count


def find_shortest(fh):
    """
    -------------------------------------------------------
    Finds the first word with shortest length in fh.
    Assumes file is not empty.
    Use: word = find_shortest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the first word with the shortest length in fh (str)
    ------------------------------------------------------
    """
    line = fh.readline().strip()
    shortest_word = line
    while line != '':
        line = fh.readline().strip()
        if len(line) < len(shortest_word):
            return shortest_word


def file_copy_n(fh_1, fh_2, n):
    """
    -------------------------------------------------------
    Copies n record from fh_1 (starting from the beginning of the file) to fh2
    Use: file_copy_n(fh_1, fh_2, n)
    -------------------------------------------------------
    Parameters:
        fh_1 - file to search (file handle - already open for reading)
        fh_2 - file to search (file handle - already open for appending)
        n - number of lines to copy from fh_1 to fh_2
    Returns:
        None
    ------------------------------------------------------
    """
    i = 0
    while i < int(n):
        line = fh_1.readline()
        fh_2.write(line)
        i += 1

    return None
