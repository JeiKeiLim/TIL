from tester import Tester, generate_random_2d_int_array, generate_random_string
from typing import List

"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

ababcbaca
defegde
hijhklij


Example 2:
Input: s = "eccbbbbdec"
Output: [10]

Constraints:
- 1 <= s.length <= 500
- s consists of lowercase English letters.
"""


class Solution:
    def partitionLabels2(self, s: str) -> List[int]:
        char_map = {}
        for i, char in enumerate(s):
            char_map[char] = i

        answer = []
        max_idx = char_map[s[0]]
        si = 0
        for i, char in enumerate(s):
            max_idx = max(max_idx, char_map[char])

            if i == max_idx:
                answer.append(i - si + 1)
                si = i + 1

        return answer

    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        char_map = {}
        for i, char in enumerate(s):
            char_map[char] = i

        answer = []
        max_idx = char_map[s[0]]
        for i, char in enumerate(s):
            if i > max_idx:
                answer.append(i)

            max_idx = max(max_idx, char_map[char])

        if len(answer) == 0:
            answer.append(n)
        elif answer[-1] < n:
            answer.append(n)

        final_answer = [answer[0]]
        for i in range(1, len(answer)):
            final_answer.append(answer[i] - answer[i - 1])

        return final_answer


if __name__ == "__main__":
    tests = [
        ["ababcbacadefegdehijhklij"],
        ["eccbbbbdec"],
        ["eaaaabaaec"],
        [generate_random_string(500)],
    ]
    answers = [[9, 7, 8], [10], [9, 1], [500]]

    tester = Tester(Solution().partitionLabels)
    tester.test(tests, answers)
