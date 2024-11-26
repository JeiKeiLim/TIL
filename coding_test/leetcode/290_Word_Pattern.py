from tester import Tester

"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
- Each letter in pattern maps to exactly one unique word in s.
- Each unique word in s maps to exactly one letter in pattern.
- No two letters map to the same word, and no two words map to the same letter.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Started @ 10:54
        Ended @ 11:03
        """
        s_list = s.split(" ")

        if len(s_list) != len(pattern):
            return False

        s_map = {}
        w_map = {}

        for char, word in zip(pattern, s_list):
            if not char in s_map:
                s_map[char] = word

            if not word in w_map:
                w_map[word] = char

            if w_map[word] != char:
                return False

            if s_map[char] != word:
                return False

        return True


if __name__ == "__main__":
    tests = [
        ["abba", "dog cat cat dog"],
        ["abba", "dog cat cat fish"],
        ["aaaa", "dog cat cat dog"],
        ["abba", "dog dog dog dog"],
    ]
    answers = [True, False, False, False]

    tester = Tester(Solution().wordPattern)
    tester.test(tests, answers)
