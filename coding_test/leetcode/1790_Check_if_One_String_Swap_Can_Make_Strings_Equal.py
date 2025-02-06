from tester import Tester
from collections import Counter

"""
You are given two strings s1 and s2 of equal length.
A string swap is an operation where you choose two indices in a string (not necessarily different)
and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings.
Otherwise, return false.

Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:
Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

Constraints:
1. 1 <= s1.length, s2.length <= 100
2. s1.length == s2.length
3. s1 and s2 consist of only lowercase English letters.
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if Counter(s1) != Counter(s2):
            return False

        n_diff = 0
        for i in range(n):
            if s1[i] != s2[i]:
                n_diff += 1
        return True if n_diff == 0 or n_diff == 2 else False


if __name__ == "__main__":
    tests = [
        ["bank", "kanb"],
        ["attack", "defend"],
        ["kelb", "kelb"],
        ["caa", "aaz"]
    ]
    answers = [True, False, True, False]

    tester = Tester(Solution().areAlmostEqual)
    tester.test(tests, answers)
