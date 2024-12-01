from tester import Tester

"""
You are given an m x n integer matrix matrix with the following two properties:
1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

The solution must be in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""


class Solution:
    def searchMatrix2(self, matrix: list[list[int]], target: int) -> bool:
        n_row = len(matrix)
        n_col = len(matrix[0])
        n_size = n_row * n_col

        left = 0
        right = n_size
        idx = (left + right) // 2
        prev_idx = idx + 1
        while idx != prev_idx:
            prev_idx = idx

            row_idx = idx // n_col
            col_idx = idx % n_col

            value = matrix[row_idx][col_idx]
            if value == target:
                return True
            elif value > target:
                right = idx
            else:
                left = idx

            idx = (left + right) // 2

        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Search in a row -> BS
        Search in the first columns -> Use BS for first and last column. 
                                       First column smaller than `target` and last column larger than `target`
                                       First and last larger -> go left
                                       First smaller and last larger -> Okay
                                       First larger and last smaller -> go left
                                       First and last smaller -> go right
        Finished in 20 mins
        """
        n_row = len(matrix)
        row_left = 0
        row_right = n_row
        row_idx = (row_left + row_right) // 2
        prev_row_idx = row_idx + 1
        while row_idx != prev_row_idx:
            prev_row_idx = row_idx
            if matrix[row_idx][0] <= target:
                if matrix[row_idx][-1] >= target:
                    break
                row_left = row_idx
            else:
                row_right = row_idx

            row_idx = (row_left + row_right) // 2

        n_col = len(matrix[row_idx])
        col_left = 0
        col_right = n_col
        col_idx = (col_left + col_right) // 2
        prev_col_idx = col_idx + 1
        while prev_col_idx != col_idx:
            prev_col_idx = col_idx
            if matrix[row_idx][col_idx] == target:
                return True
            elif matrix[row_idx][col_idx] > target:
                col_right = col_idx
            else:
                col_left = col_idx
            col_idx = (col_left + col_right) // 2

        return False


if __name__ == "__main__":
    tests = [
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13],
    ]
    answers = [
        True,
        False,
    ]

    tester = Tester(Solution().searchMatrix2)
    tester.test(tests, answers)
