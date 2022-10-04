'''
Given a previously sorted array which has been rotated, so that the n smallest values have been shifted to the end, find
the index of the value where the rotation has occurred (e.g, the sequence [3, 4, 5, 0, 1, 2] should return 3). Do this
by means of a binary search.

If the sequence is correctly sorted, return -1

You may assume the sequence does not contain duplicates.
__________
seq: The array to be searched
start: first index of the interval being searched
end: last index of the interval being searched
'''


def find_rotation(seq, start=None, end=None):
    pass


"""
A function that performs a recursive ternary search and returns the index of the searched value. A ternary search 
follows the same principle as a binary search, but instead of dividing the sequence in two, it does so in three.

If value is not found, return -1

You may assume the sequence does not contain duplicates
__________

seq: The sequence to be searched
val: the value to be searched for
start: first index of the interval being searched
end: last index of the interval being searched 
"""


def ternary_search(seq, val, start=None, end=None):
    pass


'''

Use the previously defined functions to return a tuple containing the index of the rotation value and the index of the 
value being searched for.
__________

seq: The sequence to be searched

val: the value to be searched for

'''


def rotation_and_index(seq, val):
    pass


if __name__ == '__main__':
    pass
