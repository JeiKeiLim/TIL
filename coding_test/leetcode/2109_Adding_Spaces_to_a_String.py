from tester import Tester

from typing import List

"""
You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added.
Each space is inserted before the character at the given index.

Return the modified string after the spaces have been added.

Example 1:
Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
Output: "Leetcode Helps Me Learn"

Example 2:
Input: s = "icodeinpython", spaces = [1,5,7,9]
Output: "i code in py thon"

Example 3:
Input: s = "spacing", spaces = [0,1,2,3,4,5,6]
Output: " s p a c i n g"

Constraints:
1 <= s.length <= 3 * 10^5
s consists only of lowercase and uppercase English letters.
1 <= spaces.length <= 3 * 10^5
0 <= spaces[i] <= s.length - 1
All the values of spaces are strictly increasing.
"""


class Solution:
    def addSpaces4(self, s: str, spaces: List[int]) -> str:
        result = [s[: spaces[0]]]
        for i, j in zip(spaces[:-1], spaces[1:]):
            result.append(s[i:j])
        result.append(s[spaces[-1]:])

        return " ".join(result)

    def addSpaces3(self, s: str, spaces: List[int]) -> str:
        result = [s[: spaces[0]]]
        for k in range(1, len(spaces)):
            i, j = spaces[k - 1], spaces[k]
            result.append(s[i:j])

        result.append(s[spaces[-1]:])
        return " ".join(result)

    def addSpaces2(self, s: str, spaces: List[int]) -> str:
        result = s[: spaces[0]]
        for k in range(1, len(spaces)):
            i, j = spaces[k - 1], spaces[k]
            split_s = s[i:j]
            result += f" {split_s}"

        result += f" {s[spaces[-1]:]}"
        return result

    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        j = 0
        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                result += " "
                j += 1
            result += s[i]

        return result


if __name__ == "__main__":
    tests = [
        ["LeetcodeHelpsMeLearn", [8, 13, 15]],
        ["icodeinpython", [1, 5, 7, 9]],
        ["spacing", [0, 1, 2, 3, 4, 5, 6]],
    ]
    answers = [
        "Leetcode Helps Me Learn",
        "i code in py thon",
        " s p a c i n g",
    ]

    tester = Tester(Solution().addSpaces3)
    tester.test(tests, answers)
