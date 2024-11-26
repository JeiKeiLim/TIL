from tester import Tester
from typing import List

"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
- 0 <= j <= nums[i] and
- i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""


class Solution:
    def jump2(self, nums: List[int]) -> int:
        n_nums = len(nums)
        furthest = 0

        jumps  = 0
        current_position = 0

        for i in range(n_nums - 1):
            furthest = max(furthest, i + nums[i])

            if current_position == i:
                jumps += 1
                current_position = furthest

        return jumps



    def jump(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums) - 1

        memo = {}

        def trace(paths: List[int], n: int) -> int:
            key = tuple([n] + paths)
            if len(paths) < 2:
                return min(n, memo.get(key, n))

            if key in memo:
                return memo[key]

            num = paths[0]
            for i in range(1, num + 1):
                key = tuple([n + 1] + paths[i:])

                result = trace(paths[i:], n + 1)
                memo[key] = min(result, memo.get(key, result))

            return len(nums) + 1

        trace(nums, 0)
        return min(memo.values())



if __name__ == "__main__":
    tests = [
        [[2, 3, 1, 1, 4]],
        [[2, 3, 0, 1, 4]],
        [[0]],
        [[1, 2, 3]],
        [[1, 2, 1, 1, 1]],
        [[5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3, 8, 5]],
        [[5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3, 8, 5] * 40],
    ]
    answers = [2, 2, 0, 2, 3, 5, 200]

    tester = Tester(Solution().jump2, verbose=0)
    tester.test(tests, answers)
