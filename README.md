# 8 Puzzle Problem Solution using A*
A* path finding algorithm is used to solve the 8 puzzle problem.

It uses Manhattan distance and Priority queue to get the min distance satisfying move.

## Execution steps
1. Clone the repo
```
$ git clone https://github.com/AP-Atul/8-Puzzle.git
```
2. Run the main python file
```
$ python main.py < in.txt

Solving for
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 5 | 6 | 4 |
+---+---+---+
|   | 7 | 8 |
+---+---+---+


+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 |   |
+---+---+---+

Required a total of 16 steps.

```
3. You can create your one test cases to check

## Error
If you occurred on a test case that does not solved by the code and is possible to solve, then raise an issue