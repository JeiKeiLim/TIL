from tester import Tester

from typing import List


def palindromeIndex(s: str) -> int:
    if s == s[::-1]:
        return -1

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            test_str1 = s[:left] + s[(left + 1) :]

            if test_str1 == test_str1[::-1]:
                return left
            else:
                return right

        left += 1
        right -= 1

    return -1


if __name__ == "__main__":
    tests = [
        ["aaab"],
        ["baa"],
        ["aaa"],
        ["bcbc"],
        ["abcdefkedcba"],
        ["baackwardrawkcab"],
    ]
    answers = [3, 0, -1, 0, 5, 2]
    tester = Tester(palindromeIndex)
    tester.test(tests, answers)
