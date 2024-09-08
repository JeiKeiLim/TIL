from tester import Tester  # Assuming you have a Tester class for running tests

"""
1926. Nearest Exit from Entrance in Maze
Medium

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

### Example 1:
Input: maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], entrance = [1, 2]
Output: 1

### Maze visualization:
+  +  .  +
.  .  T  +
+  +  +  .

Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.


### Example 2:
Input: maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], entrance = [1, 0]
Output: 2

### Maze visualization:
+  +  +
T  .  .
+  +  +

Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
- You can reach [1,2] by moving 2 steps to the right.
Thus, the nearest exit is [1,2], which is 2 steps away.


### Example 3:
Input: maze = [[".", "+"]], entrance = [0, 0]
Output: -1

### Maze visualization:
T  +

Explanation: There are no exits in this maze. The only empty cell is the entrance itself, which does not count as an exit.
Thus, the result is -1.

Constraints:
- maze.length == m
- maze[i].length == n
- 1 <= m, n <= 100
- maze[i][j] is either '.' or '+'.
- entrance.length == 2
- 0 <= entrancerow < m
- 0 <= entrancecol < n
- entrance will always be an empty cell.
"""


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        (
            [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]],
            [1, 2],
        ),  # Example 1
        ([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]),  # Example 2
        ([[".", "+"]], [0, 0]),  # Example 3
    ]
    answers = [
        1,  # Expected output for Example 1
        2,  # Expected output for Example 2
        -1,  # Expected output for Example 3
    ]

    tester = Tester(Solution().nearestExit)
    tester.test(tests, answers)
