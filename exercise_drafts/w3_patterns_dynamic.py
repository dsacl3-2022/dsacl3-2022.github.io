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

    for i in range(length):  # All possible starting indices
        for j in range(i, length):  # All possible ending indices
            rev_substr = string[i:j + 1][::-1]
            substr = string[i:j + 1]
            if rev_substr == substr:
                palind_mtrx[i][j] = True
    return palind_mtrx


"""
Given a string, find the minimum number of segmentations such that all resulting substrings are palindromes.
Use a dynamic programming approach.

"""


def min_seg(string, palind_mtrx=None, start=None, end=None, substr_to_min=None):
    # Initialize the matrix
    if palind_mtrx is None:
        palind_mtrx = palindrome_matrix(string)

    if start is None:
        start = 0

    if end is None:
        end = len(string) - 1 # TODO strange off-by-one behaviour, but it works

    substr = string[start:end]

    if substr_to_min is None:
        substr_to_min = {}  # a dict to keep record of the minimum splits required for a given substring

    # If the substring is not in the dictionary, add it. Else, just fetch it in constant time
    if substr not in substr_to_min.keys():

        # If it is a palindrome already
        if palind_mtrx[start][end]:
            substr_to_min[substr] = 0
        else:
            # if there is no palindrome anywhere in the substring, there are len - 1 segmentations
            min_segs = len(substr) - 1

            # try to find a better segmentation
            for seg_idx in range(start + 1, end):  # For each point at which a segmentation could occur
                # The min segmentation is 1 + the min segmentation of each of the parts
                current_min = 1 + min_seg(string, palind_mtrx, start, seg_idx, substr_to_min) + \
                              min_seg(string, palind_mtrx, seg_idx, end, substr_to_min)

                # If we've found a better segmentation, keep track of it and update dictionary at the end of the process
                if current_min < min_segs:
                    min_segs = current_min
            substr_to_min[substr] = min_segs

    return substr_to_min[substr]


if __name__ == "__main__":
    pass
