from tester import Tester

from typing import List

"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3:
- -1 + 1 + 1 + 1 + 1 = 3
- +1 - 1 + 1 + 1 + 1 = 3
- +1 + 1 - 1 + 1 + 1 = 3
- +1 + 1 + 1 - 1 + 1 = 3
- +1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1

Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""


class Solution:
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        memo = {}

        def trace(idx: int, cumsum: int) -> int:
            if idx >= len(nums):
                return 1 if cumsum == target else 0

            if (idx, cumsum) in memo:
                return memo[(idx, cumsum)]

            add = trace(idx + 1, cumsum + nums[idx])
            sub = trace(idx + 1, cumsum - nums[idx])

            memo[(idx, cumsum)] = add + sub

            return add + sub

        return trace(0, 0)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def trace(ops: List[int], idx: int) -> None:
            key = tuple(ops)
            if key in memo:
                return

            memo[key] = sum(ops)

            for i in range(idx, len(ops)):
                if nums[i] == 0:
                    continue
                new_ops = ops.copy()
                new_ops[i] *= -1
                trace(new_ops, idx + 1)

        trace(nums.copy(), 0)

        n_zeros = sum([1 for n in nums if n == 0])
        result = sum([1 for i in memo.values() if i == target])

        return result * (2**n_zeros)


if __name__ == "__main__":
    tests = [
        [[1, 1, 1, 1, 1], 3],
        [[1], 1],
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 1],
        [
            [10, 9, 6, 4, 19, 0, 41, 30, 27, 15, 14, 39, 33, 7, 34, 17, 24, 46, 2, 46],
            45,
        ],
        [
            [43, 1, 49, 22, 41, 1, 11, 1, 24, 10, 26, 49, 33, 4, 20, 19, 44, 42, 2, 37],
            17,
        ],
        [[20, 48, 33, 16, 19, 44, 14, 31, 42, 34, 38, 32, 27, 7, 22, 22, 48, 18, 48, 39], 1],
    ]
    answers = [
        5,
        1,
        524288,
        6606,
        6162,
        0,
    ]

    tester = Tester(Solution().findTargetSumWays2)
    tester.test(tests, answers)
