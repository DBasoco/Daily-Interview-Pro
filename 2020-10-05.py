# Today we have: Level Order Traversal of Binary Tree
#
# Given the root of a binary tree, print its level-order traversal. For example:
#
#    1
#   / \
#  2   3
#     / \
#    4   5
#
# The following tree should output: 1, 2, 3, 4, 5

# So just go down level by level and return the value, if there are lower ones we check there and repeat. So this has
# to be recursion.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_level_order(root, order=[]):
    if root.left and root.right:
        return root.val

    else:
        order += [print_level_order(root.left, order)]
        order += [print_level_order(root.right, order)]


# almost there just need to add the value when we get to it and then add those below it behind it if there are values
# there


def print_level_order(root, order=[]):
    if root.val:
        order += [root.val]

        if root.left:

            order += [print_level_order(root.left, order)]

        if root.right:

            order += [print_level_order(root.right, order)]

    return order


# this returns the values but includes needless lists in the print out


def print_level_order(root):
    if root.val:
        print(root.val)

        if root.left:

            print_level_order(root.left)

        if root.right:

            print_level_order(root.right)


root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(root)

# Wow this was my favorite recursion solution yet. It is just so elegant and aesthetic to look. This is also the best
# I've ever done with a binary tree problem. This marks a vast improvement from my initial starting point with the
# concept. I'm proud of how much I have moved towards understanding coding and computers in general.
