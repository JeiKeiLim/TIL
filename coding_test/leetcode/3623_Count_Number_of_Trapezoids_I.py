from tester import Tester, generate_random_2d_int_array

from typing import List

"""
You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates 
of the ith point on the Cartesian plane.

A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides 
(i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

Return the number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.
Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:
Input: points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
Output: 3
Explanation:
There are three distinct horizontal trapezoids:
- Using points [1,0], [2,0], [3,2], and [2,2].
- Using points [2,0], [3,0], [3,2], and [2,2].
- Using points [1,0], [3,0], [3,2], and [2,2].

0: 1,2,3
2: 2,3

Example 2:
Input: points = [[0,0],[1,0],[0,1],[2,1]]
Output: 1
Explanation:
- One trapezoid can be formed using [0,0],[1,0],[0,1],[2,1].
0: 0,1
1: 0,2

Example 3:
Input: points = [[1,0],[2,0],[3,0],[2,2],[3,2],[3,3],[4,3]]
Output: 3

0: 1,2,3
2: 3,4
3: 2,3

Constraints:
- 4 <= points.length <= 10^5
- –10^8 <= xi, yi <= 10^8
- All points are pairwise distinct.
"""

from collections import Counter
from math import comb


class Solution:
    def countTrapezoids2(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7

        y_counts = Counter(p[1] for p in points)

        prefix_sum = 0
        prefix_sum_squared = 0
        for count in y_counts.values():
            if count < 2:
                continue
            n_comb = comb(count, 2)
            prefix_sum = (prefix_sum + n_comb) % MOD
            prefix_sum_squared = (
                prefix_sum_squared + (n_comb % MOD) * (n_comb % MOD)
            ) % MOD

        sqaure_sum = (prefix_sum * prefix_sum) % MOD
        numerator = (sqaure_sum - prefix_sum_squared + MOD) % MOD
        mod_inverse_of_2 = pow(2, MOD - 2, MOD)

        return (numerator * mod_inverse_of_2) % MOD

    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7

        y_counts = Counter(p[1] for p in points)

        y_levels = [y for y, count in y_counts.items() if count >= 2]

        total_trapezoids = 0
        n = len(y_levels)

        for i in range(n):
            count1 = y_counts[y_levels[i]]
            num_pairs_on_line1 = comb(count1, 2)
            for j in range(i + 1, n):
                count2 = y_counts[y_levels[j]]
                num_pairs_on_line2 = comb(count2, 2)

                total_trapezoids += (num_pairs_on_line1 * num_pairs_on_line2) % MOD

        return total_trapezoids % MOD


if __name__ == "__main__":
    tests = [
        [[[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]],
        [[[0, 0], [1, 0], [0, 1], [2, 1]]],
        [[[1, 0], [2, 0], [3, 0], [3, 2], [4, 2], [2, 3], [3, 3]]],
        [[[1, 0], [2, 0], [3, 0], [2, 2], [3, 2], [3, 3], [4, 3]]],
        [generate_random_2d_int_array(2 * 10**4, 2, start_n=0, end_n=10**5)],
    ]
    answers = [3, 1, 7, 7, Solution().countTrapezoids(*tests[-1])]

    tester = Tester(Solution().countTrapezoids2)
    tester.test(tests, answers)
