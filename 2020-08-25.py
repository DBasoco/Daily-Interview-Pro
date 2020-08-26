# Today we have: Reconstruct Binary Tree from Preorder and Inorder Traversals
#
# You are given the preorder and inorder traversals of a binary tree in the form of arrays. Write a function that
# reconstructed the tree represented by these traversals.
#
# Preorder: [a, b, d, e, c, f, g]
# Inorder: [d, b, e, a, f, c, g]
#
#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g
#
# So from what I can surmise the preorder is effectively how the tree would be given that all the node classifications
# when writing the class object were to be removed. The inorder is the tree read left to right. With these two arrays
# it should be possible to reconstruct the tree since you are given information of left to right, and top to bottom
# not respectfully.

from collections import deque


# I'm not familiar with this module, however, it uses append so I assume that deque command works on the list in some
# way

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        q = deque()
        # no idea

        q.append(self)
        # adds object to q so q must be a class with some needed function

        result = ''
        # returns the list in an order of top level first reading left to right

        while len(q):  # for the time that
            n = q.popleft()
            # this seems to populate a node left of self

            result += n.val
            # fills the result with new node value

            if n.left:  # the node could be a leaf so we have to check if there is anything to populate or if we
                # should move on
                q.append(n.left)
            if n.right:  # same as if n.left
                q.append(n.right)
        return result


def reconstruct(preorder, inorder):
    pre = preorder
    ori = inorder
    # these were named after Starwars original and prequels, I mean these are suppose to be fun right

    construct = Node(pre[0]) # so the first value in preorder is the top of the tree


    return construct
# So after some testing I have learned that deque does not do what I thought
# I did manage to write a function that says both 'b' and 'g' are in the same spot


tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g'])

print(tree)

# Wow time flew by. Everything I tried when constructing these tress didn't seem to do anything. First,
# I got too distracted with what I didn't know (the deque) that I ignored what I did know (using class to construct
# trees). Second, although it was good practice to annotate and write out my thoughts when looking at deque I really
# should have looked it up online to see how to use it. 
