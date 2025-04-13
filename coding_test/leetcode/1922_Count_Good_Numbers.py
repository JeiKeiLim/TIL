from tester import Tester

"""
A digit string is good if:
- Digits at even indices are even (0, 2, 4, 6, 8) — 5 choices
- Digits at odd indices are prime (2, 3, 5, 7) — 4 choices

Given an integer n, return the total number of good digit strings of length n modulo 10^9 + 7.

Example 1:
Input: n = 1
Output: 5

5*4, 5*4*5, 5*4*5*4

Example 2:
Input: n = 4
Output: 400

Example 3:
Input: n = 50
Output: 564908303

Constraints:
1 <= n <= 10^15
"""


class Solution:
    def countGoodNumbers3(self, n: int) -> int:
        modulo = 10**9 + 7

        n_odd = n // 2
        n_even = n_odd + n % 2

        odd_prod = 1
        odd_mul = 4
        while n_odd > 0:
            if n_odd % 2 == 1:
                odd_prod = (odd_prod * odd_mul) % modulo
            odd_mul = (odd_mul * odd_mul) % modulo
            n_odd //= 2

        even_prod = 1
        even_mul = 5
        while n_even > 0:
            if n_even % 2 == 1:
                even_prod = (even_prod * even_mul) % modulo
            even_mul = (even_mul * even_mul) % modulo
            n_even //= 2

        return (even_prod * odd_prod) % modulo

    def countGoodNumbers2(self, n: int) -> int:
        modulo = 10**9 + 7

        n_odd = n // 2
        n_even = n_odd + n % 2

        answer = 1
        for _ in range(n_odd):
            answer = (answer * 4) % modulo

        for _ in range(n_even):
            answer = (answer * 5) % modulo

        return answer

    def countGoodNumbers(self, n: int) -> int:
        modulo = 10**9 + 7
        answer = 1
        for i in range(n):
            if i % 2 == 0:
                answer *= 5
            else:
                answer *= 4
            answer = answer % modulo

        return answer


if __name__ == "__main__":
    tests = [[1], [2], [4], [50], [10**7 - 1]]
    answers = [5, 20, 400, 564908303, 731047124]

    tester = Tester(Solution().countGoodNumbers3)
    tester.test(tests, answers)
