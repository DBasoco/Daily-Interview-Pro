# Today we have: Smallest Number that is not a Sum of a subset of List
#
# Given a sorted list of positive numbers, find the smallest positive number that cannot be a sum of any subset in
# the list.
#
# Example:
# Input: [1, 2, 3, 8, 9, 10]
# Output: 7
#
# Numbers 1 to 6 can all be summed by a subset of the list of numbers, but 7 cannot.


# So considering that the given list is sorted is good so I don't have to worry about that. My thinking is make list
# that gets a value added to it till I can't add that value anymore.


def findSmallest(nums):
    if nums[0] != 1:
        return 1
        # if the first entry isn't one than that's the smallest number that can't be summed to
    else:
        num = []
        num += [1]
        for i in range(0, nums):
            for j in range(1, nums):
                pass

    return None


# So this plan would take up way to much of my time complexity.
# Just did some whiteboard work and I think I have construction method that will work.

import numpy as np


def findSmallest(nums):
    if nums[0] != 1:
        return 1
    else:
        big = sum(nums)
        new = np.zeros(big)
        # we make a list of zeros with length equal to the total sum of the values in the list

        for i in nums:
            new[i - 1] = i
        # we then go and fill that list with all the entries from the given numbers in the index that is one less
        # than the listed value
        # this means that 1 --> 0 and 7 --> 6
        # this is what we will use to build a list of all the possible subset sums

        small = []
        # this will hold all the possible subset sums

        for j in range(0, len(new)):
            # traverse for the length of the new list

            if new[j] != 0:
                small += [new[j]]
                # if the number is in the original set it is added to the possible subset sums
                # the sum of a subset of a value is that value so any number present in the list is possible

            else:
                # if the value is zero we need to see if we can add the previous numbers of the set together in such
                # a way as to sum to one less than that index
                # the reason that we use only the entries before this is because of the sorted nature of the list
                # no value above this index has any chance of summing to it since they are already larger than it

                for k in range(0, j):
                    # traverse over only the numbers that are smaller than the current index for the reasons above

                    if sum(new[:j + 1]) == j:
                        small += new[j]

                    else:
                        return [small[j - 1]]
                    # this is where things went wrong I couldn't think of a time efficient way to check these sums
                    # without recursion which would ruin the whole function and only increase the time complexity.


print(findSmallest([1, 2, 3, 8, 9, 10]))

# This was a great challenge. My initial strategy failed but going to the whiteboard helped me see a better way of
# solving the problem. That method I really enjoyed. Although I couldn't crack it in time I still feel that this new
# method is the best way of approaching the problem.
