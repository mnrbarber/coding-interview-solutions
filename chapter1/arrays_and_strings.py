from chapter1.helpers import *

def is_unique(str):
    """Implement an algorithm to determine if a string has all unique characters.
    What if you can't use additional data structures?"""

    # If the length is greater than the number of unique characters (ASCII) then
    # can immediately return False
    if len(str) > 256:
        return False

    # Set up a used character dictionary and for each character in the string add
    # a key of the value and count of the number of instances. If you hit a key
    # already in the dictionary you can return False
    used_characters = {}
    for x in str:
        if x in used_characters:
            return False
        used_characters[x] = 1

    return True


def check_permutation(string_1, string_2):
    """Given two strings, write a method to decide if one is a permutation of the other."""
    # First check they are the same length
    if len(string_1) != len(string_2):
        return False

    # Check each character is present
    for x in string_1:
        if x not in string_2:
            return False
    return True


def urlify(string, length):
    """Replace all spaces in a string with '%20'. Assuming string has sufficient length to hold
    additional characters."""
    # Remove any whitespace from end of string
    string = string[:length]
    string = string.replace(" ", "%20")
    return string


def palindrome_permutation(string):
    """Given a string check if it is a permutation of a palindome."""
    # if even all letters must be duplicated for a palindrome
    # if odd all but one letters must be duplicated (non duplicated must be the middle letter)
    str_nws = string.replace(" ", "")
    str_nws = str_nws.upper()
    odd = len(str_nws) % 2 == 1
    for x in str_nws:
        if count_occurances(x, str_nws) % 2 == 1 and not odd:
            return False
    return True


def one_away(string_one, string_two):
    """Given 3 Types of edit to a string (insert a character, remove a character or replace a character)
    Check if the 2 strings supplied are one (or zero) edits away"""
    #TODO: Try to do this in a combined case
    if string_one == string_two:
        # zero edits away so true
        return True
    #Find how many characters in one string and not the other
    #needs to be in same order

    found_non_matching = False
    if len(string_one) == len(string_two):
        for x in range(len(string_one)):
            if string_one[x] != string_two[x]:
                if found_non_matching:
                    return False
                else:
                    found_non_matching = True
        if found_non_matching:
            return True

    # check if different lengths (one removed or added)
    if len(string_one) - len(string_two) in [1, -1]:
        longer_string = string_one if len(string_one) == (len(string_two)+1) else string_two
        shorter_string = string_two if len(string_one) == (len(string_two)+1) else string_one
        # if all letters match except one then true else False
        y = 0
        for x in range(len(longer_string)):
            if y >= len(shorter_string):
                if found_non_matching:
                    return False
                else:
                    return True
            if longer_string[x] != shorter_string[y]:
                if found_non_matching:
                    return False
                elif longer_string[x + 1] == shorter_string[y]:
                    y -= 1
                    found_non_matching = True
                else:
                    return False
            y += 1
        if found_non_matching:
            return True


def string_compression(string):
    """Perform basic string compression using counts of repeated characters, if compressed
    string would be longer than original string then return original."""
    original_length = len(string)
    current_character = ""
    new_string = ""
    for x in string:
        if x == current_character:
            current_character_count += 1
        else:
            if current_character:
                new_string += current_character
                new_string += str(current_character_count)
                if len(new_string) >= original_length:
                    return string
            current_character = x
            current_character_count = 1
    new_string += current_character
    new_string += str(current_character_count)

    if len(new_string) >= original_length:
        return string
    return new_string


def rotate_matrix(matrix):
    """Given a nxn matrix representing an image where each
    pixel is 4 bytes write a method to rotate the image by 90 degrees."""


def zero_matrix(matrix):
    """Write an alogrithm such that if an element in an MxN matrix is 0 then
    the entire row and column are set to 0"""
    #careful that the rows and columns are triggered after zeroing other rows/columns


def string_rotation(string):
    """Assume you have a method isSubString. Given two strings s1 and s2 write code to check if s2 is a rotation of s2
    using only one call to isSubString."""
