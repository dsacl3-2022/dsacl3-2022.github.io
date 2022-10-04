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
    # if there is a self loop in outgoing neighbors, add it to incoming too:
    if to_add in out_neigh and to_add not in in_neigh:
        in_neigh += to_add

    ret_mtrx = matrix
    node2idx2node = two_way_dict(nodes)
    # Add the new node to the dict
    node2idx2node[to_add] = len(nodes)
    node2idx2node[len(nodes)] = to_add

    # find indices of outgoing neighbors
    out_idcs = {node2idx2node[neigh] for neigh in out_neigh}

    # np array for row. Each idx is true iff it's one of the indices of the outgoing neighbors
    new_row = np.array([[True if idx in out_idcs else False for idx in range(len(nodes))]])

    # append new row to existing matrix
    ret_mtrx = np.append(ret_mtrx, new_row, axis=0)

    # create array for column len(nodes)+1
    in_idcs = {node2idx2node[neigh] for neigh in in_neigh}
    new_col = np.array([[True] if idx in in_idcs else [False] for idx in range(len(nodes) + 1)])

    # append new_col to the matrix
    ret_mtrx = np.append(ret_mtrx, new_col, axis=1)

    # add the new node to the list of nodes
    nodes.append(to_add)

    return ret_mtrx, nodes


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
    # Create a two-way dictionary index <=> node
    node2idx2node = two_way_dict(nodes)

    if visited is None:
        visited = {start: None}

    neighbors = neighbors_sorted(matrix, node2idx2node, start)

    for neigh in neighbors:
        if neigh not in visited:
            visited[neigh] = start
            matrix_dfs_cycle(matrix, nodes, neigh, visited, cyclic)

        # If we already know it is cyclic, no need to check.
        elif not cyclic:
            # Backtrack from current node and see if you get to the visited node.
            cyclic = is_cycle(start, neigh, visited)

    return visited, cyclic


'''
Returns True if there is a cycle in the graph
_____

matrix: Graph represented by a numpy array with Boolean values
nodes: the names of the nodes in the order they are represented in the matrix
'''


def contains_cycle(matrix, nodes):
    for node in nodes:
        if matrix_dfs_cycle(matrix, nodes, node)[1]:
            return True
    return False


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
    adj_list = {}
    for row_idx in range(len(matrix)):
        # Create the dict entry for the row if it does not exist yet
        if nodes[row_idx] not in adj_list:
            adj_list[nodes[row_idx]] = set()
        # The indices of True in the row (the the indices in nodes of the neighbors)
        neigh_idcs = np.nonzero(matrix[row_idx])[0]
        # Add these neighbors to the list
        for true_idx in neigh_idcs:
            adj_list[nodes[row_idx]].add(nodes[true_idx])

            # If we're creating an undirected graph
            if not directed:
                if not nodes[true_idx] in adj_list:
                    adj_list[nodes[true_idx]] = set()
                adj_list[nodes[true_idx]].add(nodes[row_idx])

    return adj_list


# Helping method to backtrack
# Returns True if a cycle is found
def is_cycle(start, neigh, visited):
    # If start is None, we have reached the starting node without finding a cycle
    if start is None:
        return False
    if start == neigh:
        return True
    return is_cycle(visited[start], neigh, visited)


# Takes a list of unique nodes. Maps nodes to their index in their list and the index to the node
def two_way_dict(nodes):
    ret = dict()
    for idx, node in enumerate(nodes):
        ret[idx] = node
        ret[node] = idx
    return ret


# Get adjacent nodes in alphabetical order
def neighbors_sorted(matrix, node2idx2node, node):
    node_idx = node2idx2node[node]
    # Indices of True in the row corresponding to the node
    neigh_idcs = np.nonzero(matrix[node_idx])[0]

    neigh_nodes = []
    for idx in neigh_idcs:
        neigh_nodes.append(node2idx2node[idx])

    return sorted(neigh_nodes)
