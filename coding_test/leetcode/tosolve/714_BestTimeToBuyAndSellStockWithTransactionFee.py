from tester import Tester  # Assuming you have a Tester class for running tests

"""
714. Best Time to Buy and Sell Stock with Transaction Fee
Medium

You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:
- You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
- The transaction fee is only charged once for each stock purchase and sale.

### Example 1:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

### Example 2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6

### Constraints:
- 1 <= prices.length <= 5 * 10^4
- 1 <= prices[i] < 5 * 10^4
- 0 <= fee < 5 * 10^4
"""


class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        ([1, 3, 2, 8, 4, 9], 2),  # Example 1
        ([1, 3, 7, 5, 10, 3], 3),  # Example 2
    ]
    answers = [
        8,  # Expected output for Example 1
        6,  # Expected output for Example 2
    ]

    tester = Tester(Solution().maxProfit)
    tester.test(tests, answers)
