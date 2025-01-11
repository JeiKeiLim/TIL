from tester import Tester

from typing import List

import random

"""
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:
1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board.
In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

[0, 1, 0]
[0, 0, 1]
[1, 1, 1]
[0, 0, 0]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

Constraints:
1. m == board.length
2. n == board[i].length
3. 1 <= m, n <= 25
4. board[i][j] is 0 or 1.

Follow up:
1. Could you solve it in-place?
2. How would you address the problem if the board was infinite?
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
        ]
        next_gen = {}
        for row in range(len(board)):
            for col in range(len(board[row])):
                n_live_cell = 0
                for dr, dc in directions:
                    rr, cc = row + dr, col + dc
                    if len(board) <= rr or rr < 0 or len(board[rr]) <= cc or cc < 0:
                        continue
                    n_live_cell += board[rr][cc]

                if board[row][col] == 1 and (n_live_cell < 2 or n_live_cell > 3):
                    next_gen[(row, col)] = 0
                elif n_live_cell == 3:
                    next_gen[(row, col)] = 1

        for (row, col), value in next_gen.items():
            board[row][col] = value

        return board


if __name__ == "__main__":
    tests = [
        [[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]],
        [[[1, 1], [1, 0]]],
    ]
    answers = [
        [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
        [[1, 1], [1, 1]],
    ]

    tester = Tester(Solution().gameOfLife)
    tester.test(tests, answers)
