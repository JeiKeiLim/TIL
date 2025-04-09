from tester import Tester, generate_random_int_array
from typing import List

"""
You are given an integer array nums. You need to ensure that the elements in the array are distinct.
To achieve this, you can perform the following operation any number of times:
- Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.

Note: An empty array is considered to have distinct elements.
Return the minimum number of operations needed to make the elements in the array distinct.

Example 1:
Input: nums = [1,2,3,4,2,3,3,5,7]
Output: 2

Example 2:
Input: nums = [4,5,6,4,4]
Output: 2

Example 3:
Input: nums = [6,7,8,9]
Output: 0

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()
        for i in range(n - 1, -1, -1):
            if nums[i] in seen:
                return ((i + 1) // 3) + (1 if (i + 1) % 3 != 0 else 0)
            seen.add(nums[i])
        return 0


if __name__ == "__main__":
    tests = [
        [[1, 2, 3, 4, 2, 3, 3, 5, 7]],
        [[4, 5, 6, 4, 4]],
        [[6, 7, 8, 9]],
        [generate_random_int_array(10**6, end_n=100)],
    ]
    answers = [2, 2, 0, -1]

    tester = Tester(Solution().minOperations)
    tester.test(tests, answers)
