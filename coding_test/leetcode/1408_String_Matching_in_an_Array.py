from tester import Tester

from typing import List
import random

"""
Given an array of strings words, return all strings in words that are a substring of another word. 
You can return the answer in any order.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is a substring of "mass" and "hero" is a substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substrings of "leetcode".

Example 3:
Input: words = ["blue","green","bu"]
Output: []
Explanation: No string in words is a substring of another string.

Constraints:
1. 1 <= words.length <= 100
2. 1 <= words[i].length <= 30
3. words[i] contains only lowercase English letters.
4. All the strings of words are unique.
"""


class Solution:
    def stringMatching2(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        answer = []
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                result = words[j].find(words[i])
                if result >= 0:
                    answer.append(words[i])
                    break
        return answer

    def stringMatching(self, words: List[str]) -> List[str]:
        answer = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j or len(words[j]) < len(words[i]):
                    continue
                is_substring = False
                for k in range(len(words[j]) - len(words[i]) + 1):
                    if words[j][k:].startswith(words[i]):
                        answer.append(words[i])
                        is_substring = True
                        break
                if is_substring:
                    break
        return answer


if __name__ == "__main__":
    tests = [
        [["mass", "as", "hero", "superhero"]],
        [["leetcode", "et", "code"]],
        [["blue", "green", "bu"]],
        [["leetcoder", "leetcode", "od", "hamlet", "am"]],
        [
            [
                "".join([chr(random.randint(ord("a"), ord("z"))) for _ in range(random.randint(1, 1000))])
                for _ in range(2000)
            ]
        ],
    ]
    answers = [["as", "hero"], ["et", "code"], [], ["leetcode", "od", "am"], []]

    tester = Tester(Solution().stringMatching2, verbose=0)
    tester.test(tests, answers)
