# Today we have: Filling Up Puddles
# You have a landscape, in which puddles can form. You are given an array of
# non-negative integers representing the elevation at each location. Return the amount of water the would accumulate
# if it rains.


# Okay I'm going to need a white board to work this out as it looks like I'll need to create a table to store
# information so it doesn't take forever.

# So it seems like row by row is the way to work through this problem

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# okay I'm thinking a few things here:
# 1 we could build this matrix or simply compare numbers then remove them after we use them


def capacity(array):
    ls = array
    count = 0
    for i in range(ls):
        try:
            if ls[i] >= ls[i+1]:
                if i == len(ls) - 1:
                    pass                # this is to stop it from counting if
                else:
                    count += 1
            else:
                pass
        except IndexError:
            pass

# wait this won't work I need to disassemble the array as I go along otherwise I'll have to add ridiculous logic

# ROUND 2: FIGHT


def capacity(array):
    ls = array                          # make a copy so we don't destroy original
    count = 0
    for j in range(0, ):             # I need a way to find the max value in the array easily
        for i in range(len(ls)):        # so I run through each row going bottom up then I delete the base and move up
            if ls[i] == 0 and (ls[i] is not ls[0] or ls[-1]):
                count += 1              # add a count for every 0 found except for those on the ends
            else:
                pass
        ls = ls - 1
        if


print(capacity(arr))
