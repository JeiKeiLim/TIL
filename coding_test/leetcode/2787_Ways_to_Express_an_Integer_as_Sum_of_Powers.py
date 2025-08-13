from tester import Tester

"""
Given two positive integers n and x, return the number of ways n can be expressed as 
the sum of the x-th power of unique positive integers.

In other words, count the number of sets [n1, n2, ..., nk] where:
    n = n1^x + n2^x + ... + nk^x
Each ni must be unique and positive.

Return the result modulo 10^9 + 7.

Example 1:
Input: n = 10, x = 2
Output: 1
Explanation: 3^2 + 1^2 = 9 + 1 = 10

Example 2:
Input: n = 4, x = 1
Output: 2
Explanation:
- 4 = 4^1
- 4 = 3^1 + 1^1

Example 3:
Input: n = 7, x = 1
Output: 5

[1,0,0,0,0,0,0,0]


Constraints:
- 1 <= n <= 300
- 1 <= x <= 5
"""


class Solution:
    MOD = (10**9) + 7

    def numberOfWays3(self, n: int, x: int) -> int:
        """Foward filling DP"""
        powers = []
        for i in range(1, n + 1):
            local_power = i**x
            if local_power > n:
                break
            powers.append(local_power)

        dp = [0] * (n + 1)
        dp[0] = 1
        for p in powers:
            new_dp = dp[:]
            for s in range(n - p + 1):
                if dp[s] < 1:
                    continue
                new_dp[s + p] += dp[s]
            dp = new_dp

        return dp[-1]

    def numberOfWays2(self, n: int, x: int) -> int:
        """TLE"""
        powers = []
        for i in range(1, n + 1):
            local_power = i**x
            if local_power > n:
                break
            powers.append(local_power)

        def count_ways(m: int, pi: int) -> int:
            if m < 0:
                return 0
            if m == 0:
                return 1
            if pi >= len(powers):
                return 0

            use_p = count_ways(m - powers[pi], pi + 1)
            no_use_p = count_ways(m, pi + 1)

            return use_p + no_use_p

        return count_ways(n, 0)

    def numberOfWays(self, n: int, x: int) -> int:
        powers = []
        for i in range(1, n + 1):
            local_power = i**x
            if local_power > n:
                break
            powers.append(local_power)

        dp = [0] * (n + 1)
        dp[0] = 1

        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % self.MOD

        return dp[-1]


if __name__ == "__main__":
    tests = [
        [10, 2],
        [4, 1],
        [7, 1],
        [2, 2],
        # [300, 1],
    ]
    answers = [1, 2, 5, 0, -1]
    """
    """

    tester = Tester(Solution().numberOfWays3)
    tester.test(tests, answers)
