from tester import Tester, generate_random_int_array
from typing import List

from itertools import combinations
from collections import Counter

"""
Given an integer array nums, return true if you can partition the array into two subsets
such that the sum of the elements in both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

1,5,5,11

1
    1,5
        1,5,11
        1,5,5
    1,11
        1,11,5
    1,5
5
    5,11
        5,11,5
    5,5
11
    11,5
5

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

[1,2,2,5,1,3]

1,10,23,40

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100


i in range(target, num - 1, -1)
dp[i] or dp[i-num]

[T, T, T, T, T, T, F, F]

"""


class Solution:
    def canPartition3(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[-1]

    def canPartition2(self, nums: List[int]) -> bool:
        """
        2,3,4,8,9,14
        2+4+14
        3+8+9
        """
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        if target in nums:
            return True

        queue = [(nums[0], set([0]))]
        seen = set()
        while queue:
            local_sum, indices = queue.pop()
            indices_str = "".join(str(idx) for idx in sorted(indices))

            if indices_str in seen:
                continue
            seen.add(indices_str)

            if local_sum == target:
                return True
            if local_sum > target:
                continue

            for i in range(n):
                if i in indices:
                    continue
                new_indices = indices.copy()
                new_indices.add(i)
                queue.append((local_sum + nums[i], new_indices))

        return False

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        for m in range(1, n):
            for combs in combinations(nums, m):
                if sum(combs) == target:
                    return True
        return False


if __name__ == "__main__":
    tests = [
        [[1, 5, 11, 5]],
        [[1, 2, 3, 5]],
        [[1, 2, 2, 5, 1, 3]],
        [[14, 9, 8, 4, 3, 2]],
        [[100] * 97 + [99, 97]],
        [generate_random_int_array(200, end_n=100)],
    ]
    answers = [
        True,
        False,
        True,
        True,
        True,
        True,
        # Solution().canPartition(*tests[-1])
    ]

    tester = Tester(Solution().canPartition3)
    tester.test(tests, answers)
