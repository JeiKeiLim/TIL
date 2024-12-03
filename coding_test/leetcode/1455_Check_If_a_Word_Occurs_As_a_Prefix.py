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
    def isPrefixOfWord2(self, sentence: str, searchWord: str) -> int:
        search_idx = 0
        word_idx = 1
        for char in sentence:
            if char == " ":
                word_idx += 1
                search_idx = 0
                continue

            if search_idx < 0:
                continue

            if char == searchWord[search_idx]:
                search_idx += 1
            else:
                search_idx = -1

            if search_idx == len(searchWord):
                return word_idx
        return -1

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split(" ")):
            if word.startswith(searchWord):
                return i + 1

        return -1


if __name__ == "__main__":
    tests = [
        ["i love eating burger", "burg"],
        ["this problem is an easy problem", "pro"],
        ["i am tired", "you"],
        ["hellohello hellohellohello", "ell"],
    ]
    answers = [
        4,
        2,
        -1,
        -1,
    ]

    tester = Tester(Solution().isPrefixOfWord2)
    tester.test(tests, answers)
