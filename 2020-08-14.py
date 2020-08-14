# Today we have:
# Merge K Sorted Linked Lists You are given an array of K sorted singly linked lists. Merge the linked
# lists into a single sorted linked list and return it.

class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ''
        while c:
            answer += str(c.val) if c.val else ''
            c = c.next
        return answer


def merge(lists):
    i, j = lists
    if i.next is not None:
        c = Node(i.val, Node(j.val, Node(merge([i.next, j.next]))))
    else:
        c = Node(i.val, Node(j.val))
    return c.__str__()


a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))

print(merge([a, b]))       # 123456

# c = Node(a.val, Node(b.val, Node(a.next.val, Node(b.next.val, Node(a.next.next.val, Node(b.next.next.val)))))) this
# is the form of c such that calling the __str__ function actually works after I found this form I simply needed to
# form the merge function to call itself for the next node value till the next val became None. The code only works
# when the linked lists are the same length. This could be an issue in the future.
# Example: should return 1234567 but fails
# x = Node(1, Node(3, Node(5, Node(7))))
# y = Node(2, Node(4, Node(6)))
# print(merge([x, y]))
