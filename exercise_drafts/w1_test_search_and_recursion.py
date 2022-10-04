import unittest
from w1_search_and_recursion import *


class MyTestCase(unittest.TestCase):
    def test_find_rotation1(self):
        seq = [2, 0, 1]
        self.assertEqual(1, find_rotation(seq))

    def test_find_rotation2(self):
        seq = [5, 0, 1, 2, 3, 4]
        self.assertEqual(1, find_rotation(seq))

    def test_find_rotation3(self):
        seq = [100, 900, 901, 903, 906, 1010, 50, 55, 59, 60, 89, 90, 92, 97]
        self.assertEqual(6, find_rotation(seq))

    def test_find_rotation4(self):
        seq = [11, 10]
        self.assertEqual(1, find_rotation(seq))

    def test_find_rotation5(self):
        seq = [10]
        self.assertEqual(-1, find_rotation(seq))

    def test_ternary_search1(self):
        seq = [0,3,4,6,8,10]
        self.assertEqual(4, ternary_search(seq, 8))

    def test_ternary_search2(self):
        seq = [0,3,4,6,8,10]
        self.assertEqual(0, ternary_search(seq, 0))

    def test_rotation_and_index1(self):
        seq = [0,3,4,6,8,10]
        self.assertTupleEqual((-1, 5), rotation_and_index(seq, 10))

    def test_rotation_and_index2(self):
        seq = [0, 3, 4, 6, 8, 10]
        self.assertTupleEqual((-1, 0), rotation_and_index(seq, 0))

    def test_rotation_and_index3(self):
        seq = [4, 6, 8, 10, 0, 3]
        self.assertTupleEqual((4, 4), rotation_and_index(seq, 0))


if __name__ == '__main__':
    unittest.main()
