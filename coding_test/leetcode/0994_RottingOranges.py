from tester import Tester  # Assuming you have a Tester class for running tests
from typing import List

"""
994. Rotting Oranges
Medium

You are given an m x n grid where each cell can have one of three values:
- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

### Example 1:

Minute 0       | Minute 1       | Minute 2       | Minute 3       | Minute 4
---------------|----------------|----------------|----------------|----------------
❌ 🍊 🍊       | ❌ ❌ 🍊       | ❌ ❌ ❌       | ❌ ❌ ❌       | ❌ ❌ ❌
🍊 🍊 ⬜       | ❌ 🍊 ⬜       | ❌ ❌ ⬜       | ❌ ❌ ⬜       | ❌ ❌ ⬜
⬜ 🍊 🍊       | ⬜ 🍊 🍊       | ⬜ 🍊 🍊       | ⬜ ❌ 🍊       | ⬜ ❌ ❌

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

### Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten because rotting only happens 4-directionally.

### Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2.
"""


def get_n_fresh_oranges(grid: List[List[int]]) -> int:
    fresh_oranges = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                fresh_oranges += 1

    return fresh_oranges


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Started @ 04:18

        Brute force method

        O((nm)^2)

        Coding finished @ 04:28
        """
        fresh_oranges = get_n_fresh_oranges(grid)
        prev_fresh_oranges = fresh_oranges
        day = 0
        while fresh_oranges > 0:
            may_rotten = []
            for row in range(len(grid)):
                for col in range(len(grid[row])):
                    if grid[row][col] == 2:
                        if (row - 1) > 0:
                            may_rotten.append((row - 1, col))

                        if (row + 1) < len(grid):
                            may_rotten.append((row + 1, col))

                        if (col - 1) > 0:
                            may_rotten.append((row, col - 1))

                        if (col + 1) < len(grid[row]):
                            may_rotten.append((row, col + 1))

            for rotten_row, rotten_col in may_rotten:
                if grid[rotten_row][rotten_col] == 1:
                    grid[rotten_row][rotten_col] = 2

            fresh_oranges = get_n_fresh_oranges(grid)
            day += 1

            if fresh_oranges == prev_fresh_oranges:
                break

            prev_fresh_oranges = fresh_oranges

        return day if fresh_oranges == 0 else -1

    def orangesRotting2(self, grid: List[List[int]]) -> int:
        """
        Coding finished @ 04:46
        It's also O((mn)^2)

        TODO: Optimize better
        """
        n_fresh_oranges = get_n_fresh_oranges(grid)
        rotten_oranges = []
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    rotten_oranges.append((row, col))

        day = 0
        prev_n_fresh = n_fresh_oranges
        while n_fresh_oranges > 0:
            rotten_candidate = []
            for rotten_row, rotten_col in rotten_oranges:
                if (rotten_row - 1) >= 0:
                    rotten_candidate.append((rotten_row - 1, rotten_col))

                if (rotten_row + 1) < len(grid):
                    rotten_candidate.append((rotten_row + 1, rotten_col))

                if (rotten_col - 1) >= 0:
                    rotten_candidate.append((rotten_row, rotten_col - 1))

                if (rotten_col + 1) < len(grid[0]):
                    rotten_candidate.append((rotten_row, rotten_col + 1))

            for rotten_row, rotten_col in rotten_candidate:
                if grid[rotten_row][rotten_col] == 1:
                    rotten_oranges.append((rotten_row, rotten_col))
                    grid[rotten_row][rotten_col] = 2
                    n_fresh_oranges -= 1

            day += 1
            if n_fresh_oranges == prev_n_fresh:
                break

            prev_n_fresh = n_fresh_oranges

        return day if n_fresh_oranges == 0 else -1


if __name__ == "__main__":
    # Test cases
    tests = [
        [[[2, 1, 1], [1, 1, 0], [0, 1, 1]]],  # Example 1
        [[[2, 1, 1], [0, 1, 1], [1, 0, 1]]],  # Example 2
        [[[0, 2]]],  # Example 3
        [
            [
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]
        ],
    ]
    answers = [
        4,  # Expected output for Example 1
        -1,  # Expected output for Example 2
        0,  # Expected output for Example 3
        19,
    ]

    tester = Tester(Solution().orangesRotting2)
    tester.test(tests, answers)
