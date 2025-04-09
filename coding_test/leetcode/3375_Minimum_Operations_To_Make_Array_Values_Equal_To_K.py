from tester import Tester
from typing import List

"""
You are given an integer array nums and an integer k.
An integer h is called valid if all values in the array that are strictly greater than h are identical.

You are allowed to perform the following operation on nums:
- Select an integer h that is valid for the current values in nums.
- For each index i where nums[i] > h, set nums[i] to h.

Return the minimum number of operations required to make every element in nums equal to k. If it is impossible to make all elements equal to k, return -1.

Example 1:
Input: nums = [5,2,5,4,5], k = 2
Output: 2
The operations can be performed in order using valid integers 4 and then 2.

Example 2:
Input: nums = [2,1,2], k = 2
Output: -1

Example 3:
Input: nums = [9,7,5,3], k = 1
Output: 4
The operations can be performed using valid integers in the order 7, 5, 3, and 1.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
- 1 <= k <= 100
"""


class Solution:
    def minimumOperationsToMakeK(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        if min(num_set) < k:
            return -1

        if k in num_set:
            return len(num_set) - 1

        return len(num_set)



if __name__ == "__main__":
    tests = [
        [[5, 2, 5, 4, 5], 2],
        [[2, 1, 2], 2],
        [[9, 7, 5, 3], 1],
    ]
    answers = [
        2,
        -1,
        4,
    ]

    tester = Tester(Solution().minimumOperationsToMakeK)
    tester.test(tests, answers)
