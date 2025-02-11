from tester import Tester

import random

"""
Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:
- Find the leftmost occurrence of the substring part and remove it from s.

Return s after removing all occurrences of part.

Example 1:

Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".

Example 2:

Input: s = "axxxxyyyyb", part = "xy"
Output: "ab"
Explanation: The following operations are done:
- s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
- s = "axyb", remove "xy" starting at index 1 so s = "ab".
Now s has no occurrences of "xy".

Constraints:
1 <= s.length <= 1000
1 <= part.length <= 1000
s and part consist of lowercase English letters.
"""


class Solution:
    def removeOccurrences3(self, s: str, part: str) -> str:
        stack = ""
        m = len(part)
        for char in s:
            stack += char

            if len(stack) < m:
                continue
            while stack[-m:] == part:
                stack = stack[:-m]
        return stack

    def removeOccurrences2(self, s: str, part: str) -> str:
        stack = []
        for char in s:
            stack.append(char)

            if "".join(stack[-len(part) :]) == part:
                for _ in range(len(part)):
                    stack.pop()

        return "".join(stack)

    def removeOccurrences(self, s: str, part: str) -> str:
        no_change = False
        while not no_change:
            no_change = True
            for i in range(len(s) - len(part) + 1):
                if s[i:].startswith(part):
                    s = s[:i] + s[i + len(part) :]
                    no_change = False
                    break
        return s


if __name__ == "__main__":
    tests = [
        ["daabcbaabcbc", "abc"],
        ["axxxxyyyyb", "xy"],
        ["gjzgbpggjzgbpgsvpwdk", "gjzgbpg"],
        [
            "".join([chr(random.randint(ord("a"), ord("z"))) for _ in range(1000)]),
            "".join([chr(random.randint(ord("a"), ord("z"))) for _ in range(100)]),
        ],
    ]
    answers = ["dab", "ab", "svpwdk", ""]

    tester = Tester(Solution().removeOccurrences3)
    tester.test(tests, answers)
