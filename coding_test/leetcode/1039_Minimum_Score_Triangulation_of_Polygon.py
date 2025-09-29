from tester import Tester, generate_random_int_array

from typing import List

"""
You have a convex n-sided polygon where each vertex has an integer value.
You are given an integer array values where values[i] is the value of the ith vertex in clockwise order.

Polygon triangulation is a process where you divide a polygon into a set of triangles, and the vertices of each triangle must also be vertices of the original polygon.
This process will result in n - 2 triangles.

For each triangle, the weight is the product of the values at its vertices.
The total score of the triangulation is the sum of these weights over all n - 2 triangles.

Return the minimum possible score that you can achieve with some triangulation of the polygon.

Example 1:
Input: values = [1,2,3]
Output: 6

   (1)
   / \
 (3)---(2)


Example 2:
Input: values = [3,7,4,5]
Output: 144

(3)----- (7)
 |     /  |
 |   /    |
 | /      |
(5)----- (4)

Triangles:
  (7,4,5) weight = 7*4*5 = 140
  (3,7,5) weight = 3*7*5 = 105
Total = 245

(3)----- (7)
 | \      |
 |   \    |
 |     \  |
(5)----- (4)

Triangles:
  (3,7,4) weight = 3*7*4 = 84
  (3,4,5) weight = 3*4*5 = 60
Total = 144

(3)-(7)-(4)-(5)

(3,7,4), (7,4,5)
(3,4,5), (3,7,5)

Example 3:
Input: values = [1,3,1,4,1,5]
Output: 13

(1) -- (3) -- (1) -- (4) -- (1) -- (5)

    (3)
   /   \
(1)     (1)
 |       |
(5)     (4)
   \   /
    (1)

Constraints:
• n == values.length
• 3 <= n <= 50
• 1 <= values[i] <= 100
"""


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        seen = {}

        def solve(i: int, j: int) -> int:
            if j < i + 2:
                return 0
            if (i, j) in seen:
                return seen[(i, j)]

            min_score = 2**31
            for k in range(i + 1, j):
                current_score = (
                    (values[i] * values[k] * values[j]) + solve(i, k) + solve(k, j)
                )
                min_score = min(min_score, current_score)

            seen[(i, j)] = min_score

            return min_score

        return solve(0, n - 1)


if __name__ == "__main__":
    tests = [
        [[1, 2, 3]],
        [[3, 7, 4, 5]],
        [[1, 3, 1, 4, 1, 5]],
        [generate_random_int_array(50, end_n=100)],
    ]
    answers = [6, 144, 13, -1]

    tester = Tester(Solution().minScoreTriangulation)
    tester.test(tests, answers)
