# Today we have: Circle of Chained Words
#
# Two words can be 'chained' if the last character of the first word is the same as the first character of the second
# word. Given a list of words, determine if there is a way to 'chain' all the words in a circle.
#
# Example:
# Input: ['eggs', 'karat', 'apple', 'snack', 'tuna']
# Output: True
# Chain: eggs, snack, karat, tuna, apple

# So really all I care about is the first and last letter of each word, and I need some 1/0 statement for each entry
# to keep track of what has been added to the chain link.

# I really need to learn more about this collections library. It has come up too many times to not be relevant to
# future work.

from collections import defaultdict


# So this will let me store key value pairs into a dictionary, thus creating the 1/0 marker I thought I needed.


def chainedWords(words):
    d = defaultdict(set)
    for i in words:
        d[i].add(1)
        # testing to see what list, int and set all do to pick which one fits the boundary conditions of the problem

    return d.items()


# So what I should do is use the set dict then cycle through the list of items and words. If we have a chain
# connection I add it to the d.items if not just keep going. The way the set seems to work is that once a value is
# put in it can't be replicated which as an interesting system to subvert in this situation.


def chainedWords(words):
    d = defaultdict(set)
    # dict init with nothing thus far
    for i in words:
        d[i].add(0)
        # fill the items with the values then set them to 0 meaning that they don't yet have a pair
        # another option to try would be to fill it up as I traverse the words
    print(d['apple'])
    print(words[0])
    print(words[0][-1])
    print(words[:])
    for j in range(0, len(words)):
        if words[j][-1] == words[:][0]:
            if j[0] == words[:][-1]:
                d[j].add(1)

    return d.items()


print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))

# So i ran out of time learning about what the different syntax and construction methods for defaultdict were. I
# almost got to the point of testing my first logic method but I ran out of time during the comparison. My slicing
# method was having issues with syntax but if I had gotten it to work it would have saved a lot coding in the future
# defining for loops to cycle through each letter.
