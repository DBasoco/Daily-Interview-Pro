# Today we have: 3 Sum
#
# Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) in nums such that a + b +
# c = 0. Note that there mau not be any triplets that sum to zero in nums, and that the triplets must not be
# duplicates.
#
# Example:
# Input: nums = [0, -1, 2, -3, 1]
# Output: [0, -1, 1], [2,, -3, 1]

# Okay so this seems really interesting. My first thought is obviously check each number combo. Let's work it out on
# a white board to see the logistics since we can't have any repeats. See I think that caveat is what makes this a
# possible method.

# So it seems like an n choose m situation with an added caveat so we aren't just using all the range

class Solution(object):
    def threeSum(self, nums):
        num = nums
        trip = []
        i = 0
        while i < len(num) - 2:
            a = num[i]
            b = num[i + 1]
            for j in range(i + 2, len(num)):
                c = num[j]
                if a + b + c == 0:
                    trip += [[a, b, c]]
                else:
                    pass
            i += 1
        return trip

# Okay so this code works but only for small values n

# Attempt number 2
class Solution(object):
    def threeSum(self, nums):
        num = nums
        tri = []
        i = 0
        while i < len(num) - 2:
            a = num[i]
            for j in range(i + 1, len(num)):
                b = num[j]
                # added this extra for step to compare every possible number
                for k in range(i + 2, len(num)):
                    c = num[k]
                    if a + b + c == 0:
                        tri += [[a, b, c]]
                    else:
                        pass
            i += 1
        return tri

# So this works but the issue is that it still produces repeat numbers

class Solution(object):
    def threeSum(self, nums):
        num = nums
        tri = []
        i = 0
        while i < len(num) - 2:
            print(i)
            a = num[i]
            for j in range(i + 1, len(num)):
                b = num[j]
                # added this extra for step to compare every possible number
                for k in range(i + 2, len(num)):
                    c = num[k]
                    if a + b + c == 0:
                        new = [[a, b, c]]
                        if not tri:
                            tri += new
                            print(tri)
                        elif new in tri:
                            print('Next')
                            pass
                        else:
                            tri += new
                            print('oops')
                            # so some type of infinite loop is happening here, every repeat oops is a mistake
                    else:
                        pass
            i += 1
        return tri


# Let's fix that weird issue of repeats


class Solution(object):
    def threeSum(self, nums):
        num = nums
        tri = []
        i = 0
        while i < len(num) - 2:
            print(i)
            a = num[i]
            for j in range(i + 1, len(num)):
                b = num[j]
                # added this extra for step to compare every possible number
                for k in range(i + 2, len(num)):
                    c = num[k]
                    if a + b + c == 0:
                        new = [[a, b, c]]
                        if not tri:
                            # place into empty set
                            tri += new
                        else:
                            for n in range(0, len(tri)):
                                # check to see if the new triple is in the final already
                                if new == [tri[n]]:
                                    pass
                                else:
                                    tri += new
                    else:
                        pass
            i += 1
        return tri


nums = [0, -1, 2, -3, 1]
print(Solution().threeSum(nums))
nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))
nums = [1, -2, 1, 0, 5, -3, -4, 0, -1, 7]
print(Solution().threeSum(nums))

# I was so close to cracking this one without using the search method. I also decided to use some version control on
# this one, so I could freely comment sections that I tried and failed with so that way I didn't bring them back in
# later versions. It also helps to see how my thinking is moving along as I encounter new bugs. Next time I'll use
# this same version control, I just hope I don't create such a convoluted logic tree as this one. I'll use more
# try/except code tomorrow.
