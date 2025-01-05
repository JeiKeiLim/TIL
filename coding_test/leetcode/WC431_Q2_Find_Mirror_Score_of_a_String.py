from tester import Tester

import random

"""
You are given a string s.

We define the mirror of a letter in the English alphabet as its corresponding letter when the alphabet is reversed.
For example, the mirror of 'a' is 'z', and the mirror of 'y' is 'b'.

Initially, all characters in the string s are unmarked.

You start with a score of 0, and you perform the following process on the string s:
1. Iterate through the string from left to right.
2. At each index i, find the closest unmarked index j such that j < i and s[j] is the mirror of s[i].
   Then, mark both indices i and j, and add the value i - j to the total score.
3. If no such index j exists for the index i, move on to the next index without making any changes.

Return the total score at the end of the process.

Example 1:
Input: s = "aczzx"
Output: 5
Explanation:
- i = 0: No index j satisfies the conditions, skip.
- i = 1: No index j satisfies the conditions, skip.
- i = 2: The closest index j that satisfies the conditions is j = 0,
         so mark both indices 0 and 2, and add 2 - 0 = 2 to the score.
- i = 3: No index j satisfies the conditions, skip.
- i = 4: The closest index j that satisfies the conditions is j = 1,
         so mark both indices 1 and 4, and add 4 - 1 = 3 to the score.
Total score = 2 + 3 = 5.

Example 2:
Input: s = "abcdef"
Output: 0
Explanation:
For each index i, there is no index j that satisfies the conditions.

Constraints:
1. 1 <= s.length <= 10^5
2. s consists only of lowercase English letters.
"""


class Solution:
    def calculateScore3(self, s: str) -> int:
        s_map = {}
        ord_a = ord("a")
        for i in range(26):
            s_map[chr(i + ord_a)] = []

        score = 0
        for i in range(len(s)):
            target = chr(((ord_a - ord(s[i]) + 25) % 26) + ord_a)

            if len(s_map[target]) > 0:
                j = s_map[target].pop()
                score += i - j
            else:
                s_map[s[i]].append(i)
        return score

    def calculateScore2(self, s: str) -> int:
        """
        Alphabet index map
        """
        s_map = {}
        for i in range(len(s)):
            s_map[s[i]] = s_map.get(s[i], []) + [i]

        for key in s_map.keys():
            s_map[key].sort(reverse=True)

        marker = set()
        ord_a = ord("a")
        score = 0
        for i in range(len(s)):
            target = chr(((ord_a - ord(s[i]) + 25) % 26) + ord_a)
            if target not in s_map or i in marker:
                continue

            j = 0
            prev_j = 1
            left = 0
            right = len(s_map[target])
            while left < right and prev_j != j:
                prev_j = j
                j = (left + right) // 2
                if s_map[target][j] > i:
                    left = j
                else:
                    right = j

            for j in range(j, len(s_map[target])):
                k = s_map[target][j]
                if k >= i or k in marker:
                    continue
                score += i - k
                s_map[target].pop(j)
                marker.add(i)
                marker.add(k)
                break

        return score

    def calculateScore(self, s: str) -> int:
        marker = set()
        ord_a = ord("a")
        score = 0
        for i in range(len(s)):
            target = chr(((ord_a - ord(s[i]) + 25) % 26) + ord_a)
            for j in range(i - 1, -1, -1):
                if j in marker:
                    continue

                if s[j] == target:
                    marker.add(j)
                    marker.add(i)
                    score += i - j
                    break

        return score


if __name__ == "__main__":
    tests = [
        ["aczzx"],
        ["abcdef"],
        ["eockppxdqclkhjgvnw"],
        ["azapfwonwwcdagew"],
        ["zadavyayobbgqsexaabk"],
        ["grhshyssy"],
        ["zfufqbffulxhiofzle"],
        ["".join([chr(random.randint(ord("a"), ord("z"))) for _ in range(10**5)])],
    ]
    answers = [5, 0, 50, 3, 18, 3, 6, -1]

    tester = Tester(Solution().calculateScore3, verbose=0)
    tester.test(tests, answers)
