from tester import Tester, generate_random_2d_int_array

from typing import List

"""
Given an m x n binary matrix, return the total number of square submatrices that have all ones.

Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

Output: 15
Explanation:
- 10 squares of size 1
- 4 squares of size 2
- 1 square of size 3

Example 2:
Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
- 6 squares of size 1
- 1 square of size 2

Constraints:
- 1 <= matrix.length <= 300
- 1 <= matrix[0].length <= 300
- 0 <= matrix[i][j] <= 1
"""


class Solution:
    def countSquares3(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    continue

                min_square = min(
                    matrix[i - 1][j],
                    matrix[i - 1][j - 1],
                    matrix[i][j - 1],
                )
                if min_square == 0:
                    continue
                matrix[i][j] = min_square + 1
        return sum(map(sum, matrix))

    def countSquares2(self, matrix: List[List[int]]) -> int:
        """Naive 2"""
        n, m = len(matrix), len(matrix[0])

        def count_sqaure(si: int, sj: int, ei: int, ej: int) -> int:
            if ei == n or ej == m:
                return 0

            for i in range(si, ei + 1):
                if matrix[i][ej] != 1:
                    return 0
            for j in range(sj, ej + 1):
                if matrix[ei][j] != 1:
                    return 0
            return 1 + count_sqaure(si, sj, ei + 1, ej + 1)

        answer = 0
        for i in range(n):
            for j in range(m):
                answer += count_sqaure(i, j, i, j)
        return answer

    def countSquares(self, matrix: List[List[int]]) -> int:
        """Naive"""
        n, m = len(matrix), len(matrix[0])

        def count_sqaure(si: int, sj: int, ei: int, ej: int) -> int:
            if ei == n or ej == m:
                return 0

            for i in range(si, ei + 1):
                for j in range(sj, ej + 1):
                    if matrix[i][j] != 1:
                        return 0
            return 1 + count_sqaure(si, sj, ei + 1, ej + 1)

        answer = 0
        for i in range(n):
            for j in range(m):
                answer += count_sqaure(i, j, i, j)
        return answer


if __name__ == "__main__":
    tests = [
        [[[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]],
        [[[1, 0, 1], [1, 1, 0], [1, 1, 0]]],
        [[[1] * 300 for _ in range(300)]],
        [generate_random_2d_int_array(300, 300, start_n=0, end_n=1)],
    ]
    answers = [15, 7, 9045050, -1]

    tester = Tester(Solution().countSquares3)
    tester.test(tests, answers)
