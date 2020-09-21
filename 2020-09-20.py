# Today we have: H-Index
#
# The h-index is a metric that attempts to measure the productivity and citation impact of the publication of a
# scholar. The definition of the h-index is if a scholar has at least h of their papers cited h times.
#
# Given a list of publications of the number of citations a scholar has, find their h-index.
#
# Example:
# Input: [3, 5, 0, 1, 3]
# Output: 3
#
# Explanation: there are 3 publications with 3 or more citations, hence the h-index is 3.

# So it seems like I will be caring a value h along and if the value at index i is greater than or equal to my
# current h than I add one to the h.
# A possible problem I just though of is if the values increase in size I could make a mistake.

# So I need to reconcile this issue:
#   [3, 5, 0, 1, 3]       [0, 1, 3, 3, 5]
# h: 1  2  2  2  3      h: 0  1  1  1  3

# As we can see both of these lists must return 3 but the method to construct them on the surface seems entirely
# different. Since, both cases are equally likely the function must accommodate both of them.

def hIndex(publications):
    h = 0
    # start h at zero
    for i in range(0, len(publications)):
        for j in range(0, i + 1):
            if publications[j] > h:
                h += 1
                # this only works for the first entry, this would result in 4 for the rearrangement I made

    return h

# So some logic needs to added that keeps track of every single book that fits that description. Maybe I need to make
# a second table.


import numpy as np


def hIndex(publications):
    h = 0
    # start h at zero

    pubs = np.zeros(len(publications))
    # so the number of books that fit will start at zero and move up as the max increases

    for i in range(0, len(publications)):
        for j in range(0, i + 1):
            if publications[j] > h:
                for k in range(0, j):
                    if

            else:
                pass
                # auto pass if the value at index i is less than h

    return h


print(hIndex([5, 3, 3, 1, 0]))


# So I didn't finish but the idea was to check first if the entry was greater than h. This meant that the value had
# the chance to increase h. Then I was once again going to go through the list to see the number of publications that
# had a value greater than h. If this was the case the max between the current h and the value such that num books =
# max value of those books. This construction would solve the problem I saw at the start of the problem.

