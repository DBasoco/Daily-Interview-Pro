# Today we have: Convert Roman Numerals to Decimal
#
# Given a Roman numeral, find the corresponding decimal value. Inputs will be between 1 and 3999.
#
# Example:
# Input: IX
# Output: 9
#
# Input: VII
# Output: 7
#
# Input: MCMIV
# Output: 1904
#
# I : 1
# V : 5
# X : 10
# L : 50
# C : 100
# D : 500
# M : 1000

# So we could make some complex logic to traverse the string and return the correct int but it seems that an easier
# method would be to traverse backwards through the string instead. This way we only need to worry if the number in
# the immediate lower index is smaller than the current. If it is we subtract that value if it isn't we add that value.

class Solution():
    def romanToInt(self, s):
        val = 0
        # start off with a valueless int

        roman = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000
                 }
        # create a dictionary that maps all symbols to int values
        # these are the only mappings we need as the others will be generated through logic not a constructed list

        for i in reversed(range(0, len(s))):
            # go backwards over the range of the string

            if i == len(s) - 1:
                val += roman[s[i]]
                # instantiate the first value as the base case

            else:
                # if it isn't the base case

                if roman[s[i]] < roman[s[i + 1]]: # compare value of current char with value of previous char
                    val = val - roman[s[i]]
                    # if the char we are currently on has a mapped value less than the previous we subtract it from
                    # the total

                else:
                    val += roman[s[i]]
                    # if it is larger or the same we add it to the total

        return val
        # return the converted int value


n = 'MCMX'
print(Solution().romanToInt(n))

# I've made functions that convert from binary and hexadecimal to base 10 and base 12 before but this was a
# completely different animal. Fot starters because of the way we read words and numbers we want to go left to right
# through the roman number. But this has a lot of steps that have us going back and redoing calculations. For humans
# this isn't too bad but for a machine code having to repeatedly do calculations is expensive and time consuming. If
# we start from the end, going right to left we find that the calculations are greatly reduced. So I really enjoyed
# this one. Having to use reverse(range()) and dictionaries was a real treat!
