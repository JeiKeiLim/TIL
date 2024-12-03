from tester import Tester

"""
Given a sentence consisting of words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in the sentence.

- Return the index (1-indexed) of the first word where searchWord is a prefix.
- If searchWord is a prefix of multiple words, return the minimal index.
- If there is no such word, return -1.

Example 1:
Input: sentence = "i love eating burger", searchWord = "burg"
Output: 4

Example 2:
Input: sentence = "this problem is an easy problem", searchWord = "pro"
Output: 2

Example 3:
Input: sentence = "i am tired", searchWord = "you"
Output: -1

Constraints:
1 <= sentence.length <= 100
1 <= searchWord.length <= 10
sentence consists of lowercase English letters and spaces.
searchWord consists of lowercase English letters.
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split(" ")):
            if word.startswith(searchWord):
                return i+1

        return -1


if __name__ == "__main__":
    tests = [
        ["i love eating burger", "burg"],
        ["this problem is an easy problem", "pro"],
        ["i am tired", "you"],
    ]
    answers = [
        4,
        2,
        -1,
    ]

    tester = Tester(Solution().isPrefixOfWord)
    tester.test(tests, answers)
