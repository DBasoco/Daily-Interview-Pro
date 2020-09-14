# Today we have: Reverse Integer
#
# Write a function that reverses the digits a 32-bit signed integer, x. Assume that the encironment can only store
# integers within the 32-bit signed integer range, [-2^31, 2^31 - 1]. The function returns 0 when the reversed
# integer overflows.
#
# Example:
# Input: 123
# Output: 321

class Solution:
    def reverse(self, x):
        if abs(x) >= 2**31:
            return 0
        # if it is beyond the space given don't fill the memory just return 0

        else:
            y = str(x)
            z = []
            final = ''
            # transition variables

            for i in y:
                z.insert(0, i)
                # take the string entries and put them in a list of reverse order

            for j in z:
                final += j
                # take that list and combine it into a new string

            return final


print(Solution().reverse(123))
print(Solution().reverse(2**31))

# So this is of linear time, I just wonder if it could have been done with fewer steps to cut it down.












