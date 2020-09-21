import time

from lib.board import Board
from queue import PriorityQueue, Queue, LifoQueue

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
        self.n = n

    def solveAStart(self):
        """
        main solve function, read the neighbours
        append the dist and moves to the queue
        Queue picks small distances and puzzle is
        solved
        """
        startTime = time.time()
        board = Board(self.boardList, n=self.n)

        print("Solving for .............")
        print(board)

        queue = PriorityQueue()
        queue.put(board.getPriority(0))
        i = 1

        while not queue.empty():
            board = queue.get()[2]
            if not board.isGoal():
                for neighbour in board.getNeighbours():
                    if neighbour != board.previous:
                        queue.put(neighbour.getPriority(i))
                        i += 1
            else:
                self.analytics("A star", board.move, i, time.time() - startTime, board)
                return

    def solveBFS(self):
        startTime = time.time()
        board = Board(self.boardList, n=self.n)

        visited = list()
        queue = Queue()
        queue.put(board.getPriority(0)[2])
        i = 1

        while not queue.empty():
            board = queue.get()
            if not board.isGoal():
                for neighbour in board.getNeighbours():
                    if neighbour not in visited:
                        visited.append(neighbour)
                        queue.put(neighbour)
                        i += 1
            else:
                self.analytics("BFS", board.move, i, time.time() - startTime, board)
                return

    def solveDFS(self):
        startTime = time.time()
        board = Board(self.boardList, n=self.n)

        visited = list()
        queue = LifoQueue()
        queue.put(board.getPriority(0)[2])
        i = 1

        while not queue.empty():
            board = queue.get()
            if not board.isGoal():
                for neighbour in board.getNeighbours():
                    if neighbour not in visited:
                        visited.append(neighbour)
                        queue.put(neighbour)
                        i += 1
            else:
                self.analytics("DFS", board.move, i, time.time() - startTime, board)
                return

    def start(self):
        """
            reading input of no 0- n * n
            0 representing the space tile.
            """
        for i in range(0, self.n * self.n):
            self.boardList.append(int(input()))
        return self

    def analytics(self, method, moves, steps, executionTime, board):
        print("**************************************")
        print(f"Algorithm name :: {method}")
        print(f"Total optimal moves to solve :: {moves}")
        print(f"Total steps required to get to Goal :: {steps}")
        print(f"Time required to find the Goal state :: {round(executionTime, 3)} s")
        print(board)
        print("**************************************")
