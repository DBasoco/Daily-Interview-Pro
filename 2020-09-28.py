# Today we have: Make the Largest Number
#
# Given a number of integers, combine them so it could create the largest number.
#
# Example:
# Input: [17, 7, 2, 45, 72]
# Output: 77245217

# So I basically compare the first number you encounter at each entry to compare to find the biggest. Then place that
# number first, remove it, then run it again.


def largestNum(nums):
    big = ''
    for i in range(0, len(nums)):
        print(nums)

        x = nums.index(max(int(str(nums[j])[0]) for j in range(0, len(nums))))
        # so here I want to pull out j not just the index of the largest number to come across

        big += str(nums[x])
        nums.remove(nums[x])

        print(big)

    return None


# Let's try dictionaries to store the place value


def largestNum(nums):
    big = ''
    for i in range(0, len(nums)):
        x = {i: 0 for i in nums}
        for i in range(0, len(nums)):
            if i == 0:
                x[0] = 0
            else:
                x[i] = x[i - 1] + 1
        print(x)

    return None


print(largestNum([17, 7, 2, 45, 72]))

# Wow this ones complexity was way more intense. The way the built the biggest number required that only the first
# number encountered in an entry would be compared for biggest present. All the techniques I know simply weren't
# robust enough to account for this evaluation method. I tried to make one that would work but upon seeing the
# shortcomings, I moved on to another method that had different issues, which just ate all my time up.
