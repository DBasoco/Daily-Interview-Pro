# Today we have: Plus One
#
# Given a non-empty array where each element represents a digit of a non-negative integer,
# add one to the integer. The most significant digit is at the front of the array and each element in the array
# contains only one digit. Furthermore, the integer does not have leading zeros, except in the case of the number '0'.
#
# Example:
# Input: [2, 3, 4]
# Output: [2, 3, 5]

# So I'm thinking of converting this to a string then into an integer the back into a string then back into a list.


class Solution():
    def plusOne(self, digits):
        if digits == [0]:
            return [1]
            # if we have zero we just return 1

        else:
            numstr = ''
            # this will be the separator for the join function

            numls = []
            # list of string numbers from digits

            for i in digits:
                numls += ['%s' % i]
                # turn each integer in digits into a string and add it in order

            number = int(numstr.join(numls))
            # join the iterable list into an integer

            number += 1
            # add one to it

            string = str(number)
            # revert back to string

            fin = []
            # final list to be returned

            for j in string:
                fin += [int(j)]
                # go through the string add the integer version of value into the final list

            return fin


num = [2, 9, 9]
print(Solution().plusOne(num))

# This was basically a test of data conversion. To make sure you knew what you can do with each data type and how to
# go between them. I found it easy to do this method. I'm sure there is a harder logic version to do about doing this
# but using memory space instead of wasting processing on time seems like the better tradeoff to me for this problem.
# Although it was easy I still liked going through and working with the string type as it isn't one I usually have to
# concatenate.
