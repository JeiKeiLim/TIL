from tester import Tester

from typing import List

"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
1. m == matrix.length
2. n == matrix[i].length
3. 1 <= m, n <= 10
4. -100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        barriers = [0, 0, 0, 0]

        row, col = 0, 0
        dir_idx = 0
        result = [matrix[0][0]]
        for i in range(len(matrix) * len(matrix[0]) - 1):
            dr, dc = directions[dir_idx]
            next_row = row + dr
            next_col = col + dc

            if (
                (dir_idx == 0 and (next_col + barriers[dir_idx]) >= len(matrix[0]))
                or (dir_idx == 1 and (next_row + barriers[dir_idx]) >= len(matrix))
                or (dir_idx == 2 and next_col < barriers[dir_idx])
                or (dir_idx == 3 and next_row < barriers[dir_idx])
            ):
                barrier_idx = (dir_idx - 1) % len(barriers)
                dir_idx = (dir_idx + 1) % len(directions)
                barriers[barrier_idx] += 1

                dr, dc = directions[dir_idx]
                next_row = row + dr
                next_col = col + dc

            result.append(matrix[next_row][next_col])
            row = next_row
            col = next_col
        return result


if __name__ == "__main__":
    tests = [
        [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]],
        [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]],
    ]
    answers = [
        [1, 2, 3, 6, 9, 8, 7, 4, 5],
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
    ]

    tester = Tester(Solution().spiralOrder)
    tester.test(tests, answers)
