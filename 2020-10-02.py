# Today we have: Longest Consecutive Sequence
#
# You are given an array of integers. Return the length of the longest consecutive elements sequence in the array.
#
# For example, the input array [100, 4, 200, 1, 3, 2] has the longest consecutive sequence 1, 2, 3, 4, and thus,
# you should return its length, 4.

def longest_consecutive(nums):
    long_con = []

    for i in range(0, len(nums)):

        tmp = []
        tmp += [nums[i]]
        print(nums[i])

        for j in range(0, len(nums)):

            if nums[i] + 1 == nums[j]:
                tmp += [nums[j]]

            if nums[i] - 1 == nums[j]:
                print(tmp, 'Before')
                tmp.insert(tmp.index(nums[i]), nums[j])
                print(tmp, 'After')

        if len(tmp) > len(long_con):
            long_con = tmp

    return long_con


# This has the flaw that it doesn't include relevant entries that come before the lowest value in the sequence


def longest_consecutive(nums):
    long_con = []

    for i in range(0, len(nums)):
        tmp = []
        tmp += [nums[i]]

        for j in range(0, len(nums)):
            if nums[i] + 1 == nums[j]:
                tmp += [nums[j]]

            if nums[i] - 1 == nums[j]:
                tmp.insert(tmp.index(nums[i]), nums[j])

        if len(tmp) > len(long_con):
            long_con = tmp

    return long_con


print(longest_consecutive([100, 4, 200, 1, 3, 2]))


