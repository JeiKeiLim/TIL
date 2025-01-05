from tester import Tester

from typing import List
from math import prod
import math

"""
You are given an array of positive integers nums.

An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:
- prod(arr) is the product of all elements of arr.
- gcd(arr) is the GCD of all elements of arr.
- lcm(arr) is the LCM of all elements of arr.

Return the length of the longest product equivalent subarray of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

The term gcd(a, b) denotes the greatest common divisor of a and b.
The term lcm(a, b) denotes the least common multiple of a and b.

Example 1:
Input: nums = [1,2,1,2,1,1,1]
Output: 5
Explanation: The longest product equivalent subarray is [1, 2, 1, 1, 1],
where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

Example 2:
Input: nums = [2,3,4,5,6]
Output: 3
Explanation: The longest product equivalent subarray is [3, 4, 5].

Example 3:
Input: nums = [1,2,3,1,4,5,1]
Output: 5

Constraints:
1. 2 <= nums.length <= 100
2. 1 <= nums[i] <= 10
"""


def lcm(nums: List[int]) -> int:
    if len(nums) < 2:
        return nums[0]

    n = (nums[0] * nums[1]) // math.gcd(nums[0], nums[1])
    for i in range(2, len(nums)):
        n = (n * nums[i]) // math.gcd(n, nums[i])
    return n


def gcd(nums: List[int]) -> int:
    if len(nums) < 2:
        return nums[0]

    n = math.gcd(nums[0], nums[1])
    for i in range(2, len(nums)):
        n = math.gcd(n, nums[i])
    return n


class Solution:
    def longestProductEquivalentSubarray(self, nums: List[int]) -> int:
        max_num = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                n_prod = prod(nums[i:j])
                n_gcd = gcd(nums[i:j])
                n_lcm = lcm(nums[i:j])
                if n_prod == (n_gcd * n_lcm):
                    max_num = max(max_num, j - i)
        return max_num


if __name__ == "__main__":
    tests = [
        [[1, 2, 1, 2, 1, 1, 1]],
        [[2, 3, 4, 5, 6]],
        [[1, 2, 3, 1, 4, 5, 1]],
    ]
    answers = [5, 3, 5]

    tester = Tester(Solution().longestProductEquivalentSubarray)
    tester.test(tests, answers)
