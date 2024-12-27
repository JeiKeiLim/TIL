from tester import Tester

from typing import List
import random

"""
You are given an integer array values where values[i] represents the value of the ith sightseeing spot.
Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j:
the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

Example 1:

Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

Example 2:

Input: values = [1,2]
Output: 2

Constraints:
2 <= values.length <= 5 * 10^4
1 <= values[i] <= 1000
"""


class Solution:
    def maxScoreSightseeingPair2(self, values: List[int]) -> int:
        score = 0
        max_v1 = 0
        for i in range(len(values)):
            score = max(score, max_v1 + values[i] - i)
            max_v1 = max(max_v1, values[i] + i)

        return score

    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        for i in range(len(values) - 1):
            vii = values[i] + i
            for j in range(i + 1, len(values)):
                score = vii + values[j] - j
                max_score = max(max_score, score)

        return max_score


if __name__ == "__main__":
    tests = [
        [[8, 1, 5, 2, 6]],
        [[1, 2]],
        [[random.randint(1, 1000) for _ in range(10**4)]],
    ]
    answers = [11, 2, -1]

    tester = Tester(Solution().maxScoreSightseeingPair2, verbose=0)
    tester.test(tests, answers)
