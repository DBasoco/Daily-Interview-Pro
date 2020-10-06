# Today we have: Determine If Linked List is Palindrome
#
# You are given a doubly linked list. Determine if it is a palindrome.

# I'm thinking recursion this time around because I need to traverse a linked list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def is_palindrome(node):
    if node:
        is_palindrome(node.next)

    return None

# scrap that we need to go the deeps node and determine if traversing back trough is the same as going there


def is_palindrome(node):

    if node is None:
        return True
        # base case from the recursion attempt

    match = node
    # matching pointer to traverse the list

    while match.next is not None:
        match = match.next
        # this will set our node to the very deepest entry in the link

    while match is not node:
        # till they become the same node again

        if match.val is not node.val:
            return False
            # if they aren't palindrome because they don't match when coming at each other

        node = node.next
        match = match.prev
        # node will move forward towards the end and match will move backwards towards the start

    return True


node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

print(is_palindrome(node))

# So for the past few problems involving nodes I wasn't able to run the code because I kept getting an argument error
# saying that the class didn't accept inputs which was super confusing to me. I use the same class structure in my
# other problems and even in my personal project. I was thinking that some kind of update came out but I couldn't
# find anything. Then today I ran into the same problem but instead this time when I read over my code I found my
# mistake. I called called __int__ instead of __init__ so no wonder the code wasn't running. BUt the actual problem
# was interesting. Like the last one I used a two pointer system to determine the final answer. I also had to think
# about what it means to be a palindrome. Which I think is a big theme you really have to break down concepts and
# systems to best use them to your advantage. Which I have really enjoyed!

