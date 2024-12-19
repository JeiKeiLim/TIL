from tester import Tester

from typing import List

"""
You are given a 0-indexed string s that you must perform k replacement operations on.
The replacement operations are given as three 0-indexed parallel arrays: indices, sources, and targets, all of length k.

To complete the ith replacement operation:
1. Check if the substring sources[i] occurs at index indices[i] in the original string s.
2. If it does not occur, do nothing.
3. Otherwise, replace that substring with targets[i].

All replacement operations must occur simultaneously, meaning the replacement operations
should not affect the indexing of each other. The replacements will not overlap.

Return the resulting string after performing all replacement operations on s.

Example 1:
Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
Output: "eeebffff"
Explanation:
- "a" occurs at index 0 in s, so we replace it with "eee".
- "cd" occurs at index 2 in s, so we replace it with "ffff".

Example 2:
Input: s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
Explanation:
- "ab" occurs at index 0 in s, so we replace it with "eee".
- "ec" does not occur at index 2 in s, so we do nothing.

Constraints:
1 <= s.length <= 1000
k == indices.length == sources.length == targets.length
1 <= k <= 100
0 <= indices[i] < s.length
1 <= sources[i].length, targets[i].length <= 50
s consists of only lowercase English letters.
sources[i] and targets[i] consist of only lowercase English letters.
"""


class Solution:
    def findReplaceString(
        self, s: str, indices: List[int], sources: List[str], targets: List[str]
    ) -> str:
        replace_set = []
        for idx, source, target in zip(indices, sources, targets):
            s_idx = idx
            e_idx = s_idx + len(source)

            if source == s[s_idx:e_idx]:
                replace_set.append((s_idx, e_idx, target))

        replace_set.sort(key=lambda x: x[0], reverse=True)
        result = ""
        idx = 0
        while replace_set:
            s_idx, e_idx, target = replace_set.pop()
            while idx < s_idx:
                result += s[idx]
                idx += 1
            result += target
            idx = e_idx

        result += s[idx:]

        return result


if __name__ == "__main__":
    tests = [
        ["abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]],
        ["abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]],
        ["vmokgggqzp", [3, 5, 1], ["kg", "ggq", "mo"], ["s", "so", "bfr"]],
    ]
    answers = [
        "eeebffff",
        "eeecd",
        "vbfrssozp",
    ]

    tester = Tester(Solution().findReplaceString)
    tester.test(tests, answers)
