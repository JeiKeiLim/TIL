from tester import Tester
from typing import List

"""
2352. Equal Row and Column Pairs
Medium

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:

Input: grid = [
    [3,2,1],
    [1,7,6],
    [2,7,7]
    ]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:

Input: grid = [
    [3,1,2,2],
    [1,4,4,5],
    [2,4,2,2],
    [2,4,2,2]
    ]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
"""


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        O(n^3)

        TODO: Is it really optimal solution?
        """
        n_row = len(grid)
        n_col = len(grid[0])
        result = 0

        for row in range(n_row):
            target_grid_row = grid[row]

            for col in range(n_col):
                cmp_grid_col = [grid[i][col] for i in range(n_row)]
                is_eqaul = True

                for x, y in zip(target_grid_row, cmp_grid_col):
                    if x != y:
                        is_eqaul = False
                        break

                if is_eqaul:
                    result += 1

        return result


class Solution2:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        O(n^2)
        """
        n = len(grid)
        result = 0

        # Step 1: Convert each row to a tuple and count occurrences
        row_counts = {}
        for row in grid:
            row_tuple = tuple(row)
            if row_tuple in row_counts:
                row_counts[row_tuple] += 1
            else:
                row_counts[row_tuple] = 1

        # Step 2: Convert each column to a tuple and count occurrences
        col_counts = {}
        for col in range(n):
            col_tuple = tuple(grid[row][col] for row in range(n))
            if col_tuple in col_counts:
                col_counts[col_tuple] += 1
            else:
                col_counts[col_tuple] = 1

        # Step 3: Calculate the total number of equal pairs
        for row_tuple, count in row_counts.items():
            if row_tuple in col_counts:
                # Multiply the occurrences of the matching row and column
                result += count * col_counts[row_tuple]

        return result


if __name__ == "__main__":
    tests = [
        [[[3, 2, 1], [1, 7, 6], [2, 7, 7]]],
        [[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]],
    ]
    answers = [1, 3]

    tester = Tester(Solution2().equalPairs)
    tester.test(tests, answers)
