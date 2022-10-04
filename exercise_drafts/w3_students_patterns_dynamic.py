import numpy as np

"""
Find all palindromes in the string and fill in the matrix. palind_mtrx[i][j] is True iff the substring between indices i 
and j (both INCLUSIVE) is a palindrome 

_____

Return: a matrix with all the palindrome information of the string
"""


def palindrome_matrix(string):
    # Initialize matrix with all False
    length = len(string)
    palind_mtrx = np.array([[False for _ in range(length)] for _ in range(length)])

    # TODO fill in the matrix

    return palind_mtrx


"""
Given a string, find the minimum number of segmentations such that all resulting substrings are palindromes.
Use a dynamic programming approach.

An implementation has been started for you. You may discard it and write your own from scratch
"""


def min_seg(string, palind_mtrx=None, start=None, end=None, substr_to_min=None):
    # Initialize the matrix
    if palind_mtrx is None:
        palind_mtrx = palindrome_matrix(string)

    if start is None:
        start = 0

    if end is None:
        end = len(string) - 1

    substr = string[start:end]

    if substr_to_min is None:
        substr_to_min = {}  # a dict to keep record of the minimum splits required for a given substring

    # If the substring is not in the dictionary, add it. Else, just fetch it in constant time
    if substr not in substr_to_min.keys():

        # If it is a palindrome already
        if palind_mtrx[start][end]:
            substr_to_min[substr] = 0
        # TODO
        else:
            pass

    return substr_to_min[substr]


if __name__ == "__main__":
    pass
