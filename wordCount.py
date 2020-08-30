# Author: Stephanie Galvan
# Class: Theory of Operating Systems
# Assignment 0: Python Intro
# Description: Given a text file, outputs a file with the total number of times each word in the given file
# appears (case insensitive) in alphabetical order

# TODO: @stephypy
# 1. [DONE] Verify command line args are  valid (only 2 args, they're both text files)
# 2. [DONE] Verify the input file exist; if output file doesnt exist then create it
# 3. [DONE] Set a re to only read words (no case sensitive, ignore punctuation)
# 4. [DONE] Read input file and save each word in dict with total number of appearances
# 5. Sort dict and save contents on output file (word <space> num per line)
# 6. Final testing and complete submission!

import sys  # command line arguments
import re  # regular expression tools
import os  # checking if file exists


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

    if not os.path.exists(filename):
        print("text file %s doesn't exist!" % filename)
        return False
    return True


def create_file(filename):
    """
    create text file with given name

    :param
        filename: (string) a text file
    """

    with open(filename, 'w+'): pass


def verify_args():
    """
    verify command line args are a total of two text files and they exist in the project. if
    output file does not exist, create it

    :return:
        tuple of strings representing a valid input and output file respectively
    """

    # verify there's only two additional args (besides python file)
    if len(sys.argv) != 3:
        print("Correct usage: wordCount.py <input text file> <output text file>")
        exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # input and output file cannot be the same
    if input_file == output_file:
        print("Input and Output files cannot be the same")
        exit()

    # verify args files are text files
    if not is_text_file(input_file) or not is_text_file(output_file):
        print("Correct usage: wordCount.py <input text file>.txt <output text file>.txt")
        exit()

    # verify input file exists
    if not does_file_exist(input_file):
        print("Exiting!")
        exit()

    # verify output file exists else create it
    if not does_file_exist(output_file):
        print("creating output file...")
        create_file(output_file)

    return input_file, output_file


def count_words(input_file):
    """

    :param
        input_file:
    :return:
    """

    total_count = dict()
    with open(input_file, 'r') as file:
        for line in file:
            # split by non alpha numeric characters
            for word in re.split('[^a-zA-Z]', line):
                word = word.lower()
                if word in total_count:
                    total_count[word] += 1
                else:
                    total_count[word] = 1
    return total_count


def write_to_file(output_file, word_count):
    pass


def main():
    """
    main method
    """
    input_file, output_file = verify_args()
    word_count = count_words(input_file)
    write_to_file(output_file, word_count)


main()
