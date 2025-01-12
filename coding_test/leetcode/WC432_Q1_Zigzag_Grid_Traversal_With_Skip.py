from tester import Tester

from typing import List

"""
You are given an m x n 2D array grid of positive integers.

Your task is to traverse grid in a zigzag pattern while skipping every alternate cell.

Zigzag pattern traversal is defined as following the below actions:
1. Start at the top-left cell (0, 0).
2. Move right within a row until the end of the row is reached.
3. Drop down to the next row, then traverse left until the beginning of the row is reached.
4. Continue alternating between right and left traversal until every row has been traversed.
5. You must skip every alternate cell during the traversal.

Return an array of integers result containing, in order, the value of the cells visited during the zigzag traversal with skips.

Example 1:
Input: grid = [[1,2],[3,4]]
Output: [1,4]

Example 2:
Input: grid = [[2,1],[2,1],[2,1]]
Output: [2,1,2]

Example 3:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,3,5,7,9]

Constraints:
1. 2 <= n == grid.length <= 50
2. 2 <= m == grid[i].length <= 50
3. 1 <= grid[i][j] <= 2500
"""


class Solution:
    def zigzagTraversalWithSkip(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        result = []
        for i in range(n):
            if i % 2 == 0:
                j_range = range(0, m, 2)
            else:
                k = m % 2
                j_range = range(m-1-k, -1, -2)

            for j in j_range:
                result.append(grid[i][j])

        return result


if __name__ == "__main__":
    tests = [
        [[[1, 2], [3, 4]]],
        [[[2, 1], [2, 1], [2, 1]]],
        [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]],
        [[[1, 2, 1, 3], [5, 15, 7, 3], [10, 4, 14, 12]]],
    ]
    answers = [[1, 4], [2, 1, 2], [1, 3, 5, 7, 9], [1, 1, 3, 15, 10, 14]]

    tester = Tester(Solution().zigzagTraversalWithSkip, exact_match=True)
    tester.test(tests, answers)
