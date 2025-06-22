from tester import Tester

from typing import List

"""
A string s can be partitioned into groups of size k using the following procedure:

- The first group consists of the first k characters of the string, the second group consists of the next k characters, and so on.
- If the last group has fewer than k characters, it is completed with the fill character.

Given the string s, the size of each group k, and the character fill, return a string array denoting the composition of every group s has been divided into.

Example 1:
Input: s = "abcdefghi", k = 3, fill = "x"
Output: ["abc","def","ghi"]

Example 2:
Input: s = "abcdefghij", k = 3, fill = "x"
Output: ["abc","def","ghi","jxx"]

Constraints:
- 1 <= s.length <= 100
- s consists of lowercase English letters only
- 1 <= k <= 100
- fill is a lowercase English letter
"""


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        answer = [s[i : i + k] for i in range(0, len(s), k)]
        if len(answer[-1]) < k:
            answer[-1] += fill * (k - len(answer[-1]))
        return answer


if __name__ == "__main__":
    tests = [
        ["abcdefghi", 3, "x"],
        ["abcdefghij", 3, "x"],
    ]
    answers = [
        ["abc", "def", "ghi"],
        ["abc", "def", "ghi", "jxx"],
    ]

    tester = Tester(Solution().divideString)
    tester.test(tests, answers)
