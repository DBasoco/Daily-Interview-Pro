# Today we have: Reverse Words in a String
#
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving
# whitespace and initial word order.
#
# Example:
# Input: 'The cat in the hat'
# Output: 'ehT tac ni eht tah'
#
# Note: In the string, each word is separated by a single space and there will not be any extra space in the string.

class Solution:
    def reverseWords(self, words):
        x = words.split()
        # separate the words from whitespace and put them into a list

        for i in x:
            # pull words from list

            for j in range(0, len(i)):
                # so how we reorder the string is weird since it isn't a simple replace
                i.replace(i[j], i[-1])
        return x


# let's try this again
class Solution:
    def reverseWords(self, words):
        x = words.split()
        # separate the words from whitespace and put them into a list

        z = ''

        for i in x:
            # pull words from list
            rev = []
            for j in i:
                rev += [j]
            # turns it into a list

            for k in range(0, len(i)):
                rev[-(k + 1)] = i[k]
                # reverse the list
            print(rev)

            z = ''.join(rev)
            print(z)
            # turn to string and join to final answer

        return z


# okay so now I have an issue with the join and rewriting the final answer

class Solution:
    def reverseWords(self, words):
        x = words.split()
        # separate the words from whitespace and put them into a list

        for i in x:
            # pull words from list

            rev = []
            z = ''
            for j in i:
                rev += [j]
                # turns it into a list

            for k in range(0, len(i)):
                rev[-(k + 1)] = i[k]
                # reverse the list
            print(rev)

            z = ''.join(rev)
            # turn to string and join see I  need to then join this z to a final string but it isn't liking anything
            # that I am trying which is really annoying

        return z


print(Solution().reverseWords('The cat in the hat'))

# This was a fun test in maintaining the integrity of your initial input which can be corrupted later if you aren't
# careful. It even made me consider using tiples but I never got to execute that plan.
