# Today we have: Find the Single Element in an Array of Duplicates
#
# Given an array of integers, arr, where all numbers occur twice except one number which occurs once,
# find the number. Your solution should ideally be O(n) time and use constant extra space.
#
# Example:
# Input: arr = [7, 3, 5, 5, 4, 3, 4, 8, 8]
# Output: 7

# This seems like it may relate to the maths definition of an even number.
#
# Consider that an even number is defined as being divisible by 2 such that: 2 * a = b, where a and b are in the set
# of positive whole numbers. This can be written as: a + a = b. This is relevant since each number will appear twice
# except for one. Therefore, under the postulate that any two even numbers when summed together will still be even we
# can pull out the odd number by the exclusion.
#
# I'm not sure if this is entirely the case but it would allow is to run in O(n) time and constant space. So let's
# take it to the whiteboard.

# So the total of the list has to be be: tot = N + x. Where N is even(2 * a) and x is odd or even.
# Iff total is odd then x is odd, and iff total is even then x is even.



class Solution(object):
    def findSingle(self, nums):
        tot = 0
        for i in nums:
            tot += i
        # sum up the whole of the array linearly

        # now we see if the number is even or odd
        # the process is the same for both but the construction is slightly different
        # x % 2 = 0 means that the number x is even, by definition: 2 * a = b

        if tot % 2 == 0:
            # if the total is even then the number that is singular must be even as well

            even = []
            # make a new list for just the even numbers

            for i in nums:
                if i % 2 == 0:
                    even += [i]
                else:
                    pass
            # linearly move through the list of nums and pull just the even numbers out

            out = 0
            print(even)
            # set output to 0

            for i in range(0, len(even)):
                if i % 2 == 0:
                    out += even[i]
                else:
                    out += -(even[i])
            # since the length of just the

            return abs(out)

        else:
            odd = []
            for i in nums:
                if not i % 2 == 0:
                    odd += [i]
                else:
                    pass

            out = 0

            for i in range(0, len(odd)):
                if i % 2 == 0:
                    out += odd[i]
                else:
                    out += -(odd[i])

            return abs(out)


nums = [1, 6, 8, 4, 4, 5, 6, 5, 1]


# I moved the order of the values around from [1, 1, 8, 4, 4, 5, 6, 5, 6] to [1, 6, 8, 4, 4, 5, 6, 5, 1] just to see
# if the maths work out for different orderings. I discovered that my alternating method of generating the singular
# even/odd number is inherently dependent on whether or not the values comes back to back. If this wasn't the case
# then we would have simply used this method on the initial array of numbers. A new function will have to be used to
# delineate the singular value from the even/odd list.

class Solution(object):
    def findSingle(self, nums):
        tot = 0
        for i in nums:
            tot += i

        if tot % 2 == 0:

            even = []

            for i in nums:
                if i % 2 == 0:
                    even += [i]
                else:
                    pass

            out = 0
            print(even)

            # what can replace this method?
            for i in range(0, len(even)):
                if i % 2 == 0:
                    out += even[i]
                else:
                    out += -(even[i])

            return abs(out)

        else:
            odd = []
            for i in nums:
                if not i % 2 == 0:
                    odd += [i]
                else:
                    pass

            out = 0

            for i in range(0, len(odd)):
                if i % 2 == 0:
                    out += odd[i]
                else:
                    out += -(odd[i])

            return abs(out)


nums = [1, 6, 8, 4, 4, 5, 6, 5, 1]

print(Solution().findSingle(nums))

# Well I couldn't solve the hangup and keep it within my current postulate. Therefore, the postulate is wrong. At
# this point I would fall back to bottom up construction looking for a branching pattern that I could then find the
# base case of to build a linear list. Even though I didn't finish this problem the idea I had got me really excited
# but it is important to not force an idea that is wrong just because you personally like it.
