from tester import Tester

from typing import List

"""
Given an array of strings words representing an English Dictionary, return the longest word in words 
that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. 
If there is no answer, return the empty string.

Note:
- The word should be built from left to right with each additional character being added to the end of a previous word.

Example 1:
Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters.
"""


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words_set = set(words)
        results = []
        max_len = 0
        words.sort(key=lambda x: len(x), reverse=True)  # O(n log n)
        for i in range(len(words)):  # O(n)
            if len(words[i]) < max_len:
                break

            is_good = True
            for j in range(len(words[i])-1, 0, -1):
                if words[i][:j] not in words_set:
                    is_good = False
                    break

            if is_good:
                max_len = len(words[i])
                results.append(words[i])

        if len(results) > 0:
            return sorted(results)[0]
        else:
            return ""



if __name__ == "__main__":
    tests = [
        [["w", "wo", "wor", "worl", "world"]],
        [["a", "banana", "app", "appl", "ap", "apply", "apple"]],
        [["ts", "e", "x", "pbhj", "opto", "xhigy", "erikz", "pbh", "opt", "erikzb", "eri", "erik", "xlye", "xhig", "optoj", "optoje", "xly", "pb", "xhi", "x", "o"]],
    ]
    answers = [
        "world",
        "apple",
        "e",
    ]

    tester = Tester(Solution().longestWord2)
    tester.test(tests, answers)
