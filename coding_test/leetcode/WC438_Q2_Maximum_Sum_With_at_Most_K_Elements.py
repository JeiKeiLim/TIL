from tester import Tester, generate_random_int_array

from typing import List

"""
You are given a 2D integer matrix grid of size n x m, an integer array limits of length n, and an integer k.
The task is to find the maximum sum of at most k elements from the matrix grid such that:

1. The number of elements taken from the ith row of grid does not exceed limits[i].

Return the maximum sum.

Example 1:
Input: grid = [[1,2],[3,4]], limits = [1,2], k = 2
Output: 7
Explanation:
- From the second row, we can take at most 2 elements. The elements taken are 4 and 3.
- The maximum possible sum of at most 2 selected elements is 4 + 3 = 7.

Example 2:
Input: grid = [[5,3,7],[8,2,6]], limits = [2,2], k = 3
Output: 21
Explanation:
- From the first row, we can take at most 2 elements. The element taken is 7.
- From the second row, we can take at most 2 elements. The elements taken are 8 and 6.
- The maximum possible sum of at most 3 selected elements is 7 + 8 + 6 = 21.

Constraints:
1. n == grid.length == limits.length
2. m == grid[i].length
3. 1 <= n, m <= 500
4. 0 <= grid[i][j] <= 10^5
5. 0 <= limits[i] <= m
6. 0 <= k <= min(n * m, sum(limits))

10, 7
10, 2
"""


class Solution:
    def maxSumWithAtMostKElements(
        self, grid: List[List[int]], limits: List[int], k: int
    ) -> int:
        if k == 0:
            return 0

        candidates = []
        for i, row in enumerate(grid):
            if limits[i] == 0:
                continue
            candidates.extend(sorted(row)[-limits[i] :])
        return sum(sorted(candidates)[-k:])


if __name__ == "__main__":
    tests = [
        [[[1, 2], [3, 4]], [1, 2], 2],
        [[[5, 3, 7], [8, 2, 6]], [2, 2], 3],
        [[[0, 1]], [0], 0],
        [[[10, 0, 7], [3, 10, 2]], [2, 2], 2],
        [
            [generate_random_int_array(500, end_n=10**5) for _ in range(500)],
            generate_random_int_array(500, end_n=500),
            500 * 500,
        ],
    ]
    answers = [7, 21, 0, 20, -1]

    tester = Tester(Solution().maxSumWithAtMostKElements)
    tester.test(tests, answers)
