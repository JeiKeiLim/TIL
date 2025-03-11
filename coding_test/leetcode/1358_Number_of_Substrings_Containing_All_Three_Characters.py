from tester import Tester, generate_random_string

"""
Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:
Input: s = "abcabc"
Output: 10

abc + len(abc) -> 4
bca + len(bc) -> 3
cab + len(c) -> 2
abc

abc, abca, abcab, abcabc
bca, bcab, bcabc
cab, cabc
abc

Example 2:
Input: s = "aaacb"
Output: 3

aaacb - len(aa) + acb -> 3


acb, aacb, aaacb


Example 3:
Input: s = "abc"
Output: 1

aaacbaaa
aaacb, aaacba, aaacbaa, aaacbaaa
aacb, aacba, aacbaa, aacbaaa
acb, acba, acbaa, acbaaa
cba, cbaa, cbaaa

Constraints:
1. 3 <= s.length <= 5 * 10^4
2. s only consists of a, b or c characters.
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        char_map = {"a": 0, "b": 0, "c": 0}
        n = len(s)
        answer = 0
        i = 0
        for j in range(n):
            char_map[s[j]] += 1

            while char_map["a"] > 0 and char_map["b"] > 0 and char_map["c"] > 0:
                answer += n - j
                char_map[s[i]] -= 1
                i += 1
        return answer


if __name__ == "__main__":
    tests = [
        ["abcabc"],
        ["aaacb"],
        ["abc"],
        ["aaacbaaa"],
        [generate_random_string(5 * 10**4, end_char="c")],
    ]
    answers = [10, 3, 1, 15, -1]

    tester = Tester(Solution().numberOfSubstrings)
    tester.test(tests, answers)
