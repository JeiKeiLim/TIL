from tester import Tester  # Assuming you have a Tester class for running tests

"""
547. Number of Provinces
Medium

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:
- 1 <= n <= 200
- n == isConnected.length
- n == isConnected[i].length
- isConnected[i][j] is 1 or 0.
- isConnected[i][i] == 1
- isConnected[i][j] == isConnected[j][i]
"""


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        [[1, 1, 0], [1, 1, 0], [0, 0, 1]],  # Example 1: 2 provinces
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]],  # Example 2: 3 provinces
    ]
    answers = [
        2,  # Expected output for Example 1
        3,  # Expected output for Example 2
    ]

    tester = Tester(Solution().findCircleNum)
    tester.test(tests, answers)
