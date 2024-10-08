"""
-------------------------------------------------------
Custom Functions library Lab 11
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-11-30"
-------------------------------------------------------
"""

# Imports
from random import randint, uniform

# Constants
CHARS = 'abcdefghijklmnopqrstuvwxyz'


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []

    for row in range(rows):
        row = []
        for col in range(cols):
            if value_type == 'float':
                row.append(uniform(low, high))
            else:
                row.append(randint(low, high))
        matrix.append(row)

    return matrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    print("  ", end='')
    for i in range(len(matrix[0])):
        print(f'{i:7d}', end='')
    print()
    for row in range(len(matrix)):
        print(f'{row:2d}', end='')
        for col in range(len(matrix[0])):
            if value_type == 'float':
                print(f'{matrix[row][col]:7.2f}', end='')
            else:
                print(f'{matrix[row][col]:7d}', end='')
        print()

    return None


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    matrix = []
    i = 0
    while i < rows:
        row, j = [], 0
        while j < cols:
            row.append(CHARS[randint(0, (len(CHARS) - 1))])
            j += 1
        matrix.append(row)
        i += 1

    return matrix


def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """
    print("  ", end='')
    for i in range(len(matrix[0])):
        print(f'{i:>4d}', end='')
    print()

    for row in range(len(matrix)):
        print(f' {row:<4d}', end='')
        for col in range(len(matrix[0])):
            print(f'{matrix[row][col]:>4s}', end='')
        if row != len(matrix) - 1:
            print()

    return None


def find_less(matrix, n):
    """
    -------------------------------------------------------
    Finds the location [row, column] of the first value in matrix
    that is smaller than a target value, n. If there is no such
    number in matrix, it should return an empty list.
    Use: loc = find_less(matrix, n)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
        n - the target value (float)
    Returns:
        loc - a list of the row and column location of
            the first value smaller than n in values,
            an empty list otherwise (list of int)
    -------------------------------------------------------
    """
    loc = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < n:
                loc = i, j
                break
    return list(loc)


def find_word_diagonal(matrix, word):
    """
    -------------------------------------------------------
    Returns whether word is on the diagonal of a square matrix
    of characters.
    Use: found = find_word_diagonal(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - a 2d list of characters (2d list of str)
        word - the word to compare against the diagonal of matrix (str)
    Returns:
        found - True if word is on the diagonal of matrix,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    found = False
    check_word = ''
    for i in range(len(matrix)):
        check_word = f'{check_word}{matrix[i][i]}'

    if check_word == word:
        found = True

    return found


def matrix_equal(matrix1, matrix2):
    """
    -------------------------------------------------------
    Compares two matrices to see if they are equal - i.e. have the
    same contents in the same locations.
    Use: equal = matrix_equal(matrix1, matrix2)
    -------------------------------------------------------
    Parameters:
        matrix1 - the first matrix (2D list of *)
        matrix2 - the second matrix (2D list of *)
    Returns:
        equal - True if matrix1 and matrix2 are equal,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    equal = True
    i = 0
    if len(matrix1) == len(matrix2):
        while i < len(matrix1):
            j = 0
            while j < len(matrix1[i]):
                if matrix1[i][j] != matrix2[i][j]:
                    equal = False
                    break
                j += 1
            i += 1
    else:
        equal = False

    return equal
