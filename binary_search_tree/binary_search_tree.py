"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

# note: the BSTNode class is a node


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left: BSTNode = None
        self.right: BSTNode = None

    def __str__(self):
        return f'value: {self.value}'

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            # Go R
            # check if there is already a node in R
            if self.right is None:
                # insert new node with value & insert in R spot
                self.right = BSTNode(value)
            else:
                # call insert function on new root at R
                self.right.insert(value)
        if value < self.value:
            # Go L
            # check if there is already a node in L
            if self.left is None:
                # insert new node with value in L spot
                self.left = BSTNode(value)
            else:
                # call insert function on new root at L
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value:
            return True
        elif target >= self.value:
            # Go R
            # if R is None:
            if self.right is None:
                return False  # we have traversed tree already
            # if R has value
            else:
                return self.right.contains(target)  # recurse on R node
        elif target < self.value:
            # Go L
            # check if L is None:
            if self.left is None:
                return False
            # if L has value
            else:
                return self.left.contains(target)  # recurse on L node

    # Return the maximum value found in the tree
    def get_max(self):
        current_max = self.value
        if self.right is None:
            return current_max
        else:
            # current_max = self.right.value  # if comment out still get right answer
            #                                 # b/c current_max is the value of the current BST node?
            return self.right.get_max()

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
bst.insert(10)
bst.insert(1000)

# print(bst)

# contains
print(bst.contains(1))  # True
print(bst.contains(7))  # True
print(bst.contains(800))  # False

# get_max
print(bst.get_max())  # 8



# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()


# current max
# current_max = self.value
# current_node = self
# while current_node is not None:
#     # check to see if node is greater than
#     if current_max < self.right.value:
#         current_max = self.right.value
#     # current_node = self.right
#     # self.right.get_max()
# return current_max


# if self.right is not None:
#     # update current_max to be whatever is to the R of the node
#     current_max = self.right.value
#     print('hi')
#     return current_max

