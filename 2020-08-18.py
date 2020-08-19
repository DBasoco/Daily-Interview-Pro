# Today we have: Deepest Node in a Binary Tree
# You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

# Example:
#     a
#    / \
#   d   c
#  /
# d

# Alright we have another challenging one on the books today. I drafted some mock ups on a white board unfortunately
# this didn't give me any insight into a faster method than recursive. I feel that there has to be a better way
# to navigate these binary trees.

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return self.val


def deepest(node, depth=0, entry=''):           # establish a record for deepest and its entry
    pres = node.val                 # store present value

    if pres is not None:                # if a value is present
        depth += 1
        entry = pres
        y = node.left.val
        x = deepest(y, depth, entry)
        f = deepest(x, depth, entry)
    else:
        return entry, depth         # this will give us the deepest root


root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')

print(deepest(root))
