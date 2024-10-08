"""
-------------------------------------------------------
Exam Task 5 Function Definitions
Fall 2022
-------------------------------------------------------
Author: Jd Jashandeep Singh
ID:     169018282
Email:  jash8282@mylaurier.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""


def sparse_matrix(fh_in):
    """
    -------------------------------------------------------
    Creates a sparse matrix 2D list.
    Use: matrix = sparse_matrix(fh_in)
    -------------------------------------------------------
    Parameters:
        fh_in - the matrix file to process (file handle - already open for reading)
    Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
        matrix - a 2D list of the form:
            [ [row, col, value], [row, col, value], ... ] (2D list of int)
    -------------------------------------------------------
    """

    # Your code here
    matrix = []
    row = 0
    for line in fh_in:
        data = line.strip().split(',')
        i = 0
        while i < len(data):
            if int(data[i]) != 0:
                info = [row, i, data[i]]
                matrix.append(info)
            i += 1
        row += 1

    return matrix
