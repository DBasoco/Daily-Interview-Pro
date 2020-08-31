# Today we have: Find the Number of Islands
#
# Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks), count the number of islands
# present in the grid. The definition of an island is as follows:
# 1.) Must be surrounded by water blocks
# 2.) Consists of land blocks(1's) connected to adjacent land blocks (either vertically or horizontally).
# Assume all edges outside of the grid are water.
#
# Example:
# Input:
# 10001
# 11000
# 10110
# 00000
#
# Output: 3

# This sounds super fun. I definitely need a white board to think it over before I start coding. I am certain I will
# need to create my own table or list. Now the interesting thing is that I only need be concerned with the places to
# the left/right and up/down which should make the coding easier.

import numpy as np

class Solution(object):
    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0]) # I cannot tell why this is included in the initial code setup???
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def numIslands(self, grid):
        map = np.array(grid)
        islands = 0
        for i in range(0, len(map)):
            for j in range(0, len(map[0])):
                if map[i][j] == 0:
                    pass
                else:
                    return
    # you know what it may just be easier to construct a whole new map from grid such that I don't have to check all
    # this logic, I'll just have to change my bounds.

# Attempt two

class Solution(object):
    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0]) # I cannot tell why this is included in the initial code setup???
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def numIslands(self, grid):
        map = np.array(grid)
        print(map)
        for i in range(0, len(grid)):
            map[i][0] += 0
            map[i][-1] += 0
            print(map, i)
            # this adds a zero to the front and end
        return map

    # I just figured out why the in range function exists


class Solution(object):
    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def numIslands(self, grid):
        map = np.array(grid)
        islands = []
        pins = []
        for i in range(0, len(map)):
            for j in range(0, len(map[0])):

                if map[i][j] == 0:
                    pass
                else:
                    if [i, j] in pins:
                        pass
                    else:
                        if map[i - 1][j].inRange:
                            top = map[i - 1][j]
                        if map[i + 1][j].inRange:
                            bottom = map[i + 1][j]
                        if map[i][j - 1].inRange:
                            left = map[i][j - 1]
                        if map[i][j + 1].inRange:
                            right = map[i][j + 1]
                        # makes sure that they are in range

                        if top and top == 1:
                            pins += [i - 1, j]
                        if bottom and bottom == 1:
                            pins += [i + 1, j]
                        if left and left == 1:
                            pins += [i][j - 1]
                        if right and right == 1:
                            pins += [i][j + 1]
        return len(islands)


map = [[1, 1, 0, 0, 0],
       [0, 1, 0, 0, 1],
       [1, 0, 0, 1, 1],
       [0, 0, 0, 0, 0]]

print(Solution().numIslands(map))


# So interesting enough the attribute connection is what is throwing me off. I feel that the logic is sound but the
# syntax is wrong.
