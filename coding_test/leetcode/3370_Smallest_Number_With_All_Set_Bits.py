from tester import Tester

"""
You are given a positive number n.

Return the smallest number x greater than or equal to n,
such that the binary representation of x contains only set bits.

Example 1:
Input: n = 5
Output: 7
Explanation: binary of 7 is "111"

Example 2:
Input: n = 10
Output: 15
Explanation: binary of 15 is "1111"

Example 3:
Input: n = 3
Output: 3
Explanation: binary of 3 is "11"

Constraints:
• 1 <= n <= 1000
"""


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        return int(bin(n)[2:].replace("0", "1"), 2)


if __name__ == "__main__":
    tests = [[5], [10], [3], [1000], [99999999999999999999]]
    answers = [7, 15, 3, 1023, -1]

    tester = Tester(Solution().minimumOneBitOperations)
    tester.test(tests, answers)
