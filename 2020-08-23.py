# Today we have: Longest Substring With K Distinct Characters
#
# You are given a string s, and an integer k. Return the length of the longest substring in s that contains at most k
# distinct characters.
#
# For instance, given the string:
# aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.

# one thing I notice is that order of the distinct characters is not specified, so we can make it discrete

def longest_substring_with_k_distinct_characters(s, k):
    # first we need to turn s into an iterable list
    ls = []
    for i in s:
        ls += i

    # now we create a storage method to build upon
    new = []

    # next we add to new
    best = []
    count = 0

    for i in range(0, len(ls)):  # keep track of distinct characters
        # searching through the list is not a good time saver so we will construct continuously
        if i == 0:  # always add the first one, but as we move and make
            count += 1
            new += ls[i]

        elif ls[i] == ls[i - 1]:  # if it is the same as the last entry, add and move on
            new += ls[i]

        else:  # if it's different add and increase count
            count += 1
            new += ls[i]

        if count == k:
            best += [new]
            print(best)
            count = 0
        # once we hit the count we add the new list to the best list

    return best


print(longest_substring_with_k_distinct_characters('aabcdefff', 3))

# Okay I found where I made my mistake. The range that I run over doesn't get smaller as I progress along so I cannot
# make a proper list unless I correct this bug.
