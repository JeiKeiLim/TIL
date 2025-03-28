from tester import Tester, generate_random_int_array
from typing import List

from collections import Counter

"""
An element x of an integer array arr of length m is dominant if more than half the elements of arr have a value of x.
You are given a 0-indexed integer array nums of length n with one dominant element.

You can split nums at an index i into two arrays nums[0, ..., i] and nums[i + 1, ..., n - 1], but the split is only valid if:
    • 0 <= i < n - 1
    • nums[0, ..., i], and nums[i + 1, ..., n - 1] have the same dominant element.

Return the minimum index of a valid split. If no valid split exists, return -1.

Example 1:
Input: nums = [1,2,2,2]
Output: 2
[1,2,2], [2]


Example 2:
Input: nums = [2,1,3,1,1,1,7,1,2,1]
Output: 4
[2,1,3,1,1], [1,7,1,2,1]

[0,1,1,2,3,4,4,5,5,6]
[1,1,2,2,2,2,3,3,4,4]


Example 3:
Input: nums = [3,3,3,3,7,2,2]
Output: -1

Constraints:
    • 1 <= nums.length <= 10^5
    • 1 <= nums[i] <= 10^9
    • nums has exactly one dominant element.
"""


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        num_map = Counter(nums)
        dominant_num, _ = max(num_map.items(), key=lambda x: x[1])

        doms = [int(nums[0] == dominant_num)]
        non_doms = [1 - doms[0]]

        for num in nums[1:]:
            is_dom = int(num == dominant_num)
            doms.append(doms[-1] + is_dom)
            non_doms.append(non_doms[-1] + (1 - is_dom))

        for i in range(n):
            if (
                doms[i] - non_doms[i] > 0
                and (doms[-1] - doms[i]) - (non_doms[-1] - non_doms[i]) > 0
            ):
                return i
        return -1


if __name__ == "__main__":
    tests = [
        [[1, 2, 2, 2]],
        [[2, 1, 3, 1, 1, 1, 7, 1, 2, 1]],
        [[3, 3, 3, 3, 7, 2, 2]],
        [generate_random_int_array(10**5, end_n=10**9)],
    ]
    answers = [2, 4, -1, -1]

    tester = Tester(Solution().minimumIndex)
    tester.test(tests, answers)
