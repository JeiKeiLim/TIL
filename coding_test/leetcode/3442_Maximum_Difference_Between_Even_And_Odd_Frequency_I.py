from tester import Tester, generate_random_string

"""
You are given a string s consisting of lowercase English letters.
Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:
- a1 has an odd frequency in the string.
- a2 has an even frequency in the string.
Return this maximum difference.

Example 1:
Input: s = "aaaaabbc"
Output: 3

Example 2:
Input: s = "abcabcab"
Output: 1

Constraints:
- 3 <= s.length <= 100
- s consists only of lowercase English letters.
- s contains at least one character with an odd frequency and one with an even frequency.
"""

from collections import Counter

class Solution:
    def maxDiff(self, s: str) -> int:
        s_map = Counter(s)
        max_odd = 0
        min_even = len(s)
        for val in s_map.values():
            if val % 2 == 0:
                min_even = min(min_even, val)
            else:
                max_odd = max(max_odd, val)

        return max_odd - min_even


if __name__ == "__main__":
    tests = [
        ["aaaaabbc"],
        ["abcabcab"],
        [generate_random_string(10000)]
    ]
    answers = [
        3,
        1,
        -1,
    ]

    tester = Tester(Solution().maxDiff)
    tester.test(tests, answers)
