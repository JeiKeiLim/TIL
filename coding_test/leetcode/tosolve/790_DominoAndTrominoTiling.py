from tester import Tester  # Assuming you have a Tester class for running tests

"""
790. Domino and Tromino Tiling
Medium

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

Given an integer n, return the number of ways to tile a 2 x n board. Since the answer may be very large, return it modulo 10^9 + 7.

### Example 1:
Input: n = 3
Output: 5
Explanation: The five different ways are shown above.

### Example 2:
Input: n = 1
Output: 1

### Constraints:
- 1 <= n <= 1000
"""

MOD = 10**9 + 7


class Solution:
    def numTilings(self, n: int) -> int:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        (3),  # Example 1
        (1),  # Example 2
    ]
    answers = [
        5,  # Expected output for Example 1
        1,  # Expected output for Example 2
    ]

    tester = Tester(Solution().numTilings)
    tester.test(tests, answers)
