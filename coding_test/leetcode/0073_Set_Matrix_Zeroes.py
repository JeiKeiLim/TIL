from typing import List
from tester import Tester, generate_random_2d_int_array

import tracemalloc

"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ]
Output: [
    [1,0,1],
    [0,0,0],
    [1,0,1]
    ]

Example 2:
Input: matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
    ]
Output: [
    [0,0,0,0],
    [0,4,5,0],
    [0,3,1,0]
    ]

Constraints:
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1

Follow up:
- Could you devise a constant space solution?
"""


class Solution:
    def setZeroes3(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])

        row_mask = 0
        col_mask = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row_mask |= (1 << i)
                    col_mask |= (1 << j)

        for i in range(n):
            if (row_mask >> i) & 1:
                for j in range(m):
                    matrix[i][j] = 0
        for j in range(m):
            if (col_mask >> j) & 1:
                for i in range(n):
                    matrix[i][j] = 0
        return matrix


    def setZeroes2(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Space: O(1)
        """
        n = len(matrix)
        m = len(matrix[0])
        marker = 'a'

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for row in range(n):
                        if matrix[row][j] == 0:
                            continue
                        matrix[row][j] = marker
                    for col in range(m):
                        if matrix[i][col] == 0:
                            continue
                        matrix[i][col] = marker

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == marker:
                    matrix[i][j] = 0

        return matrix
        

    def setZeroes(self, matrix: List[List[int]]) -> List[List[int]]:
        """Naive approach.

        Space: O(n+m)
        """
        n = len(matrix)
        m = len(matrix[0])

        rows = set()
        cols = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in rows:
            for j in range(m):
                matrix[i][j] = 0
        for i in range(n):
            for j in cols:
                matrix[i][j] = 0

        return matrix


if __name__ == "__main__":
    tests = [
        [[[1, 1, 1], [1, 0, 1], [1, 1, 1]]],
        [[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]],
        [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]],
        [[[0]]],
        [[[1, 0, 3]]],
        [generate_random_2d_int_array(200, 200, start_n=-2**7, end_n=2**7- 1)],
    ]
    answers = [
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[0]],
        [[0, 0, 0]],
        Solution().setZeroes([x.copy() for x in tests[-1][0]])
    ]

    tracemalloc.start()
    tester = Tester(Solution().setZeroes3)
    tracemalloc.stop()
    tester.test(tests, answers)
