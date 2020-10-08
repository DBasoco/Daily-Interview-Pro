# Today we have: Binary Tree Level with Minimum Sum
#
# You are given the root of a binary tree. Find the level for the binary tree with the minimum sum, and return that
# value.
#
# For instance, in the example below, the sums of the trees are 10, 2 + 8 = 10, and 4 + 1 + 2 = 7. So, the answer
# here should be 7.
#
#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2

# Alright I am feeling recursion again today with a variable that combines items of level marked by a pointer.

class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        self.below = []


def minimum_level_sum(root):

    if not root:
        return None

    else:
        return min(root.val, minimum_level_sum(root.left) + minimum_level_sum(root.right))


# the problem with this is that it doesn't account for the whole level it just does one branch at a time


def minimum_level_sum(root):

    if not root:
        return 0

    else:

        root.below += [minimum_level_sum(root.left)]
        root.below += [minimum_level_sum(root.right)]
        print(root.below)

        return min(sum(root.below), root.val)


# lets try iterative where we build lists
import numpy as np


def minimum_level_sum(root, level=0):

    if root is None:
        pass

    else:
        tot = []
        for i in range(0, 2**level):
            tot += [0]

        for i in range(0, 2**level):
            if root.right.val is not None:
                tot.pop()
                tot += [root.left]

            if root.left.val is not None:
                tot.pop()
                tot += [root.right]

        minimum_level_sum(root.left, level + 1)
        minimum_level_sum(root.right, level + 1)
        print(tot, level)

        return tot


node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

print(minimum_level_sum(node))

# Dang this was a fun one. I ran out of time before I could figure out a way to occupy the level lists. This method
# seems like the right one though. You share the memory space over a depth that is identified by a level marker. You
# then sum it and compare it to the sum of the level above and so forth. I ran into some NoneType snags but those can
# be bypassed with clever exit script and logic statements. Overall a fun binary tree challenge.
