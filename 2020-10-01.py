# Today we have: Permutations of Numbers
#
# You are given an array of integers. Return all the permutations of this array.

# So this means I have to use the permutation formula to determine the length of the final answer then occupy that
# answer with the subsets.
#
# P(n, r) = n!/(n - r)!
# So for three options and three slots I have 6 permutations

import math
# I can import a library here help but let's try and make a script to do this for us


def permute(nums):
    sec = tuple(nums)
    # tuple so we don't delete data

    n = len(sec)
    factor = 1
    # since n = r we just need to get the factorial of n which is the length of the nums, we the the factor to 1
    # since 0! = 1

    for i in range(1, n + 1):
        # we start at 1 since 0 is built into the factor, and we end at n + 1 because otherwise the final number
        # wouldn't be included

        factor = factor * i
        # multiple by itself

    perm = []
    # create the list to contain the permutations

    for i in range(0, factor):
        pass

    return factor

# I think this method of using the permutation equation to establish a set time to go over isn't correct.

# wait what if I just move two of the entries at a time and then loop at end till is over


def permute(nums):
    n = len(sec)
    factor = 1
    for i in range(1, n + 1):
        factor = factor * i
    perm = []
    x = 0

    nex = nums

    for i in range(0, factor):
        perm += nex

        if x != len(nums) - 1:


        else:
            # loop

    return None


print(permute([1, 2, 3]))

# Ran out right when I was getting somewhere with the approach. Well this did have me stooped for a second but I enjoyed struggling on the white board looking for a method that would work. A big hint was how the given answers appeared when they were returned. This helped me realize the pattern used so that I could reverse it.
