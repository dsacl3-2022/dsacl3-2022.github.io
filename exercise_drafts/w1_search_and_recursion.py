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
    if start is None:
        start = 0
    if end is None:
        end = len(seq) - 1

    while start < end:
        # If the start element is lower than the end element, the subsequence is properly sorted
        if seq[start] < seq[end]:
            return -1
        mid = start + (end - start) // 2
        # If mid is zero, we are looking at only two elements. Since we know there is a rotation,
        # seq[1] is lower than seq[0]
        if mid == 0 and len(seq) > 1:
            return 1

        # Check if the rotation has happened at mid point
        elif seq[mid] < seq[mid - 1]:
            return mid

        # The rotation has already occurred if the start is greater than the middle.
        # Look in the first half
        elif seq[start] > seq[mid]:
            return find_rotation(seq, start, mid - 1)

        # If the start is not greater than the middle, look for rotation on the second half
        elif seq[mid] > seq[end]:
            return find_rotation(seq, mid + 1, end)

    return -1


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
    if start is None:
        start = 0
    if end is None:
        end = len(seq) - 1
    if start == end and seq[start] == val:
        return start
    while start < end:
        third = (end - start) // 3
        mid1 = start + third
        mid2 = mid1 + third

        if val == seq[mid1]:
            return mid1
        elif val == seq[mid2]:
            return mid2
        elif val < seq[mid1]:
            return ternary_search(seq, val, start, mid1 - 1)
        elif val < seq[mid2]:
            return ternary_search(seq, val, mid1 + 1, mid2 - 1)
        else:
            return ternary_search(seq, val, mid2 + 1, end)

    return -1


'''

Use the previously defined functions to return a tuple containing the index of the rotation value and the index of the 
value being searched for.
__________

seq: The sequence to be searched

val: the value to be searched for

'''


def rotation_and_index(seq, val):
    rotation = find_rotation(seq)

    # if there's no rotation, just look in entire sequence
    if rotation == -1:
        return -1, ternary_search(seq, val)
    elif val == seq[-1]:
        return rotation, len(seq) - 1
    # If value we're looking for is greater than the last number, it must be before the rotation or nowhere.
    elif val > seq[-1]:
        return rotation, ternary_search(seq, val, 0, rotation - 1)
    else:
        return rotation, ternary_search(seq, val, rotation, len(seq) - 1)


if __name__ == '__main__':
    pass
