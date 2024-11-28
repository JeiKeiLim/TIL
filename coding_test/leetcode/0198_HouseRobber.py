from tester import Tester  # Assuming you have a Tester class for running tests

from typing import List

"""
198. House Robber
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected, and it will automatically contact the police if two adjacent houses are broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

### Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4.

### Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9), and rob house 5 (money = 1). Total amount you can rob = 2 + 9 + 1 = 12.

### Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400
"""


class Solution3:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)

        for i in range(2, len(nums)+2):
            dp[i] = max(dp[i-1], nums[i-2] + dp[i-2])

        return dp[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        O(n^2) solution?
        TODO: I may need to revisit here to improve its time complexity
        """

        def trace(nums: List[int], money: int) -> int:
            if len(nums) == 0:
                return money

            return max(trace(nums[2:], money + nums[0]), trace(nums[1:], money))

        return trace(nums, 0)


class Solution2:
    def rob(self, nums: List[int]) -> int:
        """
        O(n) solution
        """
        memo = {}

        def trace(idx: int) -> int:
            if idx >= len(nums):
                return 0

            if idx in memo:
                return memo[idx]

            memo[idx] = max(trace(idx + 1), nums[idx] + trace(idx + 2))
            return memo[idx]

        return trace(0)


if __name__ == "__main__":
    # Test cases
    tests = [
        [[1, 2, 3, 1]],  # Example 1
        [[2, 7, 9, 3, 1]],  # Example 2
        [[2, 7, 9, 3, 1] * 6],  # Example 2
    ]
    answers = [
        4,  # Expected output for Example 1
        12,  # Expected output for Example 2
        67,
    ]

    tester = Tester(Solution3().rob)
    tester.test(tests, answers)
