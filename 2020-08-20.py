# Today we have: First Missing Positive Integer
# You are given an array of integers. Return the smallest positive
# integer that is not present in the array. The array may contain duplicate entries.

# nums = [3, 4, -1, 1] should return 2

import numpy as np


def first_missing_positive(nums):
    new = np.zeros(len(nums))
    for i in nums:
        if i > 0:
            new[i - 1] = i
        else:
            pass
    local = np.where(new == 0)
    return local[0][0] + 1

# since the where function returns ever instance of any array in the order that they appear and that the new array is
# ordered, thus we need only call local first entry (for the event of multiple missing) plus 1 to get the smallest
# missing positive integer. My one concern is that np.where is not in constant space. I believe it is in constant time.


for i in [3, 4, -1, 1]:
    print(i)
print(first_missing_positive([3, 4, -1, 1]))

