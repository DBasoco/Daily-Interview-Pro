# Today we have: Validate Binary Search Tree
#
# You are given a binary search tree. Return true if it is a valid binary search tree, and false otherwise. Recall
# that a binary search tree has the property that all values in the left subtree are less than or equal to the root,
# and all values in the right subtree are greater than or equal to the root.

# It was cool to learn that property of a binary search tree. I didn't know that till today.

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def is_bst(root):
    x = root.key
    if x is not None:
        l = root.left
        r = root.right
        try:                            # use try instead of convoluted logic trees
            if l.key < x < r.key:
                is_bst(l)
                is_bst(r)
            else:
                return False
        except AttributeError:          # it is just ignoring information right now
            if l and r is None:
                pass
            if l or r is None:
                if type(l) is not None:
                    is_bst(l)
                if type(r) is not None:
                    is_bst(r)



                #(is_bst(l) if type(l) is not None)
                #(is_bst(r) if type(r) is not None)
    else:
        pass
    return True


a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(8)

print(is_bst(a))

# So even after I tried to eliminate needless logic statements they still happened and ended up forcing me to run out
# of time. This was still very productive in teaching me more about binary trees and implementing logic or try
# statements.
