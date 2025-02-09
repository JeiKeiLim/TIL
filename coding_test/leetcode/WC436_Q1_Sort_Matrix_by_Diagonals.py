from tester import Tester

from typing import List

"""
You are given an n x n square matrix of integers grid. Return the matrix such that:

1. The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
2. The diagonals in the top-right triangle are sorted in non-decreasing order.

Example 1:
Input: grid = [
    [1,7,3],
    [9,8,2],
    [4,5,6]
    ]
Output: [
    [8,2,3],
    [9,6,7],
    [4,5,1]
    ]

[1,2,3,4]
[1,2,3,4]
[1,2,3,4]
[1,2,3,4]

(0, 1), (1, 2), (2, 3)
(0, 2), (1, 3)
(0, 3)


(0, 0), (1, 1), (2, 2)
(1, 0), (2, 1)
(2, 0)

(0, 1), (1, 2)
(0, 2)

Explanation:
- The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:
  [1, 8, 6] becomes [8, 6, 1].
  [9, 5] and [4] remain unchanged.
- The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:
  [7, 2] becomes [2, 7].
  [3] remains unchanged.

Example 2:
Input: grid = [[0,1],[1,2]]
Output: [[2,1],[1,0]]

Explanation:
- The diagonals with a black arrow must be non-increasing, so [0, 2] is changed to [2, 0].
- The other diagonals are already in the correct order.

Example 3:
Input: grid = [[1]]
Output: [[1]]

Explanation:
- Diagonals with exactly one element are already in order, so no changes are needed.

Constraints:
1. grid.length == grid[i].length == n
2. 1 <= n <= 10
3. -10^5 <= grid[i][j] <= 10^5
"""


class Solution:
    def diagonalSort(self, grid: List[List[int]]) -> List[List[int]]:
        n = m = len(grid)
        for i in range(n):
            black_arr = []
            for j in range(i, n):
                black_arr.append(grid[i + (j - i)][j - i])
            black_arr.sort(reverse=True)
            k = 0
            for j in range(i, n):
                grid[i + (j - i)][j - i] = black_arr[k]
                k += 1

        for i in range(n - 1):
            white_arr = []
            for j in range(i + 1, n):
                white_arr.append(grid[j - i - 1][j])
            white_arr.sort()
            k = 0
            for j in range(i + 1, n):
                grid[j - i - 1][j] = white_arr[k]
                k += 1

        return grid


if __name__ == "__main__":
    tests = [
        [[[1, 7, 3], [9, 8, 2], [4, 5, 6]]],
        [[[0, 1], [1, 2]]],
        [[[1]]],
        [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]],
    ]
    answers = [
        [[8, 2, 3], [9, 6, 7], [4, 5, 1]],
        [[2, 1], [1, 0]],
        [[1]],
        [[16, 2, 3, 4], [15, 11, 7, 8], [14, 10, 6, 12], [13, 9, 5, 1]],
    ]

    tester = Tester(Solution().diagonalSort)
    tester.test(tests, answers)
