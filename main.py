from lib.solver import PuzzleSolver
"""
run this
$ python main.py < in.txt

PuzzleSolver.solve takes in one positional argument
goalState (bool) if it is set to True, the start 
function will read the Goal State
else it will create a default Goal State
"""

print("Use 0 to denote the space in the board")
solver = PuzzleSolver(n=3)
solver.start(goalState=True)
solver.solveAStart()
solver.solveBFS()
solver.solveDFS()
