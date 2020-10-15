# Today we have: Top K Frequent Words
#
# Given a non-empty list of words, return the k most frequent words. The output should be stored from highest to
# lowest frequency, and if two words have the same frequency, the word with lower alphabetical order comes first.
# Input will contain only lower-case letters.
#
# Example:
# Input: ['daily', 'interview', 'pro', 'pro', 'for', 'daily', 'pro', 'problems'], k = 2
# Output: ['pro', 'daily']

# I'm feeling dictionaries to store the data than pull the top results into a list of length k

class Solution(object):
    def topKFrequent(self, words, k):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        # lowercase letters for comparing the alphabetical first

        tally = {}
        # the dictionary to tally up the occurrence of words

        for i in words:
            if i in tally:
                tally[i] += 1
            else:
                tally[i] = 0
        # fill the dictionary with the counts of each appeared entry

        top = []
        # list to hold the top entries

        for j in range(0, k):
            top += ['']
            # list length k

        for m in tally:
            for n in range(0, k):
                if top[n] == '':
                    top += [k]

                else:
                    top[n] = tally[max(k, tally[top[n]])]
        # find the top by comparing new entries against current values in list

        return tally, top


# my method of creating the top list from the dictionary is not correct in syntax and logic


class Solution(object):
    def topKFrequent(self, words, k):
        letters = 'abcdefghijklmnopqrstuvwxyz'

        tally = {}

        for i in words:
            if i in tally:
                tally[i] += 1
            else:
                tally[i] = 1

        top = []

        ex = list(tally)

        maxi = ''

        for x in range(0, k):
            for i in ex:
                if maxi == '':
                    maxi = i

                else:



        return tally, top


words = ['daily', 'interview', 'pro', 'pro', 'for', 'daily', 'pro', 'problems']
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']

# This seemed easier on paper. I never figured a way to evaluate the entries without just returning a value. In theory I
# imagine using the max() and pop() functions to generate the final list of top entries.
