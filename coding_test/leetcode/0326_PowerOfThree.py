from tester import Tester

"""
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3^x.

Example 1:
Input: n = 27
Output: true
Explanation: 27 = 3^3

Example 2:
Input: n = 0
Output: false
Explanation: There is no x where 3^x = 0.

Example 3:
Input: n = -1
Output: false
Explanation: There is no x where 3^x = (-1).

Constraints:
-2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfThree3(self, n: int) -> bool:
        lookup_table = (1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467, 3486784401)
        return n in lookup_table


    def isPowerOfThree2(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1

    def isPowerOfThree(self, n: int) -> bool:
        """Naive"""
        if n < 1:
            return False

        power = 0
        i = 0
        while power < n:
            power = 3**i
            if power == n:
                return True
            i += 1

        return False


if __name__ == "__main__":
    tests = [[27], [0], [-1], [45], [1_162_261_467]]
    answers = [True, False, False, False, True]

    tester = Tester(Solution().isPowerOfThree2)
    tester.test(tests, answers)
