# Today we have: Detect Linked List Cycle
#
# Given a linked list, determine if the linked list has a cycle in it. For notation purposes, we use an integer pos
# which represents the zero-indexed position where the tail connects to.
#
# Example:
# Input: head = [4, 3, 2, 1, 0], pos = 1
# Output: true
#
# The example indices a list where the tail connects to the second node.

# Okay I've never heard of any of this cycle of a linked list before but let's break down what we are given.
# 1. The list has 5 entries in descending order
# 2. Each entry has a next value identified by a node value
# 3. The next value of node3 loops back around to node1, represented as;
# 4 --> 3 --> 2 --> 1 --> 0 --> 3 --> 2 --> 1 --> 0 --> 3...
#
# This seems to mean that the linked list once created will never stop. So what we want to do is find a way without
# printing the infinite list whether the list is cyclical.
#
# So for the list to be cyclical one value of the list must have a next value that has already been used. This must be
# maintained as the value won't always be the first in the list as it can be cyclical with just two values.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head, list=[]):
        if len(list) == 0:
            list += [head.next.val]
            Solution().hasCycle(head.next, list)
            # creates the first entry in the list

        else:
            # if the list isn't empty we can run some tests

            print(list)
            # making sure that the function is called recursively

            for i in range(0, len(list)):
                # only traverse the length of the list

                if list[i] is head.next.val:
                    return True
                    # if the value is already in the list than there is a cycle

                else:
                    print('\n...')
                    # test to make sure that the for loop covers the full length of the list

                    pass

            list += [head.next.val]
            Solution().hasCycle(head.next, list)
            # add the next value to the list than recur the function with the new list


# so it works up until the tail
# what exactly is happening at the tail that is making it return None instead of true
# node3.next is testTail which doesn't have a value so what I need is a different logic check

class Solution(object):
    def hasCycle(self, head, list=[]):
        if len(list) == 0:
            list += [head.next.val] # this should be head.val because it skips 4 everytime
            Solution().hasCycle(head.next, list)

        else:
            print(list)
            for i in range(0, len(list)):
                if head.next.next.val == list[i]:
                    return True

                else:
                    pass
            list += [head.next.val]
            Solution().hasCycle(head.next, list)


testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail
testTail.next = node1  # this is the point that connects the tail back up to the start of the list

print(Solution().hasCycle(testHead))

# This was a tricky one. From the starters I wasn't sure what the question was even asking. The inclusion of the pos
# variable had me stumbling for a second before I realized it was for edification purposes and not a required
# variable. The next issue was with how the problem set up the loop. It make the loop back two step which messed with
# my logic. I didn't get to the end with this one but the deduction process was fun.
