# Author: Stephanie Galvan
# Class: Theory of Operating Systems
# Assignment 0: Python Intro
# Description: Given a text file, outputs a file with the total number of times each word in the given file
# appears (case insensitive) in alphabetical order

# TODO: @stephypy
# 1. [DONE] Verify command line args are  valid (only 2 args, they're both text files)
# 2. Verify the input file exist; if output file doesnt exist then create it
# 3. Set a re to only read words (no case sensitive, ignore punctuation)
# 4. Read input file and save each word in dict with total number of appearances
# 5. Sort dict and save contents on output file (word <space> num per line)
# 6. Final testing and complete submission!

import sys  # command line arguments
import re   # regular expression tools


def is_text_file(filename):
    """
    verify the file extension is .txt

    :param
        filename: (string) a file with some or no extension
    :return:
        boolean
    """

    if not re.findall(r'\.txt$', filename, re.IGNORECASE):
        return False
    else:
        return True


def does_file_exist(filename):
    """
    verify if given file exists

    :param
        filename: (string) name of some file
    :return:
        boolean
    """

    pass


def create_file(filename):
    """
    create text file with given name

    :param
        filename: (string) a text file
    """

    pass


def verify_args():
    """
    verify command line args are a total of two text files

    :return:
        tuple of strings representing a valid input and output file respectively
    """

    # set input and output files
    if len(sys.argv) != 3:
        print("Correct usage: wordCount.py <input text file> <output text file>")
        exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not is_text_file(input_file) or not is_text_file(output_file):
        print("Correct usage: wordCount.py <input text file>.txt <output text file>.txt")
        exit()

    return input_file, output_file


def main():
    """
    main method
    """
    input_file, output_file = verify_args()
    print(input_file)
    print(output_file)


main()
