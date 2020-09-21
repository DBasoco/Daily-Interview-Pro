# Today we have: Symmetric k-ary Tree
#
# A k-ary tree is a tree with k-children, and a tree is symmetrical if the data of the left side of the tree is the
# same as the right side of the tree.
#
# Here's an example of a symmetric k-ary tree.
#
#          4
#      /       \
#     3         3
#  /  |  \   /  |  \
# 9   4   1 1   4   9


# So first, you must check if the node has children. If they don't is by definition symmetric. Next, you must check
# that the children are the same. If they aren't it is not symmetric. Finally, you check if the children have
# children and so on and so on repeating steps 2 and 3 till there are no more children.


class Node:
    def __int__(self, value, children=[]):
        self.value = value
        self.children = children


def is_symmetric(root):
    if not root.value:
        pass
        # if the value is empty just pass, aka a leaf

    else:
        if root.children:
            # if the value has children

            for i in range(0, len(root.children)):
                if root.children[i] == root.children[-(i + 1)]:
                    # this means that if the first value of the first child equals the last value of the second,
                    # and then this holds as you move towards each other then the children are symmetric
                    return True

                else:
                    return False


# This doesn't span the full scope of the problem and only goes one layer deep.


def is_symmetric(root):
    if not root.value:
        pass
    else:
        if not root.children:
            return True
            # so this adds an escape when all the children are confirmed to be symmetric we then return true

        else:
            if root.children:
                for i in range(0, len(root.children)):
                    if root.children[i] == root.children[-(i + 1)]:
                        is_symmetric(root.children[:])
                        # after teh children are confirmed we check to see if they themselves have children to check
                        # by recursion

                    else:
                        return False


tree = Node
tree.value = 4
tree.children = [Node, Node]
tree.children[0].value = 3
tree.children[1].value = 3
tree.children[0].children = [Node, Node, Node]

tree.children[1] = [Node(1), Node(4), Node(9)]
print(is_symmetric(tree))

# I never got to test if this actually worked as my IDE started having issues with the classification of my tree even
# though I have been using this same structure for weeks now. I wonder if an update to python happened that changed
# the syntax but this should have had no issue making the tree to test my function on.
