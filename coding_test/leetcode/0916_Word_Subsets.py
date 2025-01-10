from tester import Tester

from typing import List

"""
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

Example 1:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]

Constraints:
1. 1 <= words1.length, words2.length <= 10^4
2. 1 <= words1[i].length, words2[i].length <= 10
3. words1[i] and words2[i] consist only of lowercase English letters.
4. All the strings of words1 are unique.
"""


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """O(n+m)"""
        words1_map = []
        for word in words1:
            word_map = {}
            for char in word:
                word_map[char] = word_map.get(char, 0) + 1
            words1_map.append(word_map)

        words2_map = {}
        for word in words2:
            word_map = {}
            for w in word:
                word_map[w] = word_map.get(w, 0) + 1

            for key, value in word_map.items():
                words2_map[key] = max(words2_map.get(key, value), value)

        answer = []

        for i in range(len(words1_map)):
            is_good = True
            for key in words2_map.keys():
                if (
                    key not in words1_map[i]
                    or words1_map[i][key] < words2_map[key]
                ):
                    is_good = False
                    break

            if is_good:
                answer.append(words1[i])

        return answer


if __name__ == "__main__":
    tests = [
        [["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]],
        [["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]],
        [["amazon", "apple", "facebook", "google", "leetcode"], ["e", "oo"]],
        [["amazon", "apple", "facebook", "google", "leetcode"], ["lo", "eo"]],
    ]
    answers = [
        ["facebook", "google", "leetcode"],
        ["apple", "google", "leetcode"],
        ["facebook", "google"],
        ["google", "leetcode"],
    ]

    tester = Tester(Solution().wordSubsets)
    tester.test(tests, answers)
