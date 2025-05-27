from tester import Tester

"""
You are given positive integers n and m.
Define two integers as follows:
- num1: The sum of all integers in the range [1, n] that are not divisible by m.
- num2: The sum of all integers in the range [1, n] that are divisible by m.

Return the integer num1 - num2.

Example 1:
Input: n = 10, m = 3
Output: 19
Explanation: 
Integers not divisible by 3: [1,2,4,5,7,8,10] => sum = 37
Integers divisible by 3: [3,6,9] => sum = 18
Result: 37 - 18 = 19

Example 2:
Input: n = 5, m = 6
Output: 15

Example 3:
Input: n = 5, m = 1
Output: -15

Constraints:
- 1 <= n, m <= 1000
"""


class Solution:
    def differenceOfSums2(self, n: int, m: int) -> int:
        num2 = sum(i for i in range(m, n + 1, m))
        num1 = ((n * (n + 1)) // 2) - num2
        return num1 - num2

    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for i in range(1, n + 1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        return num1 - num2


if __name__ == "__main__":
    tests = [
        [10, 3],
        [5, 6],
        [5, 1],
        [1, 1],
        [1000, 1000],
    ]
    answers = [
        19,
        15,
        -15,
        -1,
        499500 - 1000,
    ]

    tester = Tester(Solution().differenceOfSums2)
    tester.test(tests, answers)
