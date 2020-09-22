# Today we have: Max and Min with Limited Comparisons
#
# Given a list of numbers of size n, where n is greater than 3, find the maximum and minimum of the list using less
# than 2 * (n - 1) comparisons.

# This seems like one of those puzzle problems where you are trying to leave the cave given so many paths or when you
# need to find the fake coin out of a given amount.

# I am also thinking about this meaning comparison because if I do a "difference" approach wherein I simply find the
# numbers with the greatest distance between them then return the numbers I have found the min and max without doing
# any comparison except those done between deltas.

def find_min_max(nums):
    mini = nums[0]
    maxx = nums[-1]
    # arbitrarily set the min and max to the first and last values

    for i in range(1, len(nums)): # this will cover the minimum value
        d = mini - nums[i]
        # if this is positive then i is smaller

        if d > 0:
            mini = nums[i]
            # my one concern is that this is technically comparing the difference to 0 which may add up if I'm not
            # careful

    for i in range(0, len(nums) - 1): # this will cover the maximum value
        d = maxx - nums[i]
        # if this is negative then i is larger

        if d < 0:
            maxx = nums[i]
            # I do this twice now but I only go over the set that excludes the current max/min so it should have 2 *
            # (n - 1) comparisons which is still in range

    ans = ()
    ans += mini, maxx
    return ans


print(find_min_max([3, 5, 1, 2, 4, 8]))
print(find_min_max([3, 5, 2, 4, 8, 1]))

# This was less daunting than I imagined. I simply had to think about what it meant for a value to be bigger or
# smaller than anther value. After that, I only needed to change the bounds for which I traversed to insure that I
# was within my restraints. I again enjoyed this one very much.
