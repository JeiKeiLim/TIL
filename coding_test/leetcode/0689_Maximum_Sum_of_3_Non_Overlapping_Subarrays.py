from tester import Tester

from typing import List

import random

"""
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum
and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed).
If there are multiple answers, return the lexicographically smallest one.

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]

Constraints:
1 <= nums.length <= 2 * 10^4
1 <= nums[i] < 2^16
1 <= k <= floor(nums.length / 3)
"""


class Solution:
    def maxSumOfThreeSubarrays2(self, nums: List[int], k: int) -> List[int]:
        local_sum = sum(nums[:k])
        s_nums = [0] * (len(nums) - k + 1)
        s_nums[0] = local_sum
        for i in range(k, len(nums)):
            local_sum += nums[i] - nums[i - k]
            s_nums[i - k + 1] = local_sum

        left_idx = [0] * len(s_nums)
        max_idx = 0
        for i in range(len(s_nums)):
            if s_nums[i] > s_nums[max_idx]:
                max_idx = i

            left_idx[i] = max_idx

        right_idx = [0] * len(s_nums)
        max_idx = len(s_nums)-1
        for i in range(len(s_nums)-1, -1, -1):
            if s_nums[i] >= s_nums[max_idx]:
                max_idx = i

            right_idx[i] = max_idx

        max_val = 0
        result = [-1, -1, -1]
        for mid in range(k, len(s_nums)-k):
            left = left_idx[mid - k]
            right = right_idx[mid + k]

            local_sum = s_nums[left] + s_nums[mid] + s_nums[right]
            if local_sum > max_val:
                max_val = local_sum
                result = [left, mid, right]
            elif local_sum == max_val:
                result = min(result, [left, mid, right])

        return result

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        [1, 2, 1, / 2, 6, 7, / 5, 1]
        """
        memo = {}

        def trace(indices: List[int]):
            if (indices[-1] + k) > len(nums):
                return

            for i in range(len(indices) - 1):
                if (indices[i] + k) > indices[i + 1]:
                    return

            key = tuple([-idx for idx in indices])

            if key in memo:
                return memo[key]

            local_sum = 0
            for idx in indices:
                local_sum += sum(nums[idx : idx + k])

            memo[key] = local_sum

            for i in range(len(indices)):
                new_indices = indices.copy()
                new_indices[i] += 1

                trace(new_indices)

        indices = [i * k for i in range(3)]
        trace(indices)

        result = max(memo, key=lambda x: (memo[x], x))
        return [-idx for idx in result]


if __name__ == "__main__":
    tests = [
        [[1, 2, 1, 2, 6, 7, 5, 1], 2],
        [[1, 2, 1, 2, 1, 2, 1, 2, 1], 2],
        [[4, 3, 2, 1], 1],
        [[7, 13, 20, 19, 19, 2, 10, 1, 1, 19], 3],
        [[random.randint(1, 2**16) for _ in range(300)], 45],
    ]
    answers = [
        [0, 3, 5],
        [0, 2, 4],
        [0, 1, 2],
        [1, 4, 7],
        [-1, -1, -1],
    ]

    tester = Tester(Solution().maxSumOfThreeSubarrays2)
    tester.test(tests, answers)
