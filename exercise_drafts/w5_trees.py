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

    def to_array(self, index=0, array=[]):
        while len(array) < index + 1:
            array.append(None)
        array[index] = self.data

        if self.left is not None:
            self.left.to_array(2*index + 1, array)

        if self.right is not None:
            self.right.to_array(2*index + 2, array)

        return array

    '''
    Get the depth of a node with respect to self. You may add default parameters to the method if you find it necessary.

    If the node is not in the subtree, return None

    ____
    node: the node whose depth we are calculating
    '''
    def get_depth(self, node, depth=0):
        on_left = None
        on_right = None

        # Return 0 if called on the root
        if node == self:
            return depth

        # If there is left child, calculate the depth wrt. the left child (if node is not found, it'll return None)
        if self.left is not None:
            on_left = self.left.get_depth(node, depth + 1)

        # If there is right child, calculate the depth wrt. the right child (if node is not found, it'll return None)
        if self.right is not None:
            on_right = self.right.get_depth(node, depth + 1)

        # Return the depth on the side in which the node has been found
        if on_left is not None:
            return on_left
        elif on_right is not None:
            return on_right

        # Return None if the node has not been found
        return None

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
    def to_qtree(self, string="", depth=0):
        if string == "":
            string += "\Tree "

        # A stack to keep track of the closing brackets
        stack = []

        # Only make roof if the depth is greater or equal to three AND the children are not leaves
        if depth >= 3 and not self.is_leaf() and (self.left is None or not self.left.is_leaf())\
                and (self.right is None or not self.right.is_leaf()):
            string += self.make_roof()

        else:
            # Make brackets if its a non-terminal and push closing brackets to stack
            if not self.is_leaf():
                string += "[." + str(self.data) + " "
                stack.append("]." + str(self.data) + " ")

            # Simply write the word if it's a terminal
            else:
                string += " " + str(self.data) + " "

            # Recursively write the code for left and the right children
            if self.left is not None:
                string = self.left.to_qtree(string, depth+1)

            if self.right is not None:
                string = self.right.to_qtree(string, depth+1)

            # Pop stack to add closing brackets
            if stack:
                string += stack.pop()

        return string

    # Helper method: The content of the leaves that are descendants of the tree, from right to left.
    def get_span(self):
        string = ""
        if self.is_leaf():
            string += str(self.data) + " "

        else:
            if self.left is not None:
                string += self.left.get_span()
            if self.right is not None:
                string += self.right.get_span()

        return string

    # Helper method to write the roof
    def make_roof(self):
        roof = "\qroof{" + self.get_span().strip() + "}"
        roof += "." + str(self.data) + " "
        return roof

    # Helper method
    def is_leaf(self):
        return self.right is None and self.left is None



if __name__ == "__main__":
    pass