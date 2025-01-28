from tester import Tester

from typing import List

"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally
(horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,1,1,0,1,0,0,0,0,0,0,0,0],
               [0,1,0,0,1,1,0,0,1,0,1,0,0],
               [0,1,0,0,1,1,0,0,1,1,1,0,0],
               [0,0,0,0,0,0,0,0,0,0,1,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:
1. m == grid.length
2. n == grid[i].length
3. 1 <= m, n <= 50
4. grid[i][j] is either 0 or 1.
"""


class Solution:
    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r >= n or c >= m or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            result = 1
            for dr, dc in directions:
                result += dfs(r+dr, c+dc)
            return result

        answer = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                answer = max(answer, dfs(i, j))

        return answer

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r >= n or c >= m or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))

            result = 0
            for dr, dc in directions:
                result += dfs(r+dr, c+dc)
            return result + grid[r][c]

        answer = 0
        for i in range(n):
            for j in range(m):
                if (i, j) in visited:
                    continue
                answer = max(answer, dfs(i, j))

        return answer


if __name__ == "__main__":
    tests = [
        [
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ]
        ],
        [[[0, 0, 0, 0, 0, 0, 0, 0]]],
    ]
    answers = [6, 0]

    tester = Tester(Solution().maxAreaOfIsland2)
    tester.test(tests, answers)
