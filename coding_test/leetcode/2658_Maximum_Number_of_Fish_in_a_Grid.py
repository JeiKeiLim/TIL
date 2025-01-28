from tester import Tester

from typing import List

"""
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
1. A land cell if grid[r][c] = 0, or
2. A water cell containing grid[r][c] fish, if grid[r][c] > 0.

A fisher can start at any water cell (r, c) and can do the following operations any number of times:
1. Catch all the fish at cell (r, c), or
2. Move to any adjacent water cell.

Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c) is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

Example 1:
Input: grid = [
    [0,2,1,0],
    [4,0,0,3],
    [1,0,0,4],
    [0,3,2,0]
    ]
Output: 7
Explanation:
- The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.

Example 2:
Input: grid = [
    [1,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,1]
    ]
Output: 1
Explanation:
- The fisher can start at cells (0,0) or (3,3) and collect a single fish.

[4,  5, 5]
[0, 10, 0]

(0, 0): 4
(0, 1): 5
(0, 2): 5
(1, 1): 10

Constraints:
1. m == grid.length
2. n == grid[i].length
3. 1 <= m, n <= 10
4. 0 <= grid[i][j] <= 10
"""


class Solution:
    def findMaxFish2(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        visited = set()

        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r >= n or c >= m or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))
            result = 0
            for dr, dc in directions:
                result += dfs(r + dr, c + dc)

            return result + grid[r][c]

        answer = 0
        for i in range(n):
            for j in range(m):
                if (i, j) in visited:
                    continue
                answer = max(answer, dfs(i, j))

        return answer

    def findMaxFish(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    queue.append((i, j, set([(i, j)])))

        max_fish = 0
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while queue:
            row, col, visited = queue.pop()

            fish = sum(grid[r][c] for r, c in visited)

            max_fish = max(fish, max_fish)

            next_rc = []
            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if r < 0 or c < 0 or r >= n or c >= m:
                    continue

                if (r, c) in visited or grid[r][c] == 0:
                    continue

                visited.add((r, c))
                next_rc.append((r, c))
                queue.append((r, c, visited))

        return max_fish


if __name__ == "__main__":
    tests = [
        [[[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]],
        [[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]],
        [[[4, 5, 5], [0, 10, 0]]],
        [[[8, 6], [2, 6]]],
        [
            [
                [0, 4, 7, 0, 1] * 10,
                [10, 7, 9, 8, 0] * 10,
                [0, 10, 8, 0, 0] * 10,
                [8, 3, 10, 0, 0] * 10,
                [0, 0, 0, 0, 0] * 10,
            ]
            * 10
        ],
    ]
    answers = [7, 1, 24, 22, 84, 84]

    tester = Tester(Solution().findMaxFish, verbose=0)
    tester.test(tests, answers)
