# Today we have: Min Range Needed to Sort
#
# Given a list of integers, return the bounds of the minimum range that must be sorted so that the whole list would
# be sorted.
#
# Example:
# Input: [1, 7, 9, 5, 7, 8, 10]
# Output: (1, 5)
#
# Explanation: The numbers between index 1 and 5 are out of order and need to be sorted.

# Some assumptions that I will use: the list will only need to be sorted over a continuous range. This will let me
# only have to worry if a number is out of sorts once not twice.

# So we need to keep track of what the largest and smallest number is and what index it is.

def findRange(nums):
    lil = 0
    big = 0
    # these will be used for reference

    sort = [lil, big]
    # this will be a list later to be a tuple that stores the value lil and big

    for i in range(0, len(nums)):
        if nums[i] < lil:
            lil = nums[i]
        if nums[i] > big:
            pass

    return tuple(sort)


# Before the markers are changed I need to see if the system is in fact out of order, because if it is ordered than
# the issue is mute


def findRange(nums):
    lil = [0, 0]
    big = [0, 0]
    # okay we will store the value and the index
    # if the answer is sorted already than we should get (0, 0) back

    for i in range(0, len(nums)):
        if i == len(nums) - 1:
            pass
            # the last number can't be compared
        else:
            if nums[i] > nums[i + 1]:
                x = nums.index(i)
                return None

    # you don't need to construct sort until after lil and big are set
    return tuple(sort)


# So I need a carry through to find when to cut off the max by storing the highest value encountered in the set that
# needs to be sorted. And I need to use the max() min() functions so that I am not using excess logic.


def findRange(nums):
    lil = [0, 0]
    big = [0, 0]
    carry = 0
    # these will be used for reference

    for i in range(0, len(nums)):
        if nums[i] > carry: # so if we need to progress the carry for the largest number we can
            carry = nums[i]
            # replace the carry value

            lil[0] = max(lil[0], nums[i])
            lil[1] = nums.index(lil[0])
            # adjust the start of the range

            big[0] = max(big[0], nums[i])
            big[1] = nums.index(big[0])
            # adjust the end of the range

        else: # if the value wouldn't end the range than we do this
            lil[0] = max(lil[0], nums[i])
            lil[1] = nums.index(lil[0])

            big[0] = max(big[0], nums[i])
            big[1]
            nums.index(big[0])

    sort = [lil[0], big[0]]
    return tuple(sort)


print(findRange([1, 7, 9, 5, 7, 8, 10]))

# This one was interesting to set the necessary variables needed to solve. It took me awhile to figure out how many
# were needed to properly solve the problem. Based off of where I got using this method three variables are needed to
# solve the problem. Which gives the function very efficient memory space.





















