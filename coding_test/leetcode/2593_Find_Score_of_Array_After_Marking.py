from tester import Tester

import random

from typing import List

"""
You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:
1. Choose the smallest unmarked integer of the array. If there is a tie, choose the one with the smallest index.
2. Add the value of the chosen integer to score.
3. Mark the chosen element and its two adjacent elements if they exist.
4. Repeat until all the array elements are marked.

Return the score after applying the algorithm.

Example 1:
Input: nums = [2,1,3,4,5,2]
Output: 7
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
- 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
- 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
Our score is 1 + 2 + 4 = 7.


Example 2:
Input: nums = [2,3,5,1,3,2]
Output: 5
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,3,5,1,3,2].
- 2 is the smallest unmarked element, since there are two of them, we choose the left-most one, so we mark the one at index 0 and its right adjacent element: [2,3,5,1,3,2].
- 2 is the only remaining unmarked element, so we mark it: [2,3,5,1,3,2].
Our score is 1 + 2 + 2 = 5.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
"""


class Solution:
    def findScore2(self, nums: List[int]) -> int:
        """
        O(n log n)
        """
        score = 0
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1], reverse=False)
        s_idx = [x[0] for x in sorted_nums]

        i = 0

        while i < len(s_idx):
            smallest_idx = s_idx[i]
            i += 1
            if nums[smallest_idx] < 1:
                continue

            score += nums[smallest_idx]

            nums[smallest_idx] = -1
            if smallest_idx > 0 and nums[smallest_idx - 1] > 0:
                nums[smallest_idx - 1] = -1
            if smallest_idx < len(nums)-1 and nums[smallest_idx + 1] > 0:
                nums[smallest_idx + 1] = -1

        return score

    def findScore(self, nums: List[int]) -> int:
        """
        O(n^2)
        """
        score = 0
        total = sum(nums)

        while total > 0:
            min_idx = 0
            for i in range(len(nums)):
                if nums[i] > 0:
                    min_idx = i
                    break

            min_val = nums[min_idx]
            for i in range(min_idx + 1, len(nums)):
                if 0 < nums[i] < min_val:
                    min_val = nums[i]
                    min_idx = i

            score += nums[min_idx]
            pop_idx = [min_idx]
            if min_idx > 0 and nums[min_idx-1] > 0:
                pop_idx.append(min_idx-1)
            if min_idx < (len(nums)-1) and nums[min_idx+1] > 0:
                pop_idx.append(min_idx+1)

            for i in pop_idx:
                total -= nums[i]
                nums[i] = -1

        return score


if __name__ == "__main__":
    tests = [
        [[2, 1, 3, 4, 5, 2]],
        [[2, 3, 5, 1, 3, 2]],
        [[10, 44, 10, 8, 48, 30, 17, 38, 41, 27, 16, 33, 45, 45, 34, 30, 22, 3, 42, 42]],
        [[5, 1, 1, 7, 2, 4]],
        [[random.randint(1, 10**6) for _ in range(100000)]],
    ]
    answers = [
        7,
        5,
        212,
        3,
        -1,
    ]

    tester = Tester(Solution().findScore2, verbose=0)
    tester.test(tests, answers)
