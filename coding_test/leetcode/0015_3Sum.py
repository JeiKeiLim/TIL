from tester import Tester
import random

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that:
- i != j, i != k, and j != k
- nums[i] + nums[j] + nums[k] == 0

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = [0,1,1]
Output: []

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]

Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""


class Solution:
    def threeSum2(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []

        sorted_nums = sorted(nums)  # O(n log n)
        solutions = set()

        for i in range(len(sorted_nums) - 2):  # O(n)
            val = sorted_nums[i]

            if i > 0 and sorted_nums[i - 1] == val:
                continue

            j = i + 1
            k = len(sorted_nums) - 1

            while j < k:  # O(n^2)
                three_sum = val + sorted_nums[j] + sorted_nums[k]
                if three_sum == 0:
                    solutions.add(tuple(sorted([val, sorted_nums[j], sorted_nums[k]])))
                    j += 1
                    while sorted_nums[j - 1] == sorted_nums[j] and j < k:
                        j += 1
                elif three_sum > 0:
                    k -= 1
                else:
                    j += 1

        return [list(solution) for solution in solutions]

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Started @ 12:26
        Ended @
        """
        solutions = set()
        sorted_nums = sorted(nums)

        if len(sorted_nums) < 3:
            return []

        for i in range(len(sorted_nums) - 2):  # O(n)
            for j in range(len(sorted_nums) - 1, i + 1, -1):  # O(n^2)
                val = sorted_nums[j] + sorted_nums[i]

                prev_idx = 0
                idx = 1
                left = i + 1
                right = j
                while prev_idx != idx:  # O(n^2 log n)
                    prev_idx = idx
                    idx = (left + right) // 2
                    three_sum = val + sorted_nums[idx]

                    if three_sum == 0:
                        sorted_comb = sorted(
                            [sorted_nums[i], sorted_nums[j], sorted_nums[idx]]
                        )
                        solutions.add(tuple(sorted_comb))
                        break
                    elif three_sum > 0:
                        right = idx
                    else:
                        left = idx

        return [list(solution) for solution in solutions]


if __name__ == "__main__":
    tests = [
        [[-1, 0, 1, 2, -1, -4]],
        [[0, 1, 1]],
        [[0, 0, 0]],
        [[-2, 0, 1, 1, 2]],
        [[3, 0, -2, -1, 1, 2]],
        [[-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]],
        [[0, -4, -1, -4, -2, -3, 2]],
        [[-5, -1, -5, -4, 2, 1, -1, 2, -4, -3, -2, -4]],
        [list([0 for _ in range(3000)])],
        [[random.randint(-(10**5), 10**5) for _ in range(3000)]],
    ]
    answers = [
        [[-1, -1, 2], [-1, 0, 1]],
        [],
        [[0, 0, 0]],
        [[-2, 0, 2], [-2, 1, 1]],
        [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]],
        [[-4, 1, 3], [-4, -2, 6], [-4, 2, 2], [-2, -2, 4], [-4, 0, 4], [-2, 0, 2]],
        [[-2, 0, 2]],
        [[-4, 2, 2], [-3, 1, 2], [-1, -1, 2]],
        [[0, 0, 0]],
        [[]],
    ]

    tester = Tester(Solution().threeSum2, verbose=0)
    tester.test(tests, answers)
