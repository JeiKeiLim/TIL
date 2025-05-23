from tester import Tester, generate_random_int_array

from typing import List

"""
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.
A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, nums[i] < nums[i+1].
Note that a subarray of size 1 is ascending.

Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

Example 2:
Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

Example 3:
Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.

Constraints:
1. 1 <= nums.length <= 100
2. 1 <= nums[i] <= 100
"""


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        answer = 0
        max_sum = 0
        prev_val = 0
        for num in nums:
            if prev_val >= num:
                answer = max(answer, max_sum)
                max_sum = 0
            max_sum += num
            prev_val = num
        answer = max(answer, max_sum)
        return answer


if __name__ == "__main__":
    tests = [
        [[10, 20, 30, 5, 10, 50]],
        [[10, 20, 30, 40, 50]],
        [[12, 17, 15, 13, 10, 11, 12]],
        [[100, 10, 1]],
        [generate_random_int_array(10 ** 6)]
    ]
    answers = [65, 150, 33, 100, -1]

    tester = Tester(Solution().maxAscendingSum, verbose=0)
    tester.test(tests, answers)
