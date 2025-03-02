from tester import Tester

from typing import List

"""
You are given an integer array nums and an integer k.

An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.

Return the largest almost missing integer from nums. If no such integer exists, return -1.

A subarray is a contiguous sequence of elements within an array.

Example 1:
Input: nums = [3,9,2,1,7], k = 3
Output: 7

Example 2:
Input: nums = [3,9,7,2,1,7], k = 4
Output: 3

Example 3:
Input: nums = [0,0], k = 1
Output: -1

Constraints:
1. 1 <= nums.length <= 50
2. 0 <= nums[i] <= 50
3. 1 <= k <= nums.length
"""


class Solution:
    def findLargestAlmostMissingInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        num_map = {}
        for i in range(n-k+1):
            local_nums = set(nums[i:i+k])
            for n in local_nums:
                num_map[n] = num_map.get(n, 0) + 1

        candidates = [key for key, val in num_map.items() if val == 1]

        if len(candidates) == 0:
            return -1

        return max(candidates)


if __name__ == "__main__":
    tests = [
        [[3, 9, 2, 1, 7], 3],
        [[3, 9, 7, 2, 1, 7], 4],
        [[0, 0], 1],
        [[0, 0], 2],
    ]
    answers = [7, 3, -1, 0]

    tester = Tester(Solution().findLargestAlmostMissingInteger)
    tester.test(tests, answers)
