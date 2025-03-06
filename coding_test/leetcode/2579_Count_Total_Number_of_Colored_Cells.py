from tester import Tester

"""
There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer n, indicating that you must do the following routine for n minutes:

1. At the first minute, color any arbitrary unit cell blue.
2. Every minute thereafter, color blue every uncolored cell that touches a blue cell.

Return the number of colored cells at the end of n minutes.

Example 1:
Input: n = 1
Output: 1

Example 2:
Input: n = 2
Output: 5

Constraints:
1. 1 <= n <= 10^5

n: 1 -> 1
1

n: 2 -> 5
 1
111
 1

n: 3 -> 13
  1
 111
11111
 111
  1

1, 1+2*4-4, 3*4-4+5
"""


class Solution:
    def coloredCells3(self, n: int) -> int:
        return 2*n*n - 2*n + 1

    def coloredCells2(self, n: int) -> int:
        return sum([i * 4 for i in range(n)]) + 1

    def coloredCells(self, n: int) -> int:
        """
        1+4+8+12+16+20 ...
        """
        num = 1
        for i in range(2, n + 1):
            num += i * 4 - 4

        return num


if __name__ == "__main__":
    tests = [
        [1],
        [2],
        [3],
        [4],
        [5],
        [6],
        [10**5],
    ]
    answers = [
        1,
        5,
        13,
        25,
        41,
        61,
        19999800001,
    ]

    tester = Tester(Solution().coloredCells3)
    tester.test(tests, answers)
