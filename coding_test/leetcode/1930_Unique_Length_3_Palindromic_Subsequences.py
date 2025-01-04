from tester import Tester

"""
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted
without changing the relative order of the remaining characters.

Example 1:
Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")

Example 2:
Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".

Example 3:
Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")

Constraints:
1. 3 <= s.length <= 10^5
2. s consists of only lowercase English letters.

b: [b, c] -> bbb, bcb -> [a] -> bab
c: [b, a, b, a]
a: [a] -> aba -> []
"""


class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        s_map = {}
        palindromes = set()
        for char in s:
            for key in s_map:
                if key == char and len(s_map[key]) > 0:
                    for middle in s_map[key]:
                        palindromes.add(char + middle + char)
                    s_map[key] = [key]
                else:
                    s_map[key].append(char)

            if char not in s_map:
                s_map[char] = []

        return len(palindromes)


if __name__ == "__main__":
    tests = [
        ["aabca"],
        ["adc"],
        ["bbcbaba"],
        ["ckafnafqo"],
        ["tlpjzdmtwderpkpmgoyrcxttiheassztncqvnfjeyxxp"],
    ]
    answers = [3, 0, 4, 4, 161]

    tester = Tester(Solution().countPalindromicSubsequences)
    tester.test(tests, answers)
