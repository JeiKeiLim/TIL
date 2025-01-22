from tester import Tester, generate_random_int_array

from typing import List
from collections import deque

"""
You are given an integer matrix isWater of size m x n that represents a map of land and water cells.
- If isWater[i][j] == 0, cell (i, j) is a land cell.
- If isWater[i][j] == 1, cell (i, j) is a water cell.

You must assign each cell a height in a way that follows these rules:
1. The height of each cell must be non-negative.
2. If the cell is a water cell, its height must be 0.
3. Any two adjacent cells must have an absolute height difference of at most 1.

A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).

Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.

Example 1:
Input: isWater = [[0,1],[0,0]]
Output: [[1,0],[2,1]]


Explanation:
The blue cell is the water cell, and the green cells are the land cells.

Example 2:
Input: isWater = [
    [0,0,1],
    [1,0,0],
    [0,0,0]
    ]
Output: [
    [1,1,0],
    [0,1,1],
    [1,2,2]
    ]

                [2, L, 2, 3, 2, L, 0, L],
                [L, 0, L, 2, 3, 2, L, 2],
                [2, L, 2, 3, 4, 3, 2, 1],
                [1, 2, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, L, 2],
                [1, 1, L, 1, 1, L, 0, L],
                [1, L, 0, L, 1, 1, L, 1],

Explanation:
A height of 2 is the maximum possible height of any assignment.

Constraints:
1. m == isWater.length
2. n == isWater[i].length
3. 1 <= m, n <= 1000
4. isWater[i][j] is 0 or 1.
5. There is at least one water cell.
"""


class Solution:
    def highestPeak2(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))

        queue = deque()

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    queue.append((i, j, 0))
                    isWater[i][j] = 0

        visited = set()
        while queue:
            row, col, height = queue.popleft()

            if (row, col) in visited:
                continue

            visited.add((row, col))
            isWater[row][col] = height

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if r < 0 or c < 0 or r >= n or c >= m:
                    continue
                queue.append((r, c, height + 1))

        return isWater

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        """O(n^3)"""
        n = len(isWater)
        m = len(isWater[0])
        board = [[1 - isWater[i][j] for j in range(m)] for i in range(n)]

        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))
        for k in range(n):
            for i in range(k, -1, -1):
                for j in range(m):
                    min_height = board[i][j]
                    if min_height == 0:
                        continue
                    for dr, dc in directions:
                        row = i + dr
                        col = j + dc
                        if row < 0 or col < 0 or row >= n or col >= m:
                            continue
                        min_height = min(min_height, board[row][col])
                    board[i][j] = min_height + 1

        return board


if __name__ == "__main__":
    tests = [
        [[[0, 1], [0, 0]]],
        [[[0, 0, 1], [1, 0, 0], [0, 0, 0]]],
        [
            [
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
            ]
        ],
        [[generate_random_int_array(1000, end_n=1) for _ in range(1000)]],
    ]
    answers = [
        [[1, 0], [2, 1]],
        [[1, 1, 0], [0, 1, 1], [1, 2, 2]],
        [
            [2, 1, 2, 3, 2, 1, 0, 1],
            [1, 0, 1, 2, 3, 2, 1, 2],
            [2, 1, 2, 3, 4, 3, 2, 3],
            [3, 2, 3, 4, 5, 4, 3, 4],
            [4, 3, 3, 4, 4, 3, 2, 3],
            [4, 3, 2, 3, 3, 2, 1, 2],
            [3, 2, 1, 2, 2, 1, 0, 1],
            [2, 1, 0, 1, 2, 2, 1, 2],
        ],
        tests[-1][-1],
    ]

    tester = Tester(Solution().highestPeak2, exact_match=True, verbose=0)
    tester.test(tests, answers)
