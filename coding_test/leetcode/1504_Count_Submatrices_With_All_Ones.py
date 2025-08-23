from tester import Tester

from typing import List

"""
Given an m x n binary matrix mat, return the number of submatrices that have all ones.

A submatrix is a rectangular section of the matrix with only 1s.

Example 1:
Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
Output: 13
Explanation:
- 6 rectangles of 1x1
- 2 rectangles of 1x2
- 3 rectangles of 2x1
- 1 rectangle of 2x2
- 1 rectangle of 3x1

Example 2:
Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
Output: 24
Explanation:
- 8 rectangles of 1x1
- 5 rectangles of 1x2
- 2 rectangles of 1x3
- 4 rectangles of 2x1
- 2 rectangles of 2x2
- 2 rectangles of 3x1
- 1 rectangle of 3x2

[0,1,2,0]
[0,1,2,3]
[1,2,3,0]

Constraints:
- 1 <= m, n <= 150
- mat[i][j] is either 0 or 1
"""


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(1, m):
                if mat[i][j] == 0:
                    continue
                mat[i][j] += mat[i][j-1]

        answer = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    continue
                min_width = mat[i][j]

                for k in range(i, -1, -1):
                    if mat[k][j] == 0:
                        break
                    min_width = min(min_width, mat[k][j])
                    answer += min_width

        return answer


if __name__ == "__main__":
    tests = [
        [[[1, 0, 1], [1, 1, 0], [1, 1, 0]]],
        [[[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]],
        [[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]],
        # [[[1] * 150 for _ in range(150)]]
    ]
    answers = [13, 24, 100, 128255625]

    tester = Tester(Solution().numSubmat2)
    tester.test(tests, answers)
