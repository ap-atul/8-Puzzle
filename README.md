# 8 Puzzle Problem Solution using A*
A* path finding algorithm is used to solve the 8 puzzle problem.

It uses Manhattan distance and Priority queue to get the min distance satisfying move.

Update: No more 8 Puzzle, upgraded to n Puzzle (edit n value in main.py)

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

## Example
Using n=5, so 24 Puzzle Problem
```
Solving for .............
+----+----+----+----+----+
| 01 | 02 | 03 | 04 | 05 |
+----+----+----+----+----+
| 06 | 07 | 08 | 09 | 10 |
+----+----+----+----+----+
| 11 | 12 | 13 | 14 | 15 |
+----+----+----+----+----+
| 16 | 17 | 18 |    | 20 |
+----+----+----+----+----+
| 21 | 22 | 23 | 19 | 24 |
+----+----+----+----+----+

**************************************
Algorithm name :: A star
Total optimal moves to solve :: 2
Total steps required to get to Goal :: 7
Time required to find the Goal state :: 0.0 s
+----+----+----+----+----+
| 01 | 02 | 03 | 04 | 05 |
+----+----+----+----+----+
| 06 | 07 | 08 | 09 | 10 |
+----+----+----+----+----+
| 11 | 12 | 13 | 14 | 15 |
+----+----+----+----+----+
| 16 | 17 | 18 | 19 | 20 |
+----+----+----+----+----+
| 21 | 22 | 23 | 24 |    |
+----+----+----+----+----+

**************************************
**************************************
Algorithm name :: BFS
Total optimal moves to solve :: 2
Total steps required to get to Goal :: 37
Time required to find the Goal state :: 0.002 s
+----+----+----+----+----+
| 01 | 02 | 03 | 04 | 05 |
+----+----+----+----+----+
| 06 | 07 | 08 | 09 | 10 |
+----+----+----+----+----+
| 11 | 12 | 13 | 14 | 15 |
+----+----+----+----+----+
| 16 | 17 | 18 | 19 | 20 |
+----+----+----+----+----+
| 21 | 22 | 23 | 24 |    |
+----+----+----+----+----+

**************************************
**************************************
Algorithm name :: DFS
Total optimal moves to solve :: 2
Total steps required to get to Goal :: 8
Time required to find the Goal state :: 0.0 s
+----+----+----+----+----+
| 01 | 02 | 03 | 04 | 05 |
+----+----+----+----+----+
| 06 | 07 | 08 | 09 | 10 |
+----+----+----+----+----+
| 11 | 12 | 13 | 14 | 15 |
+----+----+----+----+----+
| 16 | 17 | 18 | 19 | 20 |
+----+----+----+----+----+
| 21 | 22 | 23 | 24 |    |
+----+----+----+----+----+

**************************************

```

## Error
If you occurred on a test case that does not solved by the code and is possible to solve, then raise an issue