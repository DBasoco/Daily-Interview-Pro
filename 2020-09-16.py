# Today we have: Full Binary Tree
#
# Given a binary tree, remove the nodes in which there is only 1 child, so that the binary tree is a full binary tree.
#
# So leaf nodes with no children should be kept, and nodes with 2 children should be kept as well.
#
# Example:
# Input:
#     1
#    / \
#   2   3
#  /   /  \
# 0   9    4
#
# Output:
#    1
#   / \
#  0   3
#     /  \
#    9    4

# Okay so this is asking us to return a tree that only has full trees but not a complete tree. So I only need to
# identify leaves and nothing else. I am not aware of what this import does but I will try to break it down without
# using the internet, like I'd have to do in an interview.

from collections import deque


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
        # basic tree structure

    def __str__(self):
        q = deque()
        q.append(self)
        # okay this seems to make a class deque that is then occupied by self

        result = ''
        # what will be returned

        while len(q):
            num = len(q)
            while num > 0:
                n = q.popleft()
                # this will assign the the left value of q to n

                result += str(n.value)
                # adds that value to result

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                # okay so this will then check the lower nodes of the top node and them to q

                num = num - 1
                # then we take away from num
                # so if there is nothing in the node space below it won't reoccupy the value num

            if len(q):
                result += '\n'
            # when certain depth is fully run through then you move to the next lower level

        return result

# so this __str__ method will handle the construction of the final answer I just need to apply it in the right sequence


def fullBinaryTree(node):
    result = ''
    # the answer to right the other answers to

    if not node.value:
        pass
    else:
        result += node.__str__()
        if node.left:
            fullBinaryTree(node.left)
        if node.right:
            fullBinaryTree(node.right)
    return result

# So I was success in making the list but I did not remove the trees that weren't full


def fullBinaryTree(node):
    result = ''

    if not node.value:
        pass
    else:
        if node.left and node.right:
            result += node.__str__()
            fullBinaryTree(node.left)
            fullBinaryTree(node.right)
            # this should make it such that if both left and right aren't there it will pass and not add anything to
            # the result
        else:
            pass
    return result


# That didn't seem to work, let's try this. I think the first if statement is throwing off the logic. To me with how
# built out the __str__ is the full should be a simple modification, at least that's how I see it in  my head.


def fullBinaryTree(node):
    result = ''

    if node.left and node.right:
        result += node.__str__()
        fullBinaryTree(node.left)
        fullBinaryTree(node.right)

    else:
        result += '0'
    # these two alone should be enough to distinguish full or not with the bool statement
    return result

# Is it because I have my own result variable that is called each time?


def fullBinaryTree(node):

    if node.left and node.right:

        fullBinaryTree(node.left)
        fullBinaryTree(node.right)

        return node.__str__()

    else:
        return '0'


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.right.right = Node(4)
tree.right.left = Node(9)
tree.left.left = Node(0)

print(fullBinaryTree(tree))

# 1
# 03
# 94

# Okay so I wasn't able to find the right logic to make the correct result. I did come to an understanding of deque
# class structure, and worked on my own ability to interpret the function of unknown code. This is useful in research
# and pen testing. Another fun thing I notice is that each new iteration of my code is shorter than the last. This is
# different than some of my other ones that have only increased greatly in length as I have progressed them along
# testing. 
