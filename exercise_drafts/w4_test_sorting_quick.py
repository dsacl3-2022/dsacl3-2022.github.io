import unittest
from w4_sorting_quick import *


class MyTestCase(unittest.TestCase):
    def test_find_k_highest(self):
        self.assertEqual(find_k_highest([5, 4, 2, 10, 7, 23, 9, 3, 6], 4), 7)

    def test_find_k_highest2(self):
        self.assertEqual(find_k_highest([3, 4, 2, 9, 8, 0], 2), 8)

    def test_find_k_highest3(self):
        self.assertIsNone(find_k_highest([1, 4, 3, 8], 5))

    def test_find_k_highest4(self):
        self.assertEqual(find_k_highest([1, 4, 3, 8], 4), 1)

    def test_find_k_highest5(self):
        self.assertEqual(find_k_highest([6, 8, 7, 2, 4, 10, 9, 5, 42], 3), 9)

if __name__ == '__main__':
    unittest.main()
