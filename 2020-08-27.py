# Today we have: Ways to Traverse a Grid
#
# You are given 2 integers n and m representing an n by m grid, determine the number of ways you can get from the
# top-left to the bottom-right of the matrix by going right or down.
#
# Example:
# n=2, m=3
#
# This should return 2, since the only possible routes are:
# Right, down
# Down, right

# Okay the best way to do this would be find the base case and build a table that stores the moves for previous slots
# to use for the next slot.

# Used a whiteboard to run through some easy examples to get visualize what I needed the code to do

import numpy as np
# numpy already has rules for matrices, so why reinvent the wheel


def num_ways(n, m):
    mat = np.ones((n, m))
    # make a matrix to store data
    # since the base case is one we instantiate the matrix as all ones so we don't have to populate these spaces later.

    for i in range(0, n):
        # run through each row

        for j in range(0, m):
            # run through each column in that row

            if i == 0:
                pass
            elif j == 0:
                pass
            # if we have a base case we leave it as is

            else:
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
            # if we are anywhere else on the matrix we take the value above and to the left, then add them together

    return print('%dx%d:' % (n, m), int(mat[n - 1][m - 1]))


num_ways(2, 2)
num_ways(2, 23)
num_ways(10, 4)
num_ways(9, 5)

# I finished this one way faster than I expected. I even took some time after to make the results easy to read. I'm
# not surprised, given my physics background, that this matrix problem was easier for me than the binary tree ones
# the past few days.
