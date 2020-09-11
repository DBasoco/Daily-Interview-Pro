# Today we have: Arithmetic Binary Tree
#
# You are given a binary tree representation of an arithmetic expression. In this tree, each leaf is an integer
# value, and a non-leaf node is one of the four operations: '+', '-', '*', '/'.
#
# Write a function that takes this tree and evaluates the expression.
#
# Example:
#      *
#    /  \
#   +    +
#  /\   /\
# 3  2 4  5
#
# This is the representation of the expression (3 + 2) * (4 + 5), and should return 45.

# This is a really interesting application of the binary tree. It seems like it breaks down the root relationship
# between inputs. If we were to go the other way with it, this tree may provide insight into how certain physical
# systems interact with each other.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


PLUS = '+'
MINUS = '-'
TIMES = '*'
DIVIDE = '/'

# Since we don't have to deal with the repeating calculations or storage space with the scheme that this equation
# asks we can use recursion. Next we need to look at the base case to see how that should react.


def evaluate(root, eq=''):
    if type(root.val) == int:
        # if the entry is an integer type then we need to add the value to the equation

        return root.val
        # we only need return the value in the base case

    else:
        # if it is a char then we do this

        eq = ''.join('(%s%s%s)') % (evaluate(root.left, eq), root.val, evaluate(root.right, eq))
        # this recurs the function for left and right down the tree and will stop when it hits a integer
        # this also constructs the basic frame work for the equation:
        # it groups base trees into parentheses for easy arithmetic

        return eval(eq)
        # returns the value of the equation from its string form, passing it up


tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree. right.right = Node(5)

print(evaluate(tree))


# So this ended up being easier than first anticipated. My first thoughts were crazy ideas about logic but then when
# I put it to the white board I saw that I could recur it to simplify my code. I think the main thing was that I once
# again thought of the problem as a physics one which really helped me out. I finished this faster than any other one
# I have tried to date. Some drawbacks I see is that if the entry is a float and not an int then the code will fail.
# As below:

tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2.7)
tree.right = Node(PLUS)
tree.right.left = Node(4.2)
tree. right.right = Node(5)

print(evaluate(tree))

# A correction to include float in the base filter if statement can fix this, but wasn't necessary for this problem.
