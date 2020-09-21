"""
Class to store the board config and total moves
and previous state of the board to avoid the
cycle
"""


class Board:
    def __init__(self, board, move=0, previous=None, n=3):
        """
        board is a list
        move no of total moves to solve
        previous the state of board before moves
        """
        self.board = board
        self.move = move
        self.previous = previous
        self.n = n

    def __str__(self):
        """
        fancy printing on the terminal for board
        """
        string = ''
        string = string + ('+----' * self.n) + '+' + '\n'
        for i in range(self.n):
            for j in range(self.n):
                tile = self.board[i * self.n + j]
                string = string + '| {} '.format('  ' if tile == 0 else str(tile).zfill(2))
            string = string + '|\n'
            string = string + ('+----' * self.n) + '+' + '\n'
        return string

    def clone(self):
        """
        making a copy to store the previous and
        increment the moves
        """
        return Board(self.board.copy(), self.move + 1, previous=self, n=self.n)

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
            if blank % self.n != 0:
                col = (blank % self.n) - 1
                row = int(blank / self.n)
                self.swap(row * self.n + col, blank)

        if direction == "RIGHT":
            if blank % self.n != self.n - 1:
                col = (blank % self.n) + 1
                row = int(blank / self.n)
                self.swap(row * self.n + col, blank)

        if direction == "UP":
            if int(blank / self.n) != 0:
                col = (blank % self.n)
                row = int(blank / self.n) - 1
                self.swap(row * self.n + col, blank)

        if direction == "DOWN":
            if int(blank / self.n) != self.n - 1:
                col = (blank % self.n)
                row = int(blank / self.n) + 1
                self.swap(row * self.n + col, blank)

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
        if blank % self.n != 0:
            newBoard = self.clone()
            newBoard.moveBlank('LEFT')
            neighbours.append(newBoard)

        # right?
        if blank % self.n != self.n - 1:
            newBoard = self.clone()
            newBoard.moveBlank('RIGHT')
            neighbours.append(newBoard)

        # up?
        if int(blank / self.n) != 0:
            newBoard = self.clone()
            newBoard.moveBlank('UP')
            neighbours.append(newBoard)

        # down?
        if int(blank / self.n) != self.n - 1:
            newBoard = self.clone()
            newBoard.moveBlank('DOWN')
            neighbours.append(newBoard)

        return neighbours

    def isGoal(self):
        """
        check if we have reached the goal state
        """
        for i in range(0, self.n * self.n):
            if i != self.n * self.n - 1:
                if self.board[i] != i + 1:
                    return False
        return True

    def manhattan(self):
        """
        distance for the entire board
        """
        manhattan = 0

        for i in range(0, self.n * self.n):
            if self.board[i] != i + 1 and self.board[i] != 0:
                position = self.n - 1 if self.board[i] == 0 else self.board[i] - 1
                sRow = int(i / self.n)
                sCol = i % self.n
                dRow = int(position / self.n)
                dCol = position % self.n
                manhattan += abs(sRow - dRow) + abs(sCol - dCol)

        return manhattan

    def getPriority(self, count):
        """
        higher priority mean max no of distance
        """
        return self.move + self.manhattan(), count, self
