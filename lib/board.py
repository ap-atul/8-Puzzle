"""
Class to store the board config and total moves
and previous state of the board to avoid the
cycle
"""


class Board:
    def __init__(self, board, goalState=None, move=0, previous=None, n=3):
        """
        Board is structure that stores the current board config

        Determines the structure after some move is performed (left, right, up, down). Keeps track of the board
        structure currently

        Note: 0 is used to represent space

        Parameters
        ----------
        board : iterable
            list of numbers ranging from 0 - (n - 1). Starting state for the puzzle
        goalState : iterable, optional
            Goal state for the puzzle, if not provided a default list is created with 0 at end
        move : int
            initially moves are 0, later increases as new sequences are generated
        previous : object
            previous state of board, useful to avoid cycles
        n : int
            dimension of the board is n is 3, then board is 3x3 with 0-8 nos
        """
        self.board = board
        self.move = move
        self.previous = previous
        self.n = n
        self.goalState = list()

        # if goal state is not specified it will populate in increasing manner
        # Example with n = 3
        # 1  2  3
        # 4  5  6
        # 7  8  0
        if goalState is None:
            for i in range(1, self.n * self.n):
                self.goalState.append(i)
            self.goalState.append(0)
        else:
            self.goalState = goalState

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

    def __eq__(self, other):
        """
        checking equality of two boards

        Parameters
        ----------
        other : Board
            board to compare with

        Returns
        -------
        equal : bool
            True meaning both board are equal or not
        """
        if other is None:
            return False

        for i in range(self.n * self.n):
            if self.board[i] != other.board[i]:
                return False
        return True

    def clone(self):
        """
        making a copy to store the previous and
        increment the moves
        """
        return Board(self.board.copy(), goalState=self.goalState, move=self.move + 1, previous=self, n=self.n)

    def getBlank(self):
        """
        index of the blank space i.e. 0 no
        """
        return self.board.index(0)

    def swap(self, source, destination):
        """
        Swaps the two values of the board

        Parameters
        ----------
        source : int
            index of source number
        destination : int
            index of destination number

        Returns
        -------
        source : int
            new source number
        destination : int
            ne destination number
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
                if self.board[i] != self.goalState[i]:
                    return False
        return True

    def manhattan(self):
        """
        distance for the entire board
        """
        manhattan = 0

        for i in range(0, self.n * self.n):
            if self.board[i] != self.goalState[i] and self.board[i] != 0:
                position = self.n - 1 if self.board[i] == 0 else self.board[i] - 1
                sRow = int(i / self.n)
                sCol = i % self.n
                dRow = int(position / self.n)
                dCol = position % self.n
                manhattan += abs(sRow - dRow) + abs(sCol - dCol)

        return manhattan

    def getPriority(self, count):
        """
        Returns tuple with heuristic value + distance. Used to create the priority queue entry

        Parameters
        ----------
        count : index of board

        Returns
        -------
        tuple
            priority , index, board object

        """
        return self.move + self.manhattan(), count, self
