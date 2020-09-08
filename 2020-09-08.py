# Today we have: Longest Increasing Subsequence
#
# You are given an array of integers. Return the length of the longest increasing subsequence (not necessarily
# contiguous) in the array.
#
# Example:
# [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
#
# The following input should return 6 since the longest increasing subsequence is 0, 2, 6, 9, 11, 15.

# So my first thought is that I need to piecewise this thing out. Since the I need to only pass once beacause the
# moment it decreases there is no way that a subset of that set will be larger by definition so I'm thinking a while
# loop. Next I need to consider how I need to create a list to carry new sets along as I move then once it decreases
# I need to compare it's length to that of a stored value. The nice thing is that it only asks for the lenght not
# that the items be arranged in a certain way.

def longest_increasing_sub(nums):
    grt = []
    # this will be where I store the longest sequence

    carry = []
    # this is the thing that gets carried along as I compare numbers

    for i in range(0, len(nums)):
        if nums[i] < nums[i + 1]:
            carry += [nums[i]]
            # so this sees
        else:
            if len(carry) > len(grt):
                grt = carry
                carry = []
            else:
                carry = []
        return None

# Just realized that I misread the question and was answering the wrong problem that wil cost me
# Dang every new way I can think of solving the actual problem takes a lot of memory space to store all those lists. But if I make it such that they get deleted if they too short then I reduce memory space usage.


def longest_increasing_sub(nums):
    long = 0
    # the store for the lenght of the longest substring

    for i in nums:
        for j in nums:
            if j > i:
                pass
    return None

# Okay so it seems that this won't find the right way either
# Next let's try recursion


def longest_increasing_sub(nums, store=0):
    long = 0

    for i in nums:
        pass
    return None

# that takes up too much processing time which only decreases mu reserves the only option left would be to make a
# class that has a function to call later. The problem with that is I've never made my own class to solve a function
# so let's see how this goes.


class Solution:
    def longest_increasing_set(self, nums):
        # so this will be the function we call to solve the problem
        store = 0
        test = []
        # a space to store test data

        for i in nums:



    def is_Greater(self, compare=store):
        # this will be the tool used to compare the lengths of sets
        if compare > len(self):
            len(self)




print(Solution().longest_increasing_set([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))


# Man I just kept getting caught up in these weird ideas that made sense on the whiteboard but didn't work out as planned.
