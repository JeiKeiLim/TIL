from collections import defaultdict
from tester import Tester, generate_random_int_array

from typing import List

"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation:
   2
  3 4
 6 5 7
4 1 8 3
Minimum path: 2 + 3 + 5 + 1 = 11

Example 2:
Input: triangle = [[-10]]
Output: -10

Constraints:
• 1 <= triangle.length <= 200
• triangle[0].length == 1
• triangle[i].length == triangle[i - 1].length + 1
• -10^4 <= triangle[i][j] <= 10^4

Follow up: Can you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""

import heapq


class Solution:
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1].copy()

        for row in range(n - 2, -1, -1):
            for col in range(len(triangle[row])):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
        return dp[0]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        answer = 10**4
        queue = [(0, 0, 0)]
        min_levels = defaultdict(lambda: 10**4)

        while queue:
            level, i, val = heapq.heappop(queue)
            if level == n:
                answer = min(answer, val)
                continue
            key = (level, i)
            if val >= min_levels[key]:
                continue
            min_levels[key] = min(val, min_levels[key])

            heapq.heappush(queue, (level + 1, i, val + triangle[level][i]))
            if (i + 1) < len(triangle[level]):
                heapq.heappush(queue, (level + 1, i + 1, val + triangle[level][i + 1]))

        return answer


if __name__ == "__main__":
    tests = [
        [[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]],
        [[[-10]]],
        [[[-1], [3, 2], [-3, 1, -1]]],
        [[[-1], [2, 3], [1, -1, -3]]],
        [
            [
                generate_random_int_array(i, start_n=-(10**4), end_n=10**4)
                for i in range(1, 201)
            ]
        ],
        [[[0] * i for i in range(1, 201)]],
    ]
    tests[-1][-1][-2][123] = -123
    answers = [11, -10, -1, -1, -1, -123]

    tester = Tester(Solution().minimumTotal2)
    tester.test(tests, answers)
