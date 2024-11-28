from tester import Tester

from typing import Dict


class Solution:
    def climbStairs2(self, n: int) -> int:
        dp = [0] * (n + 2)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(2, n + 2):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]

    def _climbStairs(self, n: int, memo: Dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1

        if n not in memo:
            memo[n] = self._climbStairs(n - 1, memo) + self._climbStairs(n - 2, memo)

        return memo[n]

    def climbStairs(self, n: int) -> int:
        """Return the number of ways to climb n stairs

        You can climb 1 or 2 stairs at a time

        Args:
            n: the number of stairs

        Returns:
            int: the number of ways to climb n stairs
        """
        memo = {}
        return self._climbStairs(n, memo)


if __name__ == "__main__":
    tests = [[2], [3], [35]]
    answers = [2, 3, 14930352]

    tester = Tester(Solution().climbStairs2)
    tester.test(tests, answers)
