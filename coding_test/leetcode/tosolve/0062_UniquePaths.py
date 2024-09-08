from tester import Tester  # Assuming you have a Tester class for running tests

"""
62. Unique Paths
Medium

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

### Example 1:
Input: m = 3, n = 7
Output: 28

### Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

### Constraints:
- 1 <= m, n <= 100
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        (3, 7),  # Example 1
        (3, 2),  # Example 2
    ]
    answers = [
        28,  # Expected output for Example 1
        3,  # Expected output for Example 2
    ]

    tester = Tester(Solution().uniquePaths)
    tester.test(tests, answers)
