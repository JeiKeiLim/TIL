from tester import Tester

from typing import List

import random

"""
You are given a 0-indexed string array words.

Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
- isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2, and false otherwise.

Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.

Example 1:
Input: words = ["a","aba","ababa","aa"]
Output: 4
Explanation:
- i = 0, j = 1: "a" is a prefix and suffix of "aba"
- i = 0, j = 2: "a" is a prefix and suffix of "ababa"
- i = 0, j = 3: "a" is a prefix and suffix of "aa"
- i = 1, j = 2: "aba" is a prefix and suffix of "ababa"

Example 2:
Input: words = ["pa","papa","ma","mama"]
Output: 2
Explanation:
- i = 0, j = 1: "pa" is a prefix and suffix of "papa"
- i = 2, j = 3: "ma" is a prefix and suffix of "mama"

Example 3:
Input: words = ["abab","ab"]
Output: 0

Constraints:
1. 1 <= words.length <= 50
2. 1 <= words[i].length <= 10
3. words[i] consists only of lowercase English letters.
"""


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """O(n^2)"""
        answer = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    answer += 1
        return answer


if __name__ == "__main__":
    tests = [
        [["a", "aba", "ababa", "aa"]],
        [["pa", "papa", "ma", "mama"]],
        [["abab", "ab"]],
        [["".join([chr(random.randint(ord('a'), ord('z'))) for _ in range(random.randint(1, 100))]) for _ in range(1000)]]
    ]
    answers = [4, 2, 0, -1]

    tester = Tester(Solution().countPrefixSuffixPairs, verbose=0)
    tester.test(tests, answers)
