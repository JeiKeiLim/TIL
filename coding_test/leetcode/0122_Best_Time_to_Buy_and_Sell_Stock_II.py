from tester import Tester

from typing import List
import random

"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation:
Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation:
Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

Constraints:
1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4
"""


class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]

        return result

    def maxProfit(self, prices: List[int]) -> int:
        """
        7, 1, 5, 3, 6, 4

        -6, -2, -4, -1, -3
             4,  2,  5,  3
                -2,  1, -1
                     3,  1
                        -2
        """
        memo = {}

        def trace(buy: int, sell: int, profit: int) -> int:
            if buy > sell or sell >= len(prices):
                return profit

            if (buy, sell, profit) in memo:
                return memo[(buy, sell, profit)]

            next_profit = prices[sell] - prices[buy]

            profit1 = trace(buy, sell + 1, profit)
            profit2 = trace(buy + 1, sell + 1, profit)
            profit3 = 0
            if next_profit > 0:
                profit3 = trace(sell + 1, sell + 1, next_profit + profit)

            memo[(buy, sell, profit)] = max(profit, profit1, profit2, profit3)
            return memo[(buy, sell, profit)]

        result = trace(0, 1, 0)
        return result


if __name__ == "__main__":
    tests = [
        [[7, 1, 5, 3, 6, 4]],
        [[1, 2, 3, 4, 5]],
        [[7, 6, 4, 3, 1]],
        [[random.randint(0, 10**4) for _ in range(30)]],
    ]
    answers = [7, 4, 0, -1]

    tester = Tester(Solution().maxProfit2)
    tester.test(tests, answers)
