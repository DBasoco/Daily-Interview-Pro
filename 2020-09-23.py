# Today we have: Nth Fibonacci Number
#
# THe Fibonacci sequence is the integer sequence defined bu the recurrence relation: F(n) = F(n - 1) + F(n - 2),
# where F(0) = 0 and F(1) = 1. In other words, the nth Fibonacci number is the sum of the prior two Fibonacci
# numbers. Below are the first few values of the sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
#
# Given a number n, print the n-th Fibonacci Number.

# So I've done very similar problems before and I know that the way to best tackle the problem is by constructing the
# full list and calling n place.

import numpy as np


class Solution():
    def fibonacci(self, n):
        fib = np.zeros(n)
        # make a list of all zeros of length n, aka a list with n entries of zero

        fib[1] = 1
        # set the second entry, index 1
        # these steps match the condition F(0) = 0 and F(1) = 1

        for i in range(2, n):
            # this runs over range of the list except for the first two entries so that way we keep the condition

            fib[i] = fib[i - 1] + fib[i - 2]
            # this will replace the current index value, 0 as set in the construction, to the sum of the previous two
            # entries

        return fib[-1]
        # The final entry in fib, denoted as index -1, will be the nth value of the sequence


n = 9

print(Solution().fibonacci(n))
# In order to call the function we must first call the class that the function belongs to

# Of course as I am both familiar with the sequence and similar methods of bottom up construction this problem was
# not overly complex. I still think it is good to go over these types of problems though as they remind me about the
# reason behind certain construction techniques. It is also good clean code practice to see if the comments you leave
# make something that seems easy to you also easy and obvious to someone else reviewing the code.

# I had extra time so went through and found that my computer times out when asked to call any value from the
# sequence beyond the 1477th place.
