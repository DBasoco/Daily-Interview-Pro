# Today we have: Count Number of Unival Subtress
#
# A unival tree is a tree where all the nodes have the same value. Given a binary tree, return the number of unival
# subtrees in the tree.
#
# For example, the following tree should return 5:
#
#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1
#
# The 5 trees are:
#   The three single '1' leaf nodes
#   The single '0' leaf node
#   The [1, 1, 1] tree at the bottom


# Okay so this seems like an insane problem. It sounds super advanced at first, but that's what makes it fun

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_unival(root, trees=0):
    tree = trees
    if root is None:  # eliminate TypeError at base case
        return 0
    else:
        # I am still struggling with recursion in binary trees
        t = root.val
        l = root.left
        r = root.right

        # for when they are equal
        if t == l == r:
            print(tree)
            tree += 1
            tree += count_unival(l, tree)
            tree += count_unival(r, tree)

        # for when it is an end leaf
        elif l is None and r is None:
            tree += 1
            print(tree)
        # for when it's branched but not an identical tree
        else:
            tree += count_unival(l, tree)
            tree += count_unival(r, tree)
    return tree


# It feels like syntax may have changed because this code seems like it should work but my IDE keeps saying something
# is wrong with my instance of tree whenever I return it at the end of the function.
# Yeah it keeps returning type errors. Not sure if it is a python issue, pycharm issue, or a problem with my code.

a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(count_unival(a))

# Well snap again a binary tree stopped me. I am learning ways to test where the issue in my logic is but if there
# was a new syntax change that I don't know it could slow me down by a lot. Hopefully I figure it out in the coming
# days. Given how beneficial this has been, I may follow up each question with a complete walkthrough the next day.
