# Today we have: Buddy Strings
# Given two strings A and B of lowercase letters, return true if and only if we can swap
# two letters in A so that the result equals B.

# Example:
#   A = "ab", B = "ba" True
#   A = "ab", B = "ab" False
#   A = "aa", B = "aa" True
#   A = "", B = "aa" False

print(len('aaaaab')) # test to make sure str have length stores


class Solution():
    def buddyStrings(self, A, B):
        mark = 0                        # marker to see if one switch is all that is needed
        if len(A) == len(B) is False:
            return False                # nothing can be done if they have different lengths
        else:
            a = []
            b = []
            # turn str into lists so I can run through them for comparison
            for i in A:
                a.append(i)
            for i in B:
                b.append(i)
            for i in range(0, len(A)):
                # so now we go through each list item and compare
                if A[i] == B[i]:
                    pass
                else:
                    mark += 1         # we count every mistake
        # if the number of mistakes is 2, then we only have to switch two str entries
        # now I need to account for aa = aa & ab = ab conditionals
        if len(A) == 2 and a[0] == a[1]:
            return True                     # if the str's are two of the same char return true
        else:
            if mark == 2:
                return True
            else:
                return False


print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))  # true
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))  # false


# extra tests

print(Solution().buddyStrings('ab', 'ab'))                # false
print(Solution().buddyStrings('aa', 'aa'))                # true
print(Solution().buddyStrings('ab', 'ba'))                # true
