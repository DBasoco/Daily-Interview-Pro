# Today we have: Maximum Path Sum in Binary Tree
#
# You are given the root of a binary tree. Find the path between 2 nodes that maximizes the sum of all the nodes in
# the path, and return the sum. The path does not necessarily need to go through the root.
#
# Example:
#       10
#     /   \
#    2    10
#  /  \     \
# 20   1    25
#          /  \
#         3    4
#
# Path 20 - 2 - 10 - 10 for a total of 42

# Since the problem has to do with maximizing the value I would assume that the function max() should be utilized to
# construct a path. We may even have to reorder the tree to make it easier to traverse. Of course, that would mean
# first making an efficient method of formatting the tree which could have a high time complexity.

# For this tree there are 22 possible options for sums between two nodes. This process revolved starting on the left
# of the tree and working my way over to the other end. Along the way moving to each new node from the current node
# never going backwards. I'm concerned because all I can think of is a recursive solution, but even that seems like
# it wouldn't return me the correct value.

# Okay so for each node we have three options to add to the max:
# 1. Node: where we have just the node
# 2. Branch: max plus either add left or right to the node
# 3. Tree: max plus both children
# So I guess that means recursion... yay

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.Right = right


def maxPathSum(root):
    if root is None:
        return 0
        # resolves the trivial case for recursion

    else:
        # for leafs and branches

        l = maxPathSum(root.left)
        r = maxPathSum(root.right)
        # recur through the sides of the tree

    return None


# I think I may need a second function to call this


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.Right = None


def maxPathExtra(root):
    if root is None:
        return 0

    else:

        l = maxPathExtra(root.left)
        r = maxPathExtra(root.right)

        single = max(max(l, r) + root.val, root.val)


        top = max(single, l + r + root.val)

        maxPathExtra.res = max(maxPathExtra.res, top)

        return single


def maxPathSum(root):

    maxPathExtra.res = float('-inf')

    maxPathExtra(root)

    return maxPathExtra.res


root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)

print(maxPathSum(root))


# Well again this kernel run for some reason doesn't like the Node class and isn't instantiating the children values.
# Regardless of that, this problem was an extreme challenge. I spent about 66% of the time just working things out on
# the whiteboard. It seems that this method would work but the time complexity is nothing to be proud of. I'm not
# sure if there is a better way though.
