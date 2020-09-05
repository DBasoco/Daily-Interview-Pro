# Today we have: Merge List of Number Into Ranges
#
#
# Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.
#
# Example:
# Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
# Output: ['0->2', '5->5', '7->11', '15->15']


def findRanges(nums):
    out = []

    for i in range(0, len(nums)):
        con = ''
        if nums[i + 1] == nums[i] + 1: # so this will check if the next entry is consecutive
            pass
        else:
            pass

# I looked at it and I think I want to try a while loop instead of a for

def fingRanges(nums):
    out = []
    con = []
    i = 0
    while i != len(nums):

        if i == 0:
            con += nums[i]
        if nums[i + 1] == nums[i] + 1:
            pass


# so I am having the same issue in my head, the first entry isn't being added
# I am going back to for with one change and an added variable to keep track of my place in the list

def findRanges(nums):
    out = []
    con = ''
    j = 0

    for i in range(0, len(nums)):
        if i == 0:
            con = ''.join(str(nums[i]))
            # add the first entry into the string
        else:
            if nums[i + 1] == nums[i] + 1:
                pass
            else:
                pass


# the problem with that is that the string will then move to index 1 and start working without knowing that index 0
# is even there


def findRanges(nums):
    out = []
    con = ''
    j = 0

    for i in range(0, len(nums)):
        if nums[i + 1] == nums[i] + 1:
            con = ''.join(str(nums[i]))
            # can only join strings
        else:
            con = ','.join(str(nums[i]))
            # this wat the consecutive ones will be separated by a comma so that way I can find them later

    con.split(',')
    # this will split the connectives from the none

    for j in range(0, len(con)):
        # so after the consecutive numbers are organized I'll return the first and last entry with a -> in between
        out += ['%s->%s' % (con[0], con[-1])]

    return out


print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))


# All this one I had to move really fast to get anywhere. I changed up strategies to work out which method would best
# create the solution with the least amount of issues. It was really good to get my hands on the split function again
# after the one yesterday. Using the call notation to rewrite strings is neat trick I just figured out. Again these
# past few days I have been coming up short but my methods and notation of my code to work on proper practice is
# really coming along.
