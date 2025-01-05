from tester import Tester

from typing import List
import random

"""
You are given a 0-indexed array of strings words and a 2D array of integers queries.
Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri
(both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
Output: [2,3,0]
Explanation:
The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
- The answer to the query [0,2] is 2 (strings "aba" and "ece").
- The answer to the query [1,4] is 3 (strings "ece", "aa", "e").
- The answer to the query [1,1] is 0.

Example 2:
Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
Output: [3,2,1]
Explanation:
Every string satisfies the conditions, so we return [3,2,1].

Constraints:
1. 1 <= words.length <= 10^5
2. 1 <= words[i].length <= 40
3. words[i] consists only of lowercase English letters.
4. sum(words[i].length) <= 3 * 10^5
5. 1 <= queries.length <= 10^5
6. 0 <= li <= ri < words.length
"""


class Solution:
    def countVowelStringsInRanges(
        self, words: List[str], queries: List[List[int]]
    ) -> List[int]:
        word_map = [0] * (len(words) + 1)
        vowel_set = set(["a", "e", "i", "o", "u"])
        for i, word in enumerate(words):
            word_map[i + 1] = word_map[i]
            if word[0] in vowel_set and word[-1] in vowel_set:
                word_map[i + 1] += 1

        answer = [0] * len(queries)
        for i, (si, ei) in enumerate(queries):
            answer[i] = word_map[ei + 1] - word_map[si]

        return answer


if __name__ == "__main__":
    tests = [
        [["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]]],
        [["a", "e", "i"], [[0, 2], [0, 1], [2, 2]]],
        [
            [
                "".join([chr(random.randint(ord("a"), ord("z"))) for _ in range(40)])
                for _ in range(20000)
            ],
            [
                [random.randint(0, 10000), random.randint(10001, 20000 - 1)]
                for _ in range(20000)
            ],
        ],
    ]
    answers = [[2, 3, 0], [3, 2, 1], [-1]]

    tester = Tester(Solution().countVowelStringsInRanges, verbose=0)
    tester.test(tests, answers)
