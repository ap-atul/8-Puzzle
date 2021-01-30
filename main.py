from lib.solver import PuzzleSolver
"""
PuzzleSolver.solve takes in one positional argument
goalState (bool) if it is set to True, the start 
function will read the Goal State
else it will create a default Goal State

Examples
--------

$ python main.py < in.txt
Start State .............
+----+----+----+
| 08 | 07 | 06 |
+----+----+----+
|    | 05 | 04 |
+----+----+----+
| 03 | 02 | 01 |
+----+----+----+

Goal State ..............
+----+----+----+
|    | 08 | 07 |
+----+----+----+
| 06 | 05 | 04 |
+----+----+----+
| 03 | 02 | 01 |
+----+----+----+

**************************************
Algorithm name :: A star
Total optimal moves to solve :: 13
Total steps required to get to Goal :: 1022
Time required to find the Goal state :: 0.039 s
+----+----+----+
|    | 08 | 07 |
+----+----+----+
| 06 | 05 | 04 |
+----+----+----+
| 03 | 02 | 01 |
+----+----+----+

**************************************
**************************************
Algorithm name :: BFS
Total optimal moves to solve :: 13
Total steps required to get to Goal :: 4366
Time required to find the Goal state :: 10.451 s
+----+----+----+
|    | 08 | 07 |
+----+----+----+
| 06 | 05 | 04 |
+----+----+----+
| 03 | 02 | 01 |
+----+----+----+

**************************************
**************************************
Algorithm name :: DFS
Total optimal moves to solve :: 4831
Total steps required to get to Goal :: 8809
Time required to find the Goal state :: 50.325 s
+----+----+----+
|    | 08 | 07 |
+----+----+----+
| 06 | 05 | 04 |
+----+----+----+
| 03 | 02 | 01 |
+----+----+----+

**************************************

"""

print("Use 0 to denote the space in the board")
solver = PuzzleSolver(n=3)
solver.start(goalState=False)
solver.solveAStart()
solver.solveBFS()
solver.solveDFS()
