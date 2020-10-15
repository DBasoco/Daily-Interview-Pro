# Today we have: Design Tic-Tac-Toe
#
# Design a Tic-Tac-Toe game played between two players on an nxn grid. A move is guaranteed to be valid, and a valid
# move is one placed on an emtpy block in the grid. A player who succeeds in placing n of their marks in a
# horizontal, diagonal, or vertical row wins the game. Once a winning condition is reached, the game ends and no more
# moves are allowed. The example game would be too exhaustive to type out.

# This is very similar to my personal project with regards to having a win condition that makes further moves
# impossible.

class TicTacToe(object):
    def __init__(self, n):
        self.GG = False
        self.n = n
        self.mat = []
        # create game condition, store the size of the matrix, build a class matrix

        for i in range(0, n):
            self.mat += [[]]

            for j in range(0, n):
                self.mat[i] += [[]]
        # fill that matrix with the same number of rows and columns, respectfully

        self.mat[0][2] = 'X'
        # make sure the matrix works

    def move(self, row, col, player):
        if self.GG:
            return 'Player %s wins' % player
        # win condition met and result

        else:
            return self.mat, self.mat[0][2]
        # check that I can add to the matrix


# the board is made and I can fill it with pieces, now I just need logic and a measure for ver, hor, and dia


class TicTacToe(object):
    def __init__(self, n):
        self.GG = False
        self.n = n
        self.mat = []

        for i in range(0, n):
            self.mat += [[]]

            for j in range(0, n):
                self.mat[i] += [[]]

    def move(self, row, col, player):
        if self.GG:
            return self.mat, 'Player %s wins' % player

        else:
            if player == 1:
                piece = 'X'
                self.mat[row][col] = piece
            # replace the hole with the piece

            else:
                piece = 'O'
                self.mat[row][col] = piece
            # replace the hole with the piece

            return self.mat
            # see how the board changes


# boom, from that I can see that first it will be easiest to check hor first, then ver, then dia (which will only be
# two checks vs. the others which grow linearly with the size of n)
# I wonder if I can speed up the checks as more moves happen, but that may be getting ahead of myself lol


class TicTacToe(object):
    def __init__(self, n):
        self.GG = False
        self.n = n
        self.mat = []

        for i in range(0, n):
            self.mat += [[]]

            for j in range(0, n):
                self.mat[i] += [[]]

    def move(self, row, col, player):
        if self.GG:
            return self.mat, 'Player %s wins' % player

        else:
            if player == 1:
                piece = 'X'
                self.mat[row][col] = piece

            else:
                piece = 'O'
                self.mat[row][col] = piece

            # for hor to be true a whole row must be identical
            # for ver to be true a whole col must be identical
            # for dia to be true matching pairs(i.e. (0,0) (1,1) (5,5) etc) OR all pairs whose index values sum to
            # n(i.e. (0,n) (n,0) (2,n-2) etc)

            for


board = TicTacToe(3)
board.move(0, 0, 1)
board.move(0, 2, 2)
board.move(2, 2, 1)
board.move(1, 1, 2)
board.move(2, 0, 1)
board.move(1, 0, 2)
print(board.move(2, 1, 1))

# Dang this was a really fun one but I kept thinking that a more efficient way to check win conditions was to store
# player moves instead of constantly checking the board state. This would eliminate a lot of logic steps which eats up
# processing power and more importantly time. The exit conditional would be easy if any of the conditions were to be
# satisfied just set self.GG to True and then call the function again with arguments none and just the player.

