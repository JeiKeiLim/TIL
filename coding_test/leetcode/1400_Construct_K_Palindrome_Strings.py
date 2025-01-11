from tester import Tester
from tester import generate_random_string

from collections import Counter

"""
Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings, or false otherwise.

Example 1:
Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions: "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Example 2:
Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.


Example 3:
Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.


Constraints:
1. 1 <= s.length <= 10^5
2. s consists of lowercase English letters.
3. 1 <= k <= 10^5
"""


class Solution:
    def canConstruct3(self, s: str, k: int) -> bool:
        return len(s) >= k and sum([val % 2 for val in Counter(s).values()]) <= k

    def canConstruct2(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        s_map = Counter(s)
        n_odd = 0

        for value in s_map.values():
            n_odd += value % 2

        return n_odd <= k

    def canConstruct(self, s: str, k: int) -> bool:
        s_map = Counter(s)
        n_even = 0
        n_odd = 0

        for value in s_map.values():
            div = value // 2
            odd = value % 2

            n_even += div
            n_odd += odd

        if k == n_even + n_odd:
            return True
        if n_even >= k >= n_odd:
            return True
        if (n_even * 2) + n_odd >= k >= max(n_even, n_odd):
            return True

        return False


if __name__ == "__main__":
    tests = [
        ["annabelle", 2],
        ["leetcode", 3],
        ["true", 4],
        ["messi", 3],
        ["aaa", 2],
        ["ibzkwaxxaggkiwjbeysz", 15],
        [
            "udplgebqrntavzongeqzlpbvvidyxiuenerbyxzseivparkozddtxwyxqllgxzcqfrtcoqydtzprk",
            23,
        ],
        [
            "cxayrgpcctwlfupgzirmazszgfiusitvzsnngmivctprcotcuutfxdpbrdlqukhxkrmpwqqwdxxrptaftpnilfzcmknqljgbfkzuhksxzplpoozablefndimqnffrqfwgaixsovmmilicjwhppikryerkdidupvzdmoejzczkbdpfqkgpbxcrxphhnxfazovxbvaxyxhgqxcxirjsryqxtreptusvupsstylpjniezyfokbowpbgxbtsemzsvqzkbrhkvzyogkuztgfmrprz",
            5,
        ],
        [generate_random_string(10**5), 1023],
    ]
    answers = [True, False, True, True, True, True, True, False, True]

    tester = Tester(Solution().canConstruct3, verbose=0)
    tester.test(tests, answers)
