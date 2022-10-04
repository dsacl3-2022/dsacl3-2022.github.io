import numpy as np

"""
Given a graph in the form of an adjacency matrix, add a node and its
associated edges to other existent nodes in the graph. You should add the new node as the last column/row of the matrix.

_____
matrix: the adjacency matrix implemented using a numpy array of Boolean values
nodes: a list of the nodes in the order they are represented in the matrix
to_add: the node being added
in_neigh: a set of the incoming nodes
out_neigh: a set of the outgoing neighboring nodes

Return: tuple: (new matrix, nodes of the matrix)
"""


def add_node(matrix, nodes, to_add, in_neigh, out_neigh):
    pass


"""
Given a graph, perform depth first search. When it is possible to visit more than one node, visit the first possible one
in alphabetical order.

You may assume that all nodes have string names
_____

matrix: Graph represented as a numpy array with Boolean values
nodes: the names of the nodes in the order they are represented in the matrix
start: first node to visit
visited: a dictionary keeping track of visited nodes (keys) and where they were visited from.


return: a tuple (dict: visited, Boolean: does the traversal find a cycle)
"""


def matrix_dfs_cycle(matrix, nodes, start, visited=None, cyclic=False):
    pass


'''
Returns True if there is a cycle in the graph
_____

matrix: Graph represented by a numpy array with Boolean values
nodes: the names of the nodes in the order they are represented in the matrix
'''


def contains_cycle(matrix, nodes):
    pass


'''
Returns an adjacency list (implemented with a dict) that represents the same graph as the given 
adjacency matrix

_____

matrix: Graph represented as a numpy array with Boolean values
nodes: the names of the nodes in the order they are represented in the matrix
directed: if False, the resulting adjacency list must represent an undirected graph

return: adjacency dict mapping a node to the set of its neighbors. 
'''


def matrix2list(matrix, nodes, directed=True):
    pass
