from tester import Tester

from typing import List

"""
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.

Example 1:
Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

Example 2:
Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.

Constraints:
1. 1 <= words.length <= 100
2. 1 <= words[i].length, pref.length <= 100
3. words[i] and pref consist of lowercase English letters.
"""


class Solution:
    def prefixCount3(self, words: List[str], pref: str) -> int:
        answer = 0
        n = len(pref)
        for word in words:
            if word[:n] == pref:
                answer += 1
        return answer

    def prefixCount2(self, words: List[str], pref: str) -> int:
        for i in range(len(pref)):
            next_words = []
            for word in words:
                if word[i] == pref[i]:
                    next_words.append(word)
            words = next_words

        return len(words)

    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum([word.startswith(pref) for word in words])


if __name__ == "__main__":
    tests = [
        [["pay", "attention", "practice", "attend"], "at"],
        [["leetcode", "win", "loops", "success"], "code"],
    ]
    answers = [2, 0]

    tester = Tester(Solution().prefixCount3)
    tester.test(tests, answers)
