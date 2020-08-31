# Today we have: Largest BST in a Binary Tree
#
# You are given the root of a binary tree. Find and return the largest subtree of that tree, which is a valid binary
# search tree.
#
#     5
#    / \
#   6   7
#  /   / \
# 2   4   9

# So for a binary search tree to be valid it must meet the requirement that the term to the left is less than the
# root and that the term to right must be greater than the root.

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        # preorder traversal
        answer = str(self.key)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer


# So what my script needs to do is move through the tree calling the __str__ function. Then I could go through that
# list and find the largest sum such that 1 < 0 < 3 wherein the value indicates the location in the sub-list.

# So again for these types of problems I have still yet to find a method of carrying information as I search the tree.


def largest_bst_subtree(root, list=[]):
    list += root.__str__()                      # basic creation of the code structure and list generation
    if root.left:
        largest_bst_subtree(root.left, list=list)
    if root.right:
        largest_bst_subtree(root.right, list=list)
    return list

# So we have a way of traversing the tree and returning the values under each root. Now I need to discern if the
# entry meets the criteria.

# Version 2


def largest_bst_subtree(root, list=[]):
    list += [root.__str__()]
    print(list)
    if root.left:
        largest_bst_subtree(root.left, list=list)
    if root.right:
        largest_bst_subtree(root.right, list=list)
    if len(root.__str__()) == 3:
        for i in list:
            if root.__str__()[1] < root.__str__()[0] < root.__str__()[2]: # adding the logic to create the criteria
                return list
            else:
                return None
    else:
        return None

# Keeps returning None


def largest_bst_subtree(root, list=[]):
    print(root.__str__())
    if len(root.__str__()) == 3:
        if root.__str__()[1] < root.__str__()[0] < root.__str__()[2]:
            list += root.__str__()
            return list
    # refining the process to eliminate gate errors
    if root.left:
        largest_bst_subtree(root.left, list=list)
    if root.right:
        largest_bst_subtree(root.right, list=list)
    else:
        return None


# So I tried parsing out the information while still letting it pass through but in the end it still returns none.
# Even though the logic should take over at that point.


def largest_bst_subtree(root, list=[]):
    if len(root.__str__()) == 3:
        if root.__str__()[1] < root.__str__()[0] < root.__str__()[2]:
            list += root.__str__()
            return list
    else:
        if root.left:
            largest_bst_subtree(root.left, list=list)
        if root.right:
            largest_bst_subtree(root.right, list=list)
        return list

# Pretty sold but this only works for the given model. Now let's adjust for the second criteria, which asks that it
# is the largest. Not sure what this means; the root is biggest; contains the largest value; the summation of the
# entries is the greatest.
# The third one is what I will work off of.


def largest_bst_subtree(root, list=[]):
    if len(root.__str__()) == 3:
        if root.__str__()[1] < root.__str__()[0] < root.__str__()[2]:
            if sum(root.__str__()) > sum(list[0]):   # so the string values aren't iterable
                list[0] == root.__str__()
            return list
    else:
        if root.left:
            largest_bst_subtree(root.left, list=list)
        if root.right:
            largest_bst_subtree(root.right, list=list)
        return list


def largest_bst_subtree(root, list=[]):
    if len(root.__str__()) == 3:
        if root.__str__()[1] < root.__str__()[0] < root.__str__()[2]:
            if sum(int(root.__str__())) > sum(int(list[0])): # so integers aren't iterable... that doesn't make any
                # sense they should function perfectly fine for summation since they are numbers which can be summed!
                list[0] == root.__str__()
            return list
    else:
        if root.left:
            largest_bst_subtree(root.left, list=list)
        if root.right:
            largest_bst_subtree(root.right, list=list)
        return list


node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
print(largest_bst_subtree(node))

# Out of all the binary tree problems, this one went the best. I'm developing better problem solving tools with each
# new day. I got the program to run and return the right value for this tree but I couldn't make it universal in
# time. I feel that if I switch my focus to the universal right from the start I'll have far more issues
# troubleshooting if I don't get it right away. This framework seems like best practice to me.
