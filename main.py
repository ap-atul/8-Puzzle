from lib.solver import PuzzleSolver
"""
run this
$ python main.py < in.txt
"""

print("Use 0 to denote the space in the board")
solver = PuzzleSolver(n=5)
solver.start().solve()
