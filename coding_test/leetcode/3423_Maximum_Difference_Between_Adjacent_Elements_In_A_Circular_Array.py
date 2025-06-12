from tester import Tester, generate_random_int_array
from typing import List

"""
Given a circular array nums, find the maximum absolute difference between adjacent elements.
Note: In a circular array, the first and last elements are adjacent.

Example 1:
Input: nums = [1,2,4]
Output: 3
Explanation: Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.

Example 2:
Input: nums = [-5,-10,-5]
Output: 5
Explanation: The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.

Constraints:
- 2 <= nums.length <= 100
- -100 <= nums[i] <= 100
"""


class Solution:
    def maxDiffCircular2(self, nums: List[int]) -> int:
        return max(
            abs(nums[0] - nums[-1]),
            max(abs(nums[i - 1] - nums[i]) for i in range(1, len(nums))),
        )

    def maxDiffCircular(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = abs(nums[0] - nums[-1])
        for i in range(1, n):
            max_diff = max(max_diff, abs(nums[i - 1] - nums[i]))

        return max_diff


if __name__ == "__main__":
    tests = [
        [[1, 2, 4]],
        [[-5, -10, -5]],
        [[1, 100]],
        [[-50, 0, 50]],
        [[0, 0, 0]],
        [generate_random_int_array(100_000, start_n=-1000, end_n=1000)],
    ]
    answers = [
        3,
        5,
        99,
        100,
        0,
        -1,
    ]

    tester = Tester(Solution().maxDiffCircular2)
    tester.test(tests, answers)
