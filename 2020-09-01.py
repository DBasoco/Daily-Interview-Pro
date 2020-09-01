# Today we have: Group Words that are Anagrams
#
# Given a list of words, group the words that are anagrams of each other. (An anagram are words made up of the same
# letters).
#
# Example:
#
# Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
# Outputs: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]

# So my first thought is if the list will always be of three length and/or the same length.
# 1.) if they are of different length then I can easily organize them
# so different lengths aren't compared to save on time
# 2.) if they are of different length I need to think of a way to randomize the order of a set
# 3.) I have no idea what collections does so time to read

# I'll try to address all these issues but only if I have the time. Going off that they are always length three

import collections
# honestly I can't figure out how to use this module in such a short time. I will have to defer today's daily question. I apologize.

def groupAnagramWords(strs):
    for i in range(0, len(strs)):

        

print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))