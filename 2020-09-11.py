# Today we have: Tree Serialization
#
# You are given the root of a binary tree. You need to implement 2 functions:
#
# 1. serialize(root) which serializes the tree into a string representation
# 2. deserialize(s) which deserializes the string back to the original tree that it represents
#
# For this problem, often you will be asked to design your own serialization format. However, for simplicity,
# let's use the pre-order traversal of the tree. Here's your starting point.

# Okay just as I feared this is rather daunting. I need to create two functions, but that isn't the issue I am more concerned
# with how to decode what serialize means. I think I can deserialize simply using the split function but making the thing
# in the first place is going to be the real issue here.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        # pre-order printing of the tree

        result = ''
        result += str(self.val)

        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)

        return result
    # so this should be the basic makeup for moving through a tree and returning a string
    # but again the problem is with the terminology, without knowing exactly what I am being asked to do I can't hope to solve the problem

# Okay so the syntax for the serialization is as follows:
# 1. the first entry is the root of the tree
# 2. if a number, x, immediately follows another number, y, then x is within the tree of y and breaks off left
# 3. if a number, i, is preceded by a # then i breaks off from a number, j, in front of i where j is equal to the number of #'s preceding i
#
# The only thing I don't get is why the #'s are after the 7. I assume it has to be due to the fact that 7 is a leaf or it
# may just be the case that all serializations of this scheme end this way. Not sure which is the case.

def serialize(root):



def deserialize(data):
    data.replace(' ', '')
    # remove spaces

    return data.translate({ord('#'): None})
    # return data without the #'s in it





#     1
#    / \
#   3   4
#  / \    \
# 2   5    7

tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)

serial = serialize(tree)
print(serial)
deserial = deserialize(serial)
print(deserial)

# I was very far from finishing this one. I had just finished deciphering the examples writing a quick script for the
# deserialization when the time ran out. I am proud that I was able to break down the givens and create some kind of
# rules that they obey in-order to progress the problem. Again my physicist is showing lol. This may have been challenging
# but it was still very interesting to try out.
