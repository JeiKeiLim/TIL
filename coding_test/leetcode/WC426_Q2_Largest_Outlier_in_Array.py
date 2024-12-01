from sys import version
from tester import Tester
import random

"""
You are given an integer array nums. This array contains n elements, where exactly n - 2 elements are special numbers. One of the remaining two elements is the sum of these special numbers, and the other is an outlier.

An outlier is defined as a number that is neither one of the original special numbers nor the element representing the sum of those numbers.

Return the largest potential outlier in nums.

Example 1:
Input: nums = [2,3,5,10]
Output: 10

Example 2:
Input: nums = [-2,-1,-3,-6,4]
Output: 4

Example 3:
Input: nums = [1,1,1,1,1,5,5]
Output: 5

Constraints:
3 <= nums.length <= 10^5
-1000 <= nums[i] <= 1000
The input is generated such that at least one potential outlier exists in nums.
"""


class Solution:
    def largestOutlier(self, nums: list[int]) -> int:
        num_map = {}
        for n in nums:
            num_map[n * 10] = num_map.get(n * 10, 0) + 1

        sum_all = sum(nums)
        sum_nums = [sum_all - n for n in nums]
        largest_outlier = min(nums)
        for i in range(len(nums)):
            key = ((sum_nums[i] / 2) * 10)
            if key in num_map and (num_map[key] > 1 or (key // 10) != nums[i]):
                if largest_outlier < nums[i]:
                    largest_outlier = nums[i]

        return largest_outlier


if __name__ == "__main__":
    tests = [
        [[2, 3, 5, 10]],
        [[-2, -1, -3, -6, 4]],
        [[1, 1, 1, 1, 1, 5, 5]],
        [[-108, -108, -517, -216]],
        [[6, -31, 50, -35, 41, 37, -42, 13]],
    ]

    long_test = [random.randint(-1000, 1000) for _ in range(10000)]
    long_test.insert(random.randint(0, len(long_test)), sum(long_test))
    long_test_answer = random.randint(-1000, 1000)
    long_test.insert(random.randint(0, len(long_test)), long_test_answer)
    tests.append([long_test])

    answers = [10, 4, 5, -517, -35, long_test_answer]

    tester = Tester(Solution().largestOutlier, verbose=0)
    tester.test(tests, answers)
