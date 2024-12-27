from tester import Tester

from typing import List
import heapq
import random

"""
You are given an array of non-negative integers nums and an integer k.
In one operation, you may choose any element from nums and increment it by 1.

Return the maximum product of nums after at most k operations. Since the answer may be very large, return it modulo 10^9 + 7.
Note that you should maximize the product before taking the modulo.

Example 1:

Input: nums = [0,4], k = 5
Output: 20
Explanation: Increment the first number 5 times.
Now nums = [5, 4], with a product of 5 * 4 = 20.
It can be shown that 20 is maximum product possible, so we return 20.
Note that there may be other ways to increment nums to have the maximum product.

Example 2:

Input: nums = [6,3,3,2], k = 2
Output: 216
Explanation: Increment the second number 1 time and increment the fourth number 1 time.
Now nums = [6, 4, 3, 3], with a product of 6 * 4 * 3 * 3 = 216.
It can be shown that 216 is maximum product possible, so we return 216.

Constraints:
1 <= nums.length, k <= 10^5
0 <= nums[i] <= 10^6
"""


class Solution:
    def maxProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            n = heapq.heappop(nums) + 1
            heapq.heappush(nums, n)

        modulo = 10 ** 9 + 7

        result = 1
        for n in nums:
            result = (result * n) % modulo

        return result


if __name__ == "__main__":
    tests = [
        [[0, 4], 5],
        [[6, 3, 3, 2], 2],
        [[random.randint(0, 10**6) for _ in range(10 ** 5)], 10 ** 5]
    ]
    answers = [20, 216, -1]

    tester = Tester(Solution().maxProduct, verbose=0)
    tester.test(tests, answers)
