from tester import Tester
from typing import List

"""
You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that i < j < k.
If all such triplets have a negative value, return 0.

The value of a triplet (i, j, k) is:
    (nums[i] - nums[j]) * nums[k]

Example 1:
Input: nums = [12,6,1,2,7]
Output: 77
Explanation: The value of the triplet (0, 2, 4) is (12 - 1) * 7 = 77.

Example 2:
Input: nums = [1,10,3,4,19]
Output: 133
Explanation: The value of the triplet (1, 2, 4) is (10 - 3) * 19 = 133.

Example 3:
Input: nums = [1,2,3]
Output: 0
Explanation: The only triplet (0,1,2) gives (1-2)*3 = -3. Return 0.

Constraints:
- 3 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = nums[0]
        max_diff = 0
        answer = 0
        for i in range(1, n):
            max_diff = max(max_diff, max_num - nums[i-1])
            answer = max(answer, max_diff * nums[i])
            max_num = max(max_num, nums[i])
        return answer


if __name__ == "__main__":
    tests = [
        [[12, 6, 1, 2, 7]],
        [[1, 10, 3, 4, 19]],
        [[1, 2, 3]],
    ]
    answers = [
        77,
        133,
        0,
    ]

    tester = Tester(Solution().maximumTripletValue)
    tester.test(tests, answers)
