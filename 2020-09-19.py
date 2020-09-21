# Today we have: Jump to the End
#
# Starting at index 0, for an element n in index i, you are allowed to jump at most n indexes ahead. Given a list of
# numbers, find the minimum number of jumps to reach the end of the list.
#
# Example:
# Input: [3, 2, 5, 1, 1, 9, 3, 4]
# Output: 2
#
# Explanation: the minimum number of jumps to get to the end of the list is 2: 3 -> 5 -> 4

# So this makes a very interesting tree pattern. So I need to get to the last index value index(nums[-1]) in the
# fewest moves possible. Where the moves are based on the value I end at. I think I can construct a list or matrix to
# store this information. Since, I can move more than one way. I'm not sure which it'll be. This seems like a heavy
# whiteboard day.

# Alright so this is the construct of the table
# Nums: [3, 2, 5, 1, 1, 9, 3, 4]
# Index: [0, 1, 2, 3, 4, 5, 6, 7]
# Moves: [0, 1, 1, 1, 2, 2, 2, 2]

# First we need to make the moves list arbitrarily large. The moves list is constructed by moving through the
# indexes. At each index we backtrack to each previous index and see the stored num value and move value. Then if the
# num value is greater than or equal to the index value we pull the move value for comparison. Once this is done with
# each of the previous indexes we find the minimum value of all the pulled moves. Then we occupy that index with
# that min move and go to the next index.

import numpy as np


def jumpToEnd(nums):
    moves = np.ones(len(nums))
    moves = 100 * moves
    # instantiate the moves list

    for i in range(0, len(nums)):
        if i == 0:
            moves[i] = 0
            # creates the base case for min values, because if len(nums) was 1 it would take 0 jumps

        else:
            mini = moves[i]
            # so we set the comparison to the current value at index i

            for j in range(0, i):
                # then we go through each previous index

                if nums[j] >= i - j:
                    # if the value at j is greater than the difference between the indices then the jump can be made

                    x = 1 + moves[j]
                    # so we take the moves to get to that spot then add one more move to it

                    mini = min(x, moves[i])
                    # we then compare to find if the new move is smaller than the current minimum

                    moves[i] = mini
                    # update the minimum

    return int(moves[-1]) # return the last entry of moves which stores the least number of moves needed to get to
    # the end


print(jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))


# So this one was really fun. I enjoy the ones that I can work out on a white board first to figure out the basics of
# the code. This makes the refinement process easier as you already know that the logic works you just now need to
# get the right syntax which is trivial for a question like this. I really enjoyed this problem!
