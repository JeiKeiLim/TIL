from tester import Tester, generate_random_int_array

from typing import List
from collections import deque

import random

"""
You are given an m x n grid. A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). 
The robot can move either right or down at any point in time.

The grid contains a value coins[i][j] in each cell:
1. If coins[i][j] >= 0, the robot gains that many coins.
2. If coins[i][j] < 0, the robot encounters a robber, and the robber steals the absolute value of coins[i][j] coins.
3. The robot has a special ability to neutralize robbers in at most 2 cells on its path, preventing them from stealing coins in those cells.

Note: The robot's total coins can be negative.

Return the maximum profit the robot can gain on the route.

Example 1:
Input: coins = [[0,1,-1],[1,-2,3],[2,-3,4]]

[0,1,-1],
[1,-2,3],
[2,-3,4]

Output: 8
Explanation:
An optimal path for maximum coins is:
- Start at (0, 0) with 0 coins (total coins = 0).
- Move to (0, 1), gaining 1 coin (total coins = 0 + 1 = 1).
- Move to (1, 1), where there's a robber stealing 2 coins. The robot uses one neutralization here, avoiding the robbery (total coins = 1).
- Move to (1, 2), gaining 3 coins (total coins = 1 + 3 = 4).
- Move to (2, 2), gaining 4 coins (total coins = 4 + 4 = 8).

Example 2:
Input: coins = [[10,10,10],[10,10,10]]
Output: 40
Explanation:
An optimal path for maximum coins is:
- Start at (0, 0) with 10 coins (total coins = 10).
- Move to (0, 1), gaining 10 coins (total coins = 10 + 10 = 20).
- Move to (0, 2), gaining another 10 coins (total coins = 20 + 10 = 30).
- Move to (1, 2), gaining the final 10 coins (total coins = 30 + 10 = 40).

Constraints:
1. m == coins.length
2. n == coins[i].length
3. 1 <= m, n <= 500
4. -1000 <= coins[i][j] <= 1000
"""


class Solution:
    def maxProfit2(self, coins: List[List[int]]) -> int:
        n = len(coins)
        m = len(coins[0])

        stack = deque([(0, 0, 2, coins[0][0])])
        if coins[0][0] < 0:
            stack.append((0, 0, 1, 0))

        max_score = -(2**31)

        max_stack = 0
        memo = {}
        while stack:
            max_stack = max(max_stack, len(stack))
            i, j, coin, score = stack.pop()

            if (i, j, coin) in memo and score < memo[(i, j, coin)]:
                continue

            memo[(i, j, coin)] = score

            if i == n - 1 and j == m - 1:
                max_score = max(max_score, score)
                continue

            for ii, jj in ((i + 1, j), (i, j + 1)):
                if ii == n or jj == m:
                    continue

                next_score = score + coins[ii][jj]
                stack.append((ii, jj, coin, next_score))

                if coins[ii][jj] < 0 and coin > 0:
                    stack.append((ii, jj, coin - 1, score))

        return max_score

    def maxProfit(self, coins: List[List[int]]) -> int:
        n = len(coins)
        m = len(coins[0])

        dp = [[[0] * m for _ in range(n)] for _ in range(3)]

        dp[2][0][0] = coins[0][0]
        dp[1][0][0] = max(dp[2][0][0], 0)
        dp[0][0][0] = max(dp[1][0][0], 0)

        for i in range(1, n):
            dp[2][i][0] = dp[2][i - 1][0] + coins[i][0]
            dp[1][i][0] = max(
                dp[2][i][0], dp[2][i - 1][0], dp[1][i - 1][0] + coins[i][0]
            )
            dp[0][i][0] = max(
                dp[1][i][0], dp[1][i - 1][0], dp[0][i - 1][0] + coins[i][0]
            )

        for i in range(1, m):
            dp[2][0][i] = dp[2][0][i - 1] + coins[0][i]
            dp[1][0][i] = max(
                dp[2][0][i], dp[2][0][i - 1], dp[1][0][i - 1] + coins[0][i]
            )
            dp[0][0][i] = max(
                dp[1][0][i], dp[1][0][i - 1], dp[0][0][i - 1] + coins[0][i]
            )

        for i in range(1, n):
            for j in range(1, m):
                dp[2][i][j] = max(dp[2][i - 1][j], dp[2][i][j - 1]) + coins[i][j]
                dp[1][i][j] = max(
                    dp[2][i][j],
                    dp[2][i - 1][j],
                    dp[2][i][j - 1],
                    dp[1][i - 1][j] + coins[i][j],
                    dp[1][i][j - 1] + coins[i][j],
                )
                dp[0][i][j] = max(
                    dp[1][i][j],
                    dp[1][i - 1][j],
                    dp[1][i][j - 1],
                    dp[0][i - 1][j] + coins[i][j],
                    dp[0][i][j - 1] + coins[i][j],
                )

        return max(dp[0][-1][-1], dp[1][-1][-1], dp[2][-1][-1])


if __name__ == "__main__":
    tests = [
        [[[0, 1, -1], [1, -2, 3], [2, -3, 4]]],
        [[[10, 10, 10], [10, 10, 10]]],
        [[[-16, 8, -7, -19], [6, 3, -10, 13], [13, 15, 4, -3], [-16, 4, 19, -12]]],
        [[[-7, 12, 12, 13], [-6, 19, 19, -6], [9, -2, -10, 16], [-4, 14, -10, -9]]],
        [[generate_random_int_array(500, start_n=-1000, end_n=1000) for _ in range(500)]],
    ]
    """
    [-16,  8, -7,  -19]
    [  6,  3, -10,  13]
    [ 13, 15,   4,  -3]
    [-16,  4,  19, -12]

    [-16, -8, -15, -34]
    [-10, -5, -15,  -2]
    [  3, 18,  22,  19]
    [-13, 22,  41,  29]]
    """
    answers = [8, 40, 57, 60, -1]

    tester = Tester(Solution().maxProfit, verbose=0)
    tester.test(tests, answers)
