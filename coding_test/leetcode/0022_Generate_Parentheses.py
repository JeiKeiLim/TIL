from tester import Tester

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrace(current, open: int, close: int):
            if open == n and close == n:
                result.append(current)
                return

            if open < n:
                backtrace(current + "(", open + 1, close)
            if close < open:
                backtrace(current + ")", open, close + 1)

        backtrace("", 0, 0)
        return result


if __name__ == "__main__":
    tests = [
        [3],
        [1],
    ]
    answers = [
        ["((()))", "(()())", "(())()", "()(())", "()()()"],
        ["()"],
    ]

    tester = Tester(Solution().generateParenthesis)
    tester.test(tests, answers)
