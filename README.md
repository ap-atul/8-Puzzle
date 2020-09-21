# 8 Puzzle Problem Solution using A*

* A*
    A* path finding algorithm is used to solve the 8 puzzle problem.
    
    It uses Manhattan distance and Priority queue to get the min distance satisfying the move.
    
    Update: No more 8 Puzzle, upgraded to n Puzzle (edit n value in main.py)
    
    Evaluation function f(node) to order its search
    ```
    f(n) = Estimation cost of a path from Start to Goal via node n
    f(n) = g(n) + h(n)
    Here,
      g(n) : backward looking (how far are we from start) [in code no of move; look at Board.move]
      h(n) : forward looking (how far we need to go) [in code; Manhattan distance]
      f(n) : complete estimation [in code; getPriority(); look at Board.getPriority()]
    ```

* BFS
    Using Queue
   
* DFS
    Using LifoQueue (stack)

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
If you occurred on a test case that is not solved by the code, then raise an issue
