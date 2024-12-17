from tester import Tester

from typing import List

import heapq

"""
You are given an integer array nums, an integer k, and an integer multiplier.
You need to perform k operations on nums. In each operation:
1. Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
2. Replace the selected minimum value x with x * multiplier.

Return an integer array denoting the final state of nums after performing all k operations.

Example 1:
Input: nums = [2,1,3,5,6], k = 5, multiplier = 2
Output: [8,4,6,5,6]
Explanation:
Operation
Result
After operation 1
[2, 2, 3, 5, 6]
After operation 2
[4, 2, 3, 5, 6]
After operation 3
[4, 4, 3, 5, 6]
After operation 4
[4, 4, 6, 5, 6]
After operation 5
[8, 4, 6, 5, 6]

Example 2:
Input: nums = [1,2], k = 3, multiplier = 4
Output: [16,8]
Explanation:
Operation
Result
After operation 1
[4, 2]
After operation 2
[4, 8]
After operation 3
[16, 8]

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
1 <= k <= 10
1 <= multiplier <= 5
"""


class Solution:
    def finalState2(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        """O(k log n)"""
        if multiplier < 2:
            return nums

        s_nums = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(s_nums)

        for _ in range(k):
            _, min_idx = s_nums[0]

            nums[min_idx] *= multiplier
            heapq.heapreplace(s_nums, (nums[min_idx], min_idx))

        return nums


    def finalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        """O(k n)"""
        if multiplier < 2:
            return nums

        for _ in range(k):
            min_idx = 0
            for i in range(1, len(nums)):
                if nums[i] < nums[min_idx]:
                    min_idx = i

            nums[min_idx] *= multiplier

        return nums


if __name__ == "__main__":
    tests = [
        [[2, 1, 3, 5, 6], 5, 2],
        [[1, 2], 3, 4],
    ]
    answers = [
        [8, 4, 6, 5, 6],
        [16, 8],
    ]

    tester = Tester(Solution().finalState2)
    tester.test(tests, answers)
