from tester import Tester, generate_random_2d_int_array

from typing import List

"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

[1,2,3]
[4,5,6]
[7,8,9]

(0,0),
(0,1), (1,0),
(2,0), (1,1), (0,2),
(1,2), (2,1),
(2,2)

(0,0),
(0,1), (1, -1)
(1, 0), (-1, 1), (-1, 1)
(1, 0), (1, -1)
(1, 0)

[1,2,3,4]
[5,6,7,8]
[8,9,10,11]
[12,13,14,15]

(0, 0) / (-1, 1)
(0, 1), (1, 0) / (2, -1)
(2, 0), (1, 1), (0, 2) / (-1, 3)
(0, 3), (1, 2), (2, 1), (3, 0) / (4, -1)
(3, 1), (2, 2), (1, 3) / (1, 4)
(2, 3), (3, 2) / (4, 1)
(3, 3)

[1,2,3,4]
[5,6,7,8]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 10^4
- 1 <= m * n <= 10^4
- -10^5 <= mat[i][j] <= 10^5
"""


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        n, m = len(mat), len(mat[0])
        i, j = 0, 0
        dy, dx = -1, 1  # Start by moving up-right
        answer = [0] * (n * m)

        # The loop will run exactly n * m times
        for k in range(n * m):
            answer[k] = mat[i][j]

            # Case 1: Moving UP-RIGHT
            if dy == -1 and dx == 1:
                if j == m - 1:  # Hit right wall
                    i += 1
                    dy, dx = 1, -1  # Flip to down-left
                elif i == 0:  # Hit top wall
                    j += 1
                    dy, dx = 1, -1  # Flip to down-left
                else:  # No collision, continue up-right
                    i += dy
                    j += dx
            # Case 2: Moving DOWN-LEFT
            else:  # dy == 1 and dx == -1
                if i == n - 1:  # Hit bottom wall
                    j += 1
                    dy, dx = -1, 1  # Flip to up-right
                elif j == 0:  # Hit left wall
                    i += 1
                    dy, dx = -1, 1  # Flip to up-right
                else:  # No collision, continue down-left
                    i += dy
                    j += dx

        return answer


if __name__ == "__main__":
    tests = [
        [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]],
        [[[1, 2, 3, 4], [5, 6, 7, 8]]],
        [[[1, 2], [3, 4]]],
        [generate_random_2d_int_array(10**4, 10**4, start_n=-(10**5), end_n=10**5)],
    ]
    answers = [
        [1, 2, 4, 7, 5, 3, 6, 8, 9],
        [1, 2, 5, 6, 3, 4, 7, 8],
        [1, 2, 3, 4],
        [-1]
    ]

    tester = Tester(Solution().findDiagonalOrder)
    tester.test(tests, answers)
