from tester import Tester

from typing import List

"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:

Input: s = "foo", t = "bar"
Output: false
Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"
Output: true

Constraints:
1 <= s.length <= 5 * 10^4
t.length == s.length
s and t consist of any valid ascii character.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for s_char, t_char in zip(s, t):
            if not t_char in s_map:
                s_map[t_char] = s_char

            if not s_char in t_map:
                t_map[s_char] = t_char

            if s_map[t_char] != s_char or t_map[s_char] != t_char:
                return False

        return True

if __name__ == "__main__":
    tests = [
        ["egg", "add"],
        ["foo", "bar"],
        ["paper", "title"],
    ]
    answers = [True, False, True]

    tester = Tester(Solution().isIsomorphic)
    tester.test(tests, answers)

