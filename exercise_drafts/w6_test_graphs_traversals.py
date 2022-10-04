from unittest import TestCase
from w6_graphs_traversals import *
import numpy as np


class Test(TestCase):

    def test_add_node1(self):
        nodes = ["a", "b", "c"]
        mtrx = np.full((3, 3), True)
        mtrx[0][0] = False
        mtrx[0][2] = False
        mtrx[1][1] = False
        added = add_node(mtrx, nodes, "d", ["b"], ["b", "d"])

        expected_mtrx = np.full((4, 4), True)
        expected_mtrx[0][0] = False
        expected_mtrx[0][2] = False
        expected_mtrx[1][1] = False
        expected_mtrx[0][3] = False
        expected_mtrx[2][3] = False
        expected_mtrx[3][0] = False
        expected_mtrx[3][2] = False

        # Is the new matrix equal to the expected matrix
        self.assertTrue(np.array_equal(added[0], expected_mtrx))
        self.assertListEqual(added[1], ['a', 'b', 'c', 'd'])

    def test_add_node2(self):
        nodes = ["a", "b", "c"]
        mtrx = np.full((3, 3), True)
        mtrx[0][0] = False
        mtrx[0][2] = False
        mtrx[1][1] = False
        added = add_node(mtrx, nodes, "d", {'a', "b", 'd'}, {"b", "d"})

        expected_mtrx = np.full((4, 4), True)
        expected_mtrx[0][0] = False
        expected_mtrx[0][2] = False
        expected_mtrx[1][1] = False
        expected_mtrx[2][3] = False
        expected_mtrx[3][0] = False
        expected_mtrx[3][2] = False

        # Is the new matrix equal to the expected matrix
        self.assertTrue(np.array_equal(added[0], expected_mtrx))
        self.assertListEqual(added[1], ['a', 'b', 'c', 'd'])

    def test_dfs_cycle1(self):
        mtrx = np.full((3, 3), True)
        mtrx[0][0] = False
        mtrx[0][2] = False
        mtrx[1][1] = False
        nodes = ['a', 'b', 'c']

        dfs_cycle = matrix_dfs_cycle(mtrx, nodes, 'a')

        self.assertDictEqual(dfs_cycle[0], {'a': None, 'b': 'a', 'c': 'b'})
        self.assertFalse(dfs_cycle[1])

    def test_dfs_cycle2(self):
        nodes = ["b", "c", "a", "d"]
        mtrx = np.full((len(nodes), len(nodes)), True)
        mtrx[0][0] = False
        mtrx[0][2] = False
        mtrx[0][3] = False
        mtrx[1][1] = False
        mtrx[3][2] = False
        mtrx[3][3] = False

        dfs_cycle = matrix_dfs_cycle(mtrx, nodes, 'a')

        self.assertDictEqual(dfs_cycle[0], {'a': None, 'b': 'a', 'c': 'b', 'd': 'c'})
        self.assertTrue(dfs_cycle[1])

    def test_dfs_cyclic3(self):
        nodes = ['a', 'b', 'c', 'd']
        mtrx = np.full((len(nodes), len(nodes)), False)

        mtrx[0][2] = True
        mtrx[0][3] = True
        mtrx[2][1] = True
        mtrx[3][1] = True
        mtrx[3][2] = True

        dfs_cycle = matrix_dfs_cycle(mtrx, nodes, 'a')

        self.assertDictEqual(dfs_cycle[0], {'a': None, 'c': 'a', 'b': 'c', 'd': 'a'})
        self.assertFalse(dfs_cycle[1])

    def test_contains_cycle1(self):
        mtrx = np.full((3, 3), True)
        mtrx[0][0] = False
        mtrx[0][2] = False
        mtrx[1][1] = False

        nodes = ['a', 'b', 'c']
        self.assertTrue(contains_cycle(mtrx, nodes))

    def test_contains_cycle2(self):
        nodes = ['a', 'b', 'c', 'd']
        mtrx = np.full((len(nodes), len(nodes)), False)

        mtrx[0][2] = True
        mtrx[0][3] = True
        mtrx[2][1] = True
        mtrx[3][1] = True
        mtrx[3][2] = True

        self.assertFalse(contains_cycle(mtrx, nodes))

    def test_matrix2list_directed1(self):
        mtrx = np.full((7, 7), False)

        for idx in [1, 2]:
            mtrx[0][idx] = True
        for idx in [3, 4]:
            mtrx[1][idx] = True
        mtrx[2][4] = True
        for idx in [4, 5]:
            mtrx[3][idx] = True
        mtrx[4][5] = True
        mtrx[5][6] = True
        mtrx[6][3] = True

        self.assertDictEqual({'A': {'B', 'C'}, 'B': {'D', 'E'}, 'C': {'E'}, 'D': {'E', 'F'},
                              'E': {'F'}, 'F': {'G'}, 'G': {'D'}},
                             matrix2list(mtrx, ["A", 'B', 'C', "D", "E", "F", "G"]))

    def test_matrix2list_directed2(self):
        mtrx = np.full((3, 3), True)
        mtrx[0][0] = False
        mtrx[0][2] = False
        mtrx[1][1] = False

        nodes = ['A', 'B', 'C']

        self.assertDictEqual({'A': {'B'}, 'B': {'A', 'C'}, 'C': {'A', 'B', 'C'}}, matrix2list(mtrx, nodes))

    def test_matrix2list_undirected1(self):
        mtrx = np.full((7, 7), False)

        for idx in [1, 2]:
            mtrx[0][idx] = True
        for idx in [3, 4]:
            mtrx[1][idx] = True
        mtrx[2][4] = True
        for idx in [4, 5]:
            mtrx[3][idx] = True
        mtrx[4][5] = True
        mtrx[5][6] = True
        mtrx[6][3] = True

        self.assertDictEqual({'A': {'B', 'C'}, 'B': {'A', 'D', 'E'}, 'C': {'E', 'A'}, 'D': {'E', 'F', 'B', 'G'},
                              'E': {'F', 'B', 'C', 'D'}, 'F': {'G', "D", 'E'}, 'G': {'D', 'F'}},
                             matrix2list(mtrx, ["A", 'B', 'C', "D", "E", "F", "G"], False))

    def test_matrix2list_undirected2(self):
        mtrx = np.full((3, 3), True)
        mtrx[0][0] = False
        mtrx[0][2] = False
        mtrx[1][1] = False

        nodes = ['A', 'B', 'C']

        self.assertDictEqual({'A': {'B', 'C'}, 'B': {'A', 'C'}, 'C': {'A', 'B', 'C'}}, matrix2list(mtrx, nodes, False))
