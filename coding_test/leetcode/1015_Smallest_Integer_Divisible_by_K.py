from tester import Tester

"""
Given a positive integer k, you need to find the length of the smallest positive integer n 
such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.

Example 1:
Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.

Example 2:
Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.

Example 3:
Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.

Constraints:
- 1 <= k <= 10^5
"""


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0:
            return -1
        num = 1
        for i in range(1, k + 1):
            if num % k == 0:
                return i
            num = ((num * 10) + 1) % k
        return -1


if __name__ == "__main__":
    tests = [[1], [2], [3], [5], [167], [15]]
    answers = [1, -1, 3, -1, 166, -1]

    tester = Tester(Solution().smallestRepunitDivByK)
    tester.test(tests, answers)
