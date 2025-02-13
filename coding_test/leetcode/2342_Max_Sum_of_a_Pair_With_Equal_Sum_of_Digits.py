from tester import Tester, generate_random_int_array

from typing import List
import itertools

"""
You are given a 0-indexed array nums consisting of positive integers.
You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

Example 1:
Input: nums = [18,43,36,13,7]
Output: 54
Explanation:
- The pairs (i, j) that satisfy the conditions are:
  (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
  (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
- So the maximum sum that we can obtain is 54.

9: 0, 2
7: 1, 3
4: 2


Example 2:
Input: nums = [10,12,19,14]
Output: -1
Explanation:
- There are no two numbers that satisfy the conditions, so we return -1.

Constraints:
1. 1 <= nums.length <= 10^5
2. 1 <= nums[i] <= 10^9
"""


class Solution:
    def maximumSum2(self, nums: List[int]) -> int:
        max_sums = [0] * 82
        answer = -1
        for num in nums:
            key = 0
            n = num
            while n:
                key, n = key + n % 10, n // 10

            if max_sums[key] != 0:
                answer = max(max_sums[key] + num, answer)

            max_sums[key] = max(max_sums[key], num)

        return answer

    def maximumSum(self, nums: List[int]) -> int:
        pair_map = {}
        for i, num in enumerate(nums):
            key = 0
            while num:
                key, num = key + num % 10, num // 10

            if key not in pair_map:
                pair_map[key] = []

            pair_map[key].append(i)

        pair_map = {key: val for key, val in pair_map.items() if len(val) > 1}
        if len(pair_map) < 1:
            return -1

        max_pair = 0
        for indices in pair_map.values():
            values = sorted(nums[i] for i in indices)
            max_pair = max(max_pair, values[-1] + values[-2])

        return max_pair


if __name__ == "__main__":
    tests = [
        [[18, 43, 36, 13, 7]],
        [[10, 12, 19, 14]],
        [generate_random_int_array(10**6, start_n=1, end_n=10**9)],
    ]
    answers = [54, -1, Solution().maximumSum(*tests[-1])]

    tester = Tester(Solution().maximumSum2)
    tester.test(tests, answers)
