import unittest
from w3_patterns_dynamic import *
import numpy as np
from timeit import default_timer as timer


class MyTestCase(unittest.TestCase):
    def test_palindromatrix_none(self):
        correct = np.full((3,3), False)
        np.fill_diagonal(correct, True)
        np.testing.assert_array_equal(correct, palindrome_matrix("abc"))

    def test_palindromatrix_all(self):
        correct = np.full((4, 4), True)
        correct[np.tril_indices(4, -1)] = False
        np.testing.assert_array_equal(correct, palindrome_matrix("zzzz"))

    def test_palindromatrix_full_palindrome(self):
        correct = np.full((5,5), False)
        np.fill_diagonal(correct, True)
        correct[0][4] = True
        correct[1][3] = True
        np.testing.assert_array_equal(correct, palindrome_matrix("civic"))

    def test_palindromatrix_some(self):
        correct = np.full((9,9), False)
        np.fill_diagonal(correct, True)
        correct[1][3], correct[5][7], correct[6][8] = True, True, True
        np.testing.assert_array_equal(correct, palindrome_matrix("abcbdefef"))

    def test_min_seg1(self):
        self.assertEqual(1, min_seg("reconoce"))

    def test_min_seg2(self):
        self.assertEqual(0, min_seg("anitalavalatina"))

    def test_min_seg3(self):
        self.assertEqual(2, min_seg("abcdc"))

    def test_min_seg4(self):
        self.assertEqual(4, min_seg("xyabcdc"))

    def test_min_seg5(self):
        self.assertEqual(5, min_seg("xyabcbca"))


if __name__ == '__main__':
    unittest.main()
