'''
Using ideas from the quick sort algorithm and without sorting the input, find the kth highest element in an unsorted
list. Assume no duplicates are present in the input. For example, [3, 4, 2, 9, 8, 0] with k = 2 should return 8.

If there is no k highest element, return None

____
seq: the sequence being searched

k: the rank being searched for
'''


def find_k_highest(seq, k):
    if k > len(seq):
        return None
    elif len(seq) == 1:
        return seq[0]
    else:
        lower = []
        higher = []
        pivot = seq[len(seq) - 1]
        for i in range(len(seq)):
            if seq[i] > pivot:
                higher.append(seq[i])
            elif seq[i] < pivot:
                lower.append(seq[i])

        # If the len of higher is k - 1, higher contains the top k - 1, which makes the pivot the k highest
        if len(higher) == k - 1:
            return pivot

        # If len(higher) is greater or equal to k, we still need to find the top k of the higher
        elif len(higher) >= k:
            return find_k_highest(higher, k)

        # If len(higher) < k, the we need to look for the kth highest element in the lower list. But we already have
        # the top len(higher) + 1 (the pivot), so we want
        elif len(higher) < k:
            k_in_lower = k - len(higher) - 1
            return find_k_highest(lower, k_in_lower)


if __name__ == "__main__":
    pass
