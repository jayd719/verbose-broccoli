"""
-------------------------------------------------------
Custom Functions Library Assignment 9
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   jash8282@mylaurier.ca
__updated__ = "2022-12-03"
-------------------------------------------------------
"""

# Imports

# Constants

LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def file_head(fh, linecount):
    """
    -------------------------------------------------------
    Prints first linecount lines of fh. Line numbering starts at 0.
    If length of file is shorter than linecount, stops printing after
    last line of file.
    Use: file_head(fh, linecount)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
        linecount - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    line = None
    lines = 0
    while line != '' and lines < linecount:
        line = fh.readline().strip()
        print(line)
        lines = lines + 1

    return None


def file_integers(fh):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: numbers = file_integers(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process ( (file handle - open for reading)
    Returns:
        numbers - a list of integers from fh (list of int)
    -------------------------------------------------------
    """
    numbers = []
    for line in fh:
        contents = line.strip().split(',')
        for each in contents:
            if each.isdigit():
                numbers.append(int(each))

    return numbers


def file_stats(fh):
    """
    -------------------------------------------------------
    Evaluates the contents of a file.
    Use: ucount, lcount, dcount, wcount = file_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        ucount - The number of uppercase letters in the file (int)
        lcount - The number of lowercase letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of whitespace characters in the file (int)
    -------------------------------------------------------
    """
    content = fh.read()
    ucount, lcount, dcount, wcount = 0, 0, 0, 0
    for char in content:
        if char in LETTERS.upper():
            ucount += 1
        elif char in LETTERS:
            lcount += 1
        elif char.isdigit():
            dcount += 1
        elif char == ' ':
            wcount += 1

    return ucount, lcount, dcount, wcount


def number_lines(fh_in, fh_out):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_out contain contents
    of fh_in where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: number_lines(fh_in, fh_out)
    -------------------------------------------------------
    Parameters:
        fh_in - file to read (file - open for reading)
        fh_out - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    j = 0
    for line in fh_in:
        fh_out.write(f'[{j}] {line}')
        j += 1

    return None


def student_info(students):
    """
    -------------------------------------------------------
    Get information from a file of students and grades.
    Use: l_id, h_id, avg =student_info(students)
    -------------------------------------------------------
    Parameters:
        students - student_no information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    line = None
    l_id = None
    h_id = None

    highest, lowest, student_no, avg = 0, 100, 0, 0
    total_marks = 0

    while line != '':
        line = students.readline()
        st_in = line.strip().split(',')

        if len(st_in) > 1:
            student_no += 1
            mark = int(st_in[3])

            if mark > highest:
                highest = mark
                h_id = st_in[2]
            if mark < lowest:
                lowest = mark
                l_id = st_in[2]
            total_marks += mark
            avg = (total_marks) / student_no

    return str(l_id), str(h_id), float(f'{avg:.2f}')
