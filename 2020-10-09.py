# Today we have: Find Missing Numbers in an Array
#
# Given an array of integers of size n, where all elements are between 1 and n inclusive, find all of the elements of
# [1, n] that do not appear in the array. Some numbers may appear more than once.
#
# Example:
# Input: [4, 5, 2, 6, 8, 2, 1, 5]
# Output: [3, 7]

# The key here to me seems to be that the length of the list determines the values of the list so I have some base
# case situation.

class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        # first we need to know the bonds of the problem [1, n], which we get from the length

        new = []
        # now we create a new list to hold a sorted version of the given numbers

        for x in range(0, n):
            new += [0]
            # fill the new list with zeros
            # this is helpful because the bounds tell us that 0 won't ever be in the given list

        for i in nums:
            new[i - 1] = i
            # next, in one pass, replace the values of new with those given in the list
            # mapping value 1 to index 0 and so forth
            # repeated numbers will be calculated twice but won't ruin the construction

        fin = []
        # create the list to hold the final missing numbers

        for j in range(0, n):
            if new[j] == 0:
                fin += [j + 1]
                # if the value of new is zero, take that index, add one to it, then occupy fin with it
                # the zeros mark the values not found in the original list

            else:
                pass

        return fin


nums = [4, 6, 2, 6, 7, 2, 1]
print(Solution().findDisappearedNumbers(nums))

# This was super fun. I thought of it in reverse terms. If I needed this at the end what would I need before that and
# so forth till I found a point I could reach from the given information. It paralleled my approach to physics
# problems where you know the ending format and you back track ways to get that till the way you backtrack needs the
# givens of the problem. After that it is plug and chug. I'm sure there is another way to find the solution but mine
# uses linear time and space which makes me proud just to know what that even means. 
