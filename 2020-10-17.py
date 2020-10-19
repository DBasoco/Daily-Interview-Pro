# Today we have: Spreadsheet Column Title
#
# MS Excel column titles have the following pattern: A, B, C, ..., Z, AA, AB, ..., AZ, BA, BB, ..., ZZ, AAA, AAB,
# ... etc. In other words, column 1 is named 'A', column 2 is 'B', column 26 is 'Z', column 27 is 'AA' and so forth.
# Given a positive integer, find its corresponding column name.
#
# Examples:
# Input: 26
# Output: Z
#
# Input: 51
# Output: AY
#
# Input: 676
# Output: YZ
#
# Input: 704
# Output: AAB

# So this is just a base 26 situation, instead of base two or base twelve. From the whiteboard we are looking at the
# summation of x_i * 26**n_i, where n_i is the place in the number and x_i is in letters.

class Solution:
    def convertToTitle(self, n):
        #letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        letdic = {
            1: 'A',
            2: 'B',
            3: 'C',
            4: 'D',
            5: 'E',
            6: 'F',
            7: 'G',
            8: 'H',
            9: 'I',
            10: 'J',
            11: 'K',
            12: 'L',
            13: 'M',
            14: 'N',
            15: 'O',
            16: 'P',
            17: 'Q',
            18: 'R',
            19: 'S',
            20: 'T',
            21: 'U',
            22: 'V',
            23: 'W',
            24: 'X',
            25: 'Y',
            26: 'Z'
        }
        # make a dictionary to easily call the key value once found

        if n <= 26:
            return letdic[n]
        # no need for logic in the base case just return the key value

        else:
            n_mod = n / 26
            n_div = n_mod % 26
            n_set = n_div % 26
            n_next = n_set % 26
            # searching for a way to determine the periodicity of the function or the n

        return n_mod, n_div, n_set, n_next, (52 / 26)


# so the mod case is throwing me off because of how I'm use to encountering 0's when ever I move up by a factor of one
# I'm thinking this might need some kind of recursion where the final answer is a string
# going from letters to numbers would be WAY easier
# I need a way to determine the max n_i required to solve the problem

import math


class Solution:
    def convertToTitle(self, n):
        #letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        letdic = {
            1: 'A',
            2: 'B',
            3: 'C',
            4: 'D',
            5: 'E',
            6: 'F',
            7: 'G',
            8: 'H',
            9: 'I',
            10: 'J',
            11: 'K',
            12: 'L',
            13: 'M',
            14: 'N',
            15: 'O',
            16: 'P',
            17: 'Q',
            18: 'R',
            19: 'S',
            20: 'T',
            21: 'U',
            22: 'V',
            23: 'W',
            24: 'X',
            25: 'Y',
            26: 'Z'
        }
        if n <= 26:
            return letdic[n]

        else:
            i = n % 26

            if i == 0:
                # when i is zero we are dealing with a multiple of 26
                n_r = math.remainder(n, 26)

                if n_r == 0:
                    nf = n / 26

            else:
                n_r = math.remainder(n, 26)

                n_i = (n - n_r) / 26

                nf = Solution().convertToTitle(n_i)

                nf += Solution().convertToTitle(n_r)
                # this was a test to see if recursion was an applicable approach to this solution

        return nf


input1 = 1
input2 = 456976
input3 = 704
print(Solution().convertToTitle(input1))
print(Solution().convertToTitle(input2))
print(Solution().convertToTitle(input3))

# Well from the run scenarios it seems that recursion was the way to go with this one. Sorry I spent way to much time
# making the dictionary as I first made the str values the key not the int values which ate up a lot of time going
# back and correcting. Although it is clear that recursion is the way to go about this with the base being a value
# less than 26, the construction still eludes me. My next step would be to test more math cases to find a way to
# determine and carry the n_i factor along. If that isn't needed as I predict with the recursion approach then I
# would throw up a recursion where we get the gcd for all i in 26 and use that to determine x_i then recur and
# multiple.
