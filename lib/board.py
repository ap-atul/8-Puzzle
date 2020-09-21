"""
Class to store the board config and total moves
and previous state of the board to avoid the
cycle
"""


class Board:
    def __init__(self, board, move=0, previous=None):
        """
        board is a list
        move no of total moves to solve
        previous the state of board before moves
        """
        self.board = board
        self.move = move
        self.previous = previous

    def __str__(self):
        """
        fancy printing on the terminal for board
        """
        string = ''
        string = string + '+---+---+---+\n'
        for i in range(3):
            for j in range(3):
                tile = self.board[i * 3 + j]
                string = string + '| {} '.format(' ' if tile == 0 else tile)
            string = string + '|\n'
            string = string + '+---+---+---+\n'
        return string

    def clone(self):
        """
        making a copy to store the previous and
        increment the moves
        """
        return Board(self.board.copy(), self.move + 1, previous=self)

    def getBlank(self):
        """
        index of the blank space i.e. 0 no
        """
        return self.board.index(0)

    def swap(self, source, destination):
        """
        swap space with tile selected
        """
        self.board[source], self.board[destination] = self.board[destination], self.board[source]

    def moveBlank(self, direction):
        """
        make a move and swap the space with
        a tile, based on the direction
        """
        blank = self.getBlank()

        if direction == "LEFT":
            if blank % 3 != 0:
                col = (blank % 3) - 1
                row = int(blank / 3)
                self.swap(row * 3 + col, blank)

        if direction == "RIGHT":
            if blank % 3 != 2:
                col = (blank % 3) + 1
                row = int(blank / 3)
                self.swap(row * 3 + col, blank)

        if direction == "UP":
            if int(blank / 3) != 0:
                col = (blank % 3)
                row = int(blank / 3) - 1
                self.swap(row * 3 + col, blank)

        if direction == "DOWN":
            if int(blank / 3) != 2:
                col = (blank % 3)
                row = int(blank / 3) + 1
                self.swap(row * 3 + col, blank)

    def getNeighbours(self):
        """
        get direction where the move can be made
        return: a list of all neighbours
        If it cannot move is any dir, it is not added
        to the list
        """
        blank = self.getBlank()
        neighbours = []

        # left?
        if blank % 3 != 0:
            newBoard = self.clone()
            newBoard.moveBlank('LEFT')
            neighbours.append(newBoard)

        # right?
        if blank % 3 != 2:
            newBoard = self.clone()
            newBoard.moveBlank('RIGHT')
            neighbours.append(newBoard)

        # up?
        if int(blank / 3) != 0:
            newBoard = self.clone()
            newBoard.moveBlank('UP')
            neighbours.append(newBoard)

        # down?
        if int(blank / 3) != 2:
            newBoard = self.clone()
            newBoard.moveBlank('DOWN')
            neighbours.append(newBoard)

        return neighbours

    def isGoal(self):
        """
        check if we have reached the goal state
        """
        for i in range(0, 9):
            if i != 8:
                if self.board[i] != i + 1:
                    return False
        return True

    def manhattan(self):
        """
        distance for the entire board
        """
        manhattan = 0

        for i in range(0, 9):
            if self.board[i] != i + 1 and self.board[i] != 0:
                position = 8 if self.board[i] == 0 else self.board[i] - 1
                sRow = int(i / 3)
                sCol = i % 3
                dRow = int(position / 3)
                dCol = position % 3
                manhattan += abs(sRow - dRow) + abs(sCol - dCol)

        return manhattan

    def getPriority(self, count):
        """
        higher priority mean max no of distance
        """
        return self.move + self.manhattan(), count, self
