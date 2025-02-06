from tester import Tester
from typing import List

"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
"""


class Solution:
    def coinChange2(self, coins: List[int], amount: int) -> int:
        """
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
        0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6
        0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] <= amount else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        def backtrace(current: List[int], remain: int, min_cnt: int) -> int:
            if remain < 0:
                return min(amount + 1, min_cnt)

            if len(current) >= min_cnt:
                return min_cnt

            if remain == 0:
                return min(len(current), min_cnt)

            for coin in coins:
                repeat = 1
                if remain % coin == 0:
                    repeat = remain // coin

                if len(current) + repeat >= min_cnt:
                    continue

                min_cnt = backtrace(
                    current + [coin] * repeat, remain - coin * repeat, min_cnt
                )

            return min_cnt

        result = backtrace([], amount, amount + 1)
        return result if result <= amount else -1


if __name__ == "__main__":
    tests = [
        [[1, 2, 5], 11],
        [[2], 3],
        [[1], 0],
        [[1], 2],
        [[1, 2, 5], 100],
        [[186, 419, 83, 408], 6249],
    ]
    answers = [
        3,
        -1,
        0,
        2,
        20,
        20,
    ]

    tester = Tester(Solution().coinChange2)
    tester.test(tests, answers)
