# Today we have: Sort Colors
#
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are
# adjacent, with the colors in order red, white and blue.
#
# Here, we wil use the integers 0, 1, and 2 to represent the color res, white, and blue respectively.
#
# Example:
# Input: [2, 0, 2, 1, 1, 0]
# Output: [0, 0, 1, 1, 2, 2]

# So this seems like a greater than less than problem

class Solution:
    def sortColors(self, num):
        sort = num
        # first thought was to construct three separate lists then append but it has to be done in space
        i = 0
        j = 0
        while i < len(num):
            if sort[i] < sort[i + 1]: # move on if the next value is higher but store that place
                i += 1
                j = i
                print(sort, 1) # these are here to see where the infinite loop is coming from

            elif sort[i] == sort[i + 1]: # move up two spots if the value is the same
                i += 2
                print(sort, 2)

            elif sort[i] > sort[i + 1]: # if something is less than send it back to where we had a break
                sort[j] = sort[i + 1]
                j = i - 1
                print(sort, 3)

            else:
                sort[i + 1] = sort[i]
                print(sort, 4)

        i = 0
        while i < len(nums): # this is a second attempt where instead of using <> notation we use % to determine ratios then use <> to distinguish further
            if sort[i] % sort[i + 1] == 0:
                i += 1
                # dang this an have multiple answers in this context
                # this can still work if I add logic <> notation to distinguish the different versions further

            elif sort[i] % sort[i + 1]:

        return sort

# Since they have numeric values maybe I can do boolean for +- certain values

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print('Before Sort: ')
print(nums)

Solution().sortColors(nums)
print('After Sort: ')
print(nums)

# This was way more fun than the previous past days because I could incorporate arithmetic into the problem solving
# instead of simply manipulating binary trees in different ways. I guess that's the mathematician/physicist in me. I also
# ran into some runs that seemed like the while loop was running forever, that's what gave me the thought to move to modulo
# instead of simple boolean logic.
