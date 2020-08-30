# Author: Stephanie Galvan
# Class: Theory of Operating Systems
# Assignment 0: Python Intro
# Python version: 3.8.5
# Description: Given a text file, outputs a file with the total number of times each word in the given file
# appears (case insensitive) in alphabetical order

import sys  # command line arguments
import re  # regular expression tools
import os  # checking if file exists


def is_text_file(filename):
    """
    verify the file extension is .txt

    :param filename: (string) a file with some or no extension
    :return: boolean
    """

    if not re.findall(r'\.txt$', filename, re.IGNORECASE):
        return False
    else:
        return True


def does_file_exist(filename):
    """
    verify if given file exists

    :param filename: (string) name of some file
    :return: boolean
    """

    if not os.path.exists(filename):
        print("text file %s doesn't exist!" % filename)
        return False
    return True


def verify_args():
    """
    verify command line args are a total of two text files and they exist in the project. if
    output file does not exist, create it

    :return: tuple of strings representing a valid input and output file respectively
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

    return input_file, output_file


def count_words(input_file):
    """
    count the times of appearances of all words (case insensitive and ignoring punctuation) given a file

    :param input_file: (string) file which will be read
    :return: a sorted dict in the format of {word} : {count}
    """

    total_count = dict()
    with open(input_file, 'r') as file:
        for line in file:
            # split by non alpha numeric characters
            for word in re.split('[^a-zA-Z]', line):
                word = word.lower()
                # ignore whitespaces
                if word.isspace() or len(word) < 1:
                    continue
                # updating/adding occurrences
                elif word in total_count:
                    total_count[word] += 1
                else:
                    total_count[word] = 1
    sorted_total_count = sorted(total_count.items())
    return sorted_total_count


def write_to_file(output_file, word_count):
    """
    save all contents of the dict into the output file in which the word and its count is separated by a space

    :param output_file: (string) file that will contain all the word count
    :param word_count: (dict) dictionary with words and their individual counts
    """

    with open(output_file, "w+") as file:
        for curr_word_count in word_count:
            file.write(curr_word_count[0] + " " + str(curr_word_count[1]) + '\n')


def main():
    """
    main method
    """
    input_file, output_file = verify_args()
    word_count = count_words(input_file)
    write_to_file(output_file, word_count)


# start (:
main()
