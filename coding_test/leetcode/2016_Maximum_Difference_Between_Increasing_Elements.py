from tester import Tester, generate_random_int_array
from typing import List

"""
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] 
(i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.

Example 1:
Input: nums = [7,1,5,4]
Output: 4
Explanation:
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.

Example 2:
Input: nums = [9,4,3,2]
Output: -1
Explanation:
There is no i and j such that i < j and nums[i] < nums[j].

Example 3:
Input: nums = [1,5,2,10]
Output: 9
Explanation:
The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.

Constraints:
- n == nums.length
- 2 <= n <= 1000
- 1 <= nums[i] <= 10^9
"""


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_n = 10**9
        answer = -1
        for n in nums:
            min_n = min(min_n, n)
            diff = n - min_n
            if diff != 0 and diff > answer:
                answer = diff

        return answer


if __name__ == "__main__":
    tests = [
        [[7, 1, 5, 4]],
        [[9, 4, 3, 2]],
        [[1, 5, 2, 10]],
        [[2, 3]],
        [[100, 90, 80, 70]],
        [generate_random_int_array(10**6)],
    ]
    answers = [4, -1, 9, 1, -1, -1]

    tester = Tester(Solution().maximumDifference)
    tester.test(tests, answers)
