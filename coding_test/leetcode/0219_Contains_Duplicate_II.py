from tester import Tester
from typing import List

"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Started @ 11:04
        Ended @ 11:19
        """
        num_map = {}
        for i, n in enumerate(nums):
            if n in num_map and abs(i - num_map[n]) <= k:
                return True

            num_map[n] = i

        return False


if __name__ == "__main__":
    tests = [
        [[1, 2, 3, 1], 3],
        [[1, 0, 1, 1], 1],
        [[1, 2, 3, 1, 2, 3], 2],
        [[99, 99], 2],
        [list(range(-24500, 300000)), 35000]
    ]
    answers = [True, True, False, True, False]

    tester = Tester(Solution().containsNearbyDuplicate)
    tester.test(tests, answers)
