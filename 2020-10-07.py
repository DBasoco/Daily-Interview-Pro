# Today we have: Lowest Common Ancestor of 2 Nodes in Binary Tree
#
# You are given the root of a binary tree, along with two nodes, A and B. Find and return the lowest common ancestor
# of A and B. For this problem, you can assume that each node also has a pointer to its parent, along with its left
# and right child.
#
#    a
#   / \
#  b   c
#     / \
#    d*  e*
# c

# This a is very interesting question. It seems to have many real world applications so experience with it is
# essential. The method to store this seems troublesome though. Since, it is a binary tree I am thinking of using
# recursion, however, I can't just endless recur I need to stop when the child is reached and then find the path to
# the other node traveling through the lowest ancestor node. Then return that node and print it's value. Very irksome
# indeed.

# An approach I would think of is to use the property of binary trees where the left children are lower than the
# right children. If that was the case I could compare values with built in functions to compare that way
# recursively. But the given tree uses char not int so I will have to use the double link factor of the tree that
# assumes the root knows its parent inherently. This means I won't have to waste space storing that info.


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val


def lowestCommonAncestor(root, a, b):
    if root is None:
        return None
        # remove base trivial case

    if a.parent is b.parent:
        return a.parent
        # check if they share a parent


# so this accounts for the case where the children are on the same level and the path between them goes through only
# one ancestor node.


def lowestCommonAncestor(root, a, b):
    if root is None:
        return None

    if a.parent is b.parent:
        return a.parent

    else:
        lowestCommonAncestor(a.parent, a, b.parent)
        # move the root to the parent of a while keeping a and moving b to the parent of b
        # this will progress up the tree till they collide at the lowest common ancestor
        

root = TreeNode('a')
root.left = TreeNode('b')
root.left.parent = root
root.right = TreeNode('c')
root.right.parent = root
x = root.right.left = TreeNode('d')
root.right.left.parent = root.right
y = root.right.right = TreeNode('e')
root.right.right.parent = root.right

print(lowestCommonAncestor(root, x, y).val)

# I am concerned that this solution doesn't account for every possibility but in whiteboard mock ups the function
# returns the correct value 'a' when 'b' is selected instead of 'd'. I think the simple script comes from the fact
# that the trees construction is so heavily verbose. The inclusion of the parent value makes the need for a complex
# function needless.
