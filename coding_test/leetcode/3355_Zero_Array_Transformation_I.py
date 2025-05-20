from typing import List
from tester import Tester, generate_random_int_array
from collections import Counter

"""
You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

For each queries[i]:
- Select a subset of indices within the range [li, ri] in nums.
- Decrement the values at the selected indices by 1.

A Zero Array is an array where all elements are equal to 0.
Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.

Example 1:
Input: nums = [1,0,1], queries = [[0,2]]
Output: true

Example 2:
Input: nums = [4,3,2,1], queries = [[1,3],[0,2]]
Output: false


Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
- 1 <= queries.length <= 10^5
- queries[i].length == 2
- 0 <= li <= ri < nums.length
"""


class Solution:
    def canTransformToZeroArray3(
        self, nums: List[int], queries: List[List[int]]
    ) -> bool:
        n = len(nums)
        delta = [0] * (n + 1)
        for l, r in queries:
            delta[l] += 1
            delta[r + 1] -= 1

        x = 0
        for i in range(n):
            x += delta[i]
            if x < nums[i]:
                return False

        return True

    def canTransformToZeroArray2(
        self, nums: List[int], queries: List[List[int]]
    ) -> bool:
        n = len(nums)
        inc_map = Counter([x[0] for x in queries])
        dec_map = Counter([x[1] for x in queries])

        x = 0
        total = sum(nums)
        for i in range(n):
            if i in inc_map:
                x += inc_map[i]

            if nums[i] > 0:
                cx = min(nums[i], x)
                nums[i] -= cx
                total -= cx

            if i in dec_map:
                x -= dec_map[i]

        return total == 0

    def canTransformToZeroArray(
        self, nums: List[int], queries: List[List[int]]
    ) -> bool:
        """Naive approach."""
        total = sum(nums)
        for li, ri in queries:
            for i in range(li, ri + 1):
                if nums[i] == 0:
                    continue
                total -= 1
                nums[i] -= 1
        return total == 0


if __name__ == "__main__":
    tests = [
        [[1, 0, 1], [[0, 2]]],
        [[4, 3, 2, 1], [[1, 3], [0, 2]]],
        [[2, 2, 2], [[0, 1], [1, 2], [0, 2]]],
        [[0, 0, 0], []],
        [[1], [[0, 0]]],
        [
            generate_random_int_array(10**5, end_n=10**4),
            [
                sorted(generate_random_int_array(2, end_n=10**5 - 1))
                for _ in range(10**5)
            ],
        ],
    ]
    answers = [
        True,
        False,
        True,
        True,
        True,
        Solution().canTransformToZeroArray2(*tests[-1]),
    ]

    tester = Tester(Solution().canTransformToZeroArray3)
    tester.test(tests, answers)
