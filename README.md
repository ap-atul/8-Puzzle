# 8 Puzzle Problem Solution using A*
A* path finding algorithm is used to solve the 8 puzzle problem.

It uses Manhattan distance and Priority queue to get the min distance satisfying the move.

Evaluation function f(node) to order its search
```
f(n) = Estimation cost of a path from Start to Goal via node n
f(n) = g(n) + h(n)
Here,
  g(n) : backward looking (how far are we from start) [in code no of move; look at Board.move]
  h(n) : forward looking (how far we need to go) [in code; Manhattan distance]
  f(n) : complete estimation [in code; getPriority(); look at Board.getPriority()]
```
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
3. You can create your own test cases to check

## Error
If you occurred on a test case that is not solved by the code, then raise an issue
