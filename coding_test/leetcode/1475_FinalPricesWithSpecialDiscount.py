from tester import Tester

from typing import List
import random

"""
You are given an integer array prices where prices[i] is the price of the ith item in a shop.

There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount
equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i].
Otherwise, you will not receive any discount at all.

Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop,
considering the special discount.

Example 1:
Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
Explanation:
- For item 0 with price[0] = 8, the discount is prices[1] = 4, so the final price is 8 - 4 = 4.
- For item 1 with price[1] = 4, the discount is prices[3] = 2, so the final price is 4 - 2 = 2.
- For item 2 with price[2] = 6, the discount is prices[3] = 2, so the final price is 6 - 2 = 4.
- For items 3 and 4, there is no discount.

Example 2:
Input: prices = [1,2,3,4,5]
Output: [1,2,3,4,5]
Explanation: In this case, for all items, there is no discount.

Example 3:
Input: prices = [10,1,1,6]
Output: [9,0,1,6]
Explanation:
- For item 0 with price[0] = 10, the discount is prices[1] = 1, so the final price is 10 - 1 = 9.
- For item 1 with price[1] = 1, the discount is prices[2] = 1, so the final price is 1 - 1 = 0.
- For item 2 with price[2] = 1, there is no discount.
- For item 3 with price[3] = 6, there is no discount.

Constraints:
1 <= prices.length <= 500
1 <= prices[i] <= 1000
"""


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """O(n^2)"""
        paid = []
        for i in range(len(prices)):
            price = prices[i]
            discount = 0
            for j in range(i+1, len(prices)):
                if prices[j] <= price:
                    discount = prices[j]
                    break

            paid.append(price-discount)

        return paid


if __name__ == "__main__":
    tests = [
        [[8, 4, 6, 2, 3]],
        [[1, 2, 3, 4, 5]],
        [[10, 1, 1, 6]],
        [[random.randint(1, 1000) for _ in range(10 ** 5)]]
    ]
    answers = [
        [4, 2, 4, 2, 3],
        [1, 2, 3, 4, 5],
        [9, 0, 1, 6],
        [-1],
    ]

    tester = Tester(Solution().finalPrices, verbose=0)
    tester.test(tests, answers)
