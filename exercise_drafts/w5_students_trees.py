class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    '''
    Represent the subtree of which self is the root as an array. You may add default parameters to the method if you 
    find it necessary
    
    ____
    Return the array (list) representation of the subtree with self as the root node. 
     
    '''

    def to_array(self):
        pass

    '''
    Get the depth of a node with respect to self. You may add default parameters to the method if you find it useful.
    
    If the node is not in the subtree, return None
    
    ____
    node: the node whose depth we are calculating
    '''
    def get_depth(self, node):
       pass

    '''
    Write a qtree representation of the Node given and its descendants. If a node with descendants has depth greater or
    equal to 3, use a roof, unless its children are leaves.  
    
    You can find the qtree documentation under the URL https://www.ling.upenn.edu/advice/latex/qtree/qtreenotes.pdf. You
    only need to understand sections 3.1, 3.2 and 3.3.
    
    For testing purposes, please always use the option of writing the label after both the left and the right bracket of
    the node as explained in section 3.2.
    
    You can check the correctness of your qtree by using LaTeX. You may also add default parameters to the signature 
    should you find it useful
    '''

    def to_qtree(self):
        pass

    # TODO Helper method: get the data of the leaves that are descendants of the tree, from right to left, as a string.
    def get_span(self):
        pass

    # Helper method: draw a roof
    def make_roof(self):
        roof = "\qroof{" + self.get_span().strip() + "}"
        roof += "." + str(self.data) + " "
        return roof

    # Helper method to determine whether a node is a leaf
    def is_leaf(self):
        return self.right is None and self.left is None


if __name__ == "__main__":
    pass