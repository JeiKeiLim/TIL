from tester import Tester, generate_random_int_array
from typing import List

"""
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j)
where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.

Example 1:
Input: nums = [3,1,2,2,2,1,3], k = 2
Output: 4

Example 2:
Input: nums = [1,2,3,4], k = 1
Output: 0

Constraints:
1 <= nums.length <= 100
1 <= nums[i], k <= 100
"""


class Solution:
    def countPairs3(self, nums: List[int], k: int) -> int:
        num_map = {}
        answer = 0
        for i, num in enumerate(nums):
            if num not in num_map:
                num_map[num] = [i]
            else:
                num_map[num].append(i)

            if len(num_map[num]) < 2:
                continue

            for j in num_map[num][:-1]:
                if (i * j) % k == 0:
                    answer += 1

        return answer

    def countPairs2(self, nums: List[int], k: int) -> int:
        num_map = {}
        for i, num in enumerate(nums):
            if num not in num_map:
                num_map[num] = [i]
            else:
                num_map[num].append(i)

        answer = 0
        for indices in num_map.values():
            if len(indices) < 2:
                continue

            for o, i in enumerate(indices[:-1]):
                for j in indices[(o + 1) :]:
                    if (i * j) % k == 0:
                        answer += 1
        return answer

    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        answer = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                m = i * j
                if m % k == 0 and nums[i] == nums[j]:
                    answer += 1
        return answer


if __name__ == "__main__":
    tests = [
        [[3, 1, 2, 2, 2, 1, 3], 2],
        [[1, 2, 3, 4], 1],
        [[5] * 10000, 1],
        [generate_random_int_array(10**3), 33],
    ]
    answers = [
        4,
        0,
        49995000,
        Solution().countPairs(*tests[-1]),
    ]

    tester = Tester(Solution().countPairs3)
    tester.test(tests, answers)
