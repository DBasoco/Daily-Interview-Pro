# Today we have: Get all Values at a Certain Height in a Binary Tree
#
# Given a binary tree, return all values given a certain height h.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


for i in range(0, 3): # okay there doesn't seem to be an issue with my ranges
    print(i)


# okay so my first thought was to search and add values at height to a new list
def valuesAtHeight(root, height):
    h = []
    for i in range(0, height):  # this will iterate the function just to the depth of three
        if root is None:
            pass
        elif root.value is not None:
            if i == height-1:               # so if we aren't on the right level we go down again
                h += [root.value]           # the storing of the values keeps getting reset when the recursion occurs
            else:
                h = valuesAtHeight(root.left, height - 1)
                h = valuesAtHeight(root.right, height - 1)
        else:
            pass

    return h

# there is something wrong with my ranges that is throwing off my search I believe
# so the ranges weren't the issue
# now I'm facing a memory issue, I think I can solve it but I'm running out of time...
# made a carry along correction but now it is just returning the right most side of the tree
# well I could run this function a number of times = h and then extract the first entry from the list
# however this wouldn't include the value a.right.left (if it existed)

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

# return [4, 5, 7]


a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)

print(valuesAtHeight(a, 3))


# Firstly, from my work yesterday I know that the given binary tree isn't actually a true binary tree since it lacks
# the < x < property for direction. Second, it is once again apparent that I lack binary tree traversal skills,
# at the moment.
