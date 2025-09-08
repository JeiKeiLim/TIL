from tester import Tester

"""
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [a, b] where:
• a and b are No-Zero integers.
• a + b = n

The test cases are generated so that there is at least one valid solution. 
If there are many valid solutions, you can return any of them.

Example 1:
Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.

Example 2:
Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.

6009

Constraints:
• 2 <= n <= 10^4
"""


class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        left, right = 0, 0
        i = 1
        while "0" in str(left) or "0" in str(right):
            left, right = n-i, i
            i += 1

        return [left, right]


if __name__ == "__main__":
    tests = [
        [2],
        [11],
        [90203040]
    ]
    answers = [
        [1, 1],
        [2, 9],  # or any valid answer
        [89991929, 211111]
    ]

    tester = Tester(Solution().getNoZeroIntegers)
    tester.test(tests, answers)
