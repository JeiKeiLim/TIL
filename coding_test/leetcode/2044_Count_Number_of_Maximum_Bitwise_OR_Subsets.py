from tester import Tester, generate_random_int_array

from typing import List

"""
Given an integer array nums, find the maximum possible bitwise OR of a subset of nums 
and return the number of different non-empty subsets with the maximum bitwise OR.

Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1].

Example 1:
Input: nums = [3,1]
Output: 2
Explanation: Subsets with OR = 3 are [3] and [3,1].

Example 2:
Input: nums = [2,2,2]
Output: 7
Explanation: All 2^3 - 1 = 7 non-empty subsets have OR = 2.
[0], [1], [2], [0,1], [0,2], [1,2], [0,1,2]

Example 3:
Input: nums = [3,2,1,5]
Output: 6
Explanation: There are 6 subsets with OR = 7.


Constraints:
- 1 <= nums.length <= 16
- 1 <= nums[i] <= 10^5
"""

from itertools import combinations


class Solution:
    def countMaxOrSubsets3(self, nums: List[int]) -> int:
        n = len(nums)
        max_or_value = 0
        for num in nums:
            max_or_value |= num

        def dfs(idx: int, or_value: int) -> int:
            if idx == n:
                return 1 if or_value == max_or_value else 0

            return dfs(idx + 1, or_value | nums[idx]) + dfs(idx + 1, or_value)

        return dfs(0, 0)

    def countMaxOrSubsets2(self, nums: List[int]) -> int:
        n = len(nums)
        max_or_value = 0
        for num in nums:
            max_or_value |= num

        queue = [(0, 0)]
        answer = 0
        while queue:
            idx, or_value = queue.pop()

            if idx >= n:
                if or_value == max_or_value:
                    answer += 1
                continue
            queue.append((idx + 1, or_value | nums[idx]))
            queue.append((idx + 1, or_value))

        return answer

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        value_cnt = {}
        for i in range(1, n + 1):
            for sub_nums in combinations(nums, i):
                or_value = 0
                for num in sub_nums:
                    or_value = or_value | num

                if or_value not in value_cnt:
                    value_cnt[or_value] = 1
                else:
                    value_cnt[or_value] += 1

        max_or_value = max(value_cnt.keys())
        return value_cnt[max_or_value]


if __name__ == "__main__":
    tests = [
        [[3, 1]],
        [[2, 2, 2]],
        [[3, 2, 1, 5]],
        [generate_random_int_array(16, start_n=1, end_n=10**5)],
    ]
    answers = [2, 7, 6, -1]

    tester = Tester(Solution().countMaxOrSubsets3)
    tester.test(tests, answers)
