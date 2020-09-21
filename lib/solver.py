from lib.board import Board
from queue import PriorityQueue

"""
Solver class that takes in Board and perform 
A* to solve it
Priority queue uses Min Heap which will return 
the value of the Min Priority which points to 
min distance required to solve the puzzle.
So moves are picked directly by Queue.
"""


class PuzzleSolver:
    def __init__(self, n=3):
        """
        initializing the queue and board
        """
        self.boardList = []
        self.queue = PriorityQueue()
        self.n = n

    def solve(self):
        """
        main solve function, read the neighbours
        append the dist and moves to the queue
        Queue picks small distances and puzzle is
        solved
        """
        board = Board(self.boardList, n=self.n)
        print("Solving for")
        print(board)
        print()

        self.queue.put(board.getPriority(0))
        i = 1

        while not self.queue.empty():
            board = self.queue.get()[2]
            if not board.isGoal():
                for neighbour in board.getNeighbours():
                    if neighbour != board.previous:
                        self.queue.put(neighbour.getPriority(i))
                        i += 1
            else:
                print(board)
                print(f"Required a total of {board.move} steps.")
                return

    def start(self):
        """
        reading input of no 0- n * n
        0 representing the space tile.
        """
        for i in range(0, self.n * self.n):
            self.boardList.append(int(input()))
        return self
