from tester import Tester, generate_random_int_array

from typing import List

"""
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers
and the number of negative integers.

Example 1:
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

Example 2:
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

Example 3:
Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.

Constraints:
1. 1 <= nums.length <= 2000
2. -2000 <= nums[i] <= 2000
3. nums is sorted in a non-decreasing order.

Follow-up:
Can you solve the problem in O(log(n)) time complexity?
"""


class Solution:
    def maximumCount2(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid - 1

        neg_cnt = right + 1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 1:
                left = mid + 1
            else:
                right = mid - 1

        pos_cnt = len(nums) - left

        return max(pos_cnt, neg_cnt)

    def maximumCount(self, nums: List[int]) -> int:
        neg_idx = -1
        pos_idx = -1
        for i, n in enumerate(nums):
            if n < 0:
                neg_idx = i
            elif pos_idx < 0 and n > 0:
                pos_idx = i

        neg_cnt = neg_idx + 1
        if neg_idx < 0:
            neg_cnt = 0

        pos_cnt = len(nums) - pos_idx
        if pos_idx < 0:
            pos_cnt = 0

        return max(neg_cnt, pos_cnt)


if __name__ == "__main__":
    tests = [
        [[-2, -1, -1, 1, 2, 3]],
        [[-3, -2, -1, 0, 0, 1, 2]],
        [[5, 20, 66, 1314]],
        [[0, 0, 0, 0, 0, 0]],
        [sorted(generate_random_int_array(200000, start_n=-2000, end_n=2000))]
    ]
    answers = [3, 3, 4, 0, -1]

    tester = Tester(Solution().maximumCount2)
    tester.test(tests, answers)
