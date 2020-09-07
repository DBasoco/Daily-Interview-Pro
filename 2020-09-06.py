# Today we have: Product of Array Except Self
#
# You are given an array of integers. Return an array of the same size where the element at each index is the product
# of all the elements in the original array except for the element at that index.
#
# For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 20, 24].
#
# You cannot use division in this problem.

# Okay so my immediate thought was to use factorial iff the list is given s.t. the entries are sequential and start
# with 1. They clearly thought of this so now I actually have to traverse the list instead of mathing my way out of it.

def products(nums):
    dot = []
    # this is where I will store the dot product

    rock = tuple(nums)
    # this way I don't go messing with the order

    for i in rock:
        # set the element to be used

        nums.remove(i)
        # remove the element from the list not the tuple

        val = 1
        # set val 1 otherwise maths won't work

        for j in nums:
            val = j * val
            # Go through the newly adjusted list

        dot += [val]
        # add the value of the multiplication to the return list

        nums = list(rock)
        # reset the nums from the unaffected list

    return dot


print(products([1, 2, 3, 4, 5]))


# So this method goes through the numbers and doesn't care if they are in sequential order or not. It also makes use
# of the tuple to preserve starting data which is very important for data science and repeat experimentation.
# Although at first this one seemed very daunting it has definitely become one of my favorite problems so far.
