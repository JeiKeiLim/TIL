from tester import Tester

from typing import List

"""
Given three strings a, b, and c, your task is to find a string that has the minimum length and contains all three strings as substrings.
If there are multiple such strings, return the lexicographically smallest one.

Notes:
- A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ,
  string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
- A substring is a contiguous sequence of characters within a string.

Example 1:
Input: a = "abc", b = "bca", c = "aaa"
Output: "aaabca"
Explanation:
- "aaabca" contains all the given strings:
  a = ans[2...4], b = ans[3..5], c = ans[0..2].
- The length of the resulting string would be at least 6, and "aaabca" is the lexicographically smallest one.

Example 2:
Input: a = "ab", b = "ba", c = "aba"
Output: "aba"
Explanation:
- "aba" contains all the given strings:
  a = ans[0..1], b = ans[1..2], c = ans[0..2].
- The length of the resulting string would be at least 3, and "aba" is the lexicographically smallest one.

Constraints:
1. 1 <= a.length, b.length, c.length <= 100
2. a, b, c consist only of lowercase English letters
"""


class Solution:
    def shortestStringContainingThree(self, a: str, b: str, c: str) -> str:
        def merge(aa: str, bb: str) -> List[str]:
            if aa == bb:
                return [aa]

            len_a, len_b = len(aa), len(bb)
            if len_a > len_b:
                aa, bb = bb, aa
                len_a, len_b = len_b, len_a

            result = set()
            for k in range(len_a + len_b - 1):
                si1 = max(0, k - len_b + 1)
                ei1 = min(len_a, k + 1)

                si2 = max(0, len_b - k - 1)
                ei2 = min(len_b, len_a + len_b - k - 1)

                ww1 = aa[si1:ei1]
                ww2 = bb[si2:ei2]

                if ww1 == "" or ww2 == "":
                    continue

                if ww1 == ww2:
                    if k < len_b:
                        matched_str = bb + aa[ei1:]
                    else:
                        matched_str = aa + bb[ei2:]
                    result.add(matched_str)
            return list(result)

        a, b, c = sorted([a, b, c], reverse=True, key=lambda x: len(x))

        merge_ab = merge(a, b)
        merge_ac = merge(a, c)
        merge_bc = merge(b, c)
        stack = []
        for merged in merge_ab:
            stack.append((merged, c))
        for merged in merge_ac:
            stack.append((merged, b))
        for merged in merge_bc:
            stack.append((merged, a))

        if len(stack) == 0:
            return "".join(sorted([a, b, c]))

        results = [
            sorted(["".join(sorted(s)) for s in stack], key=lambda x: (len(x), x))[0],
        ]
        while stack:
            aa, bb = stack.pop()
            results.extend(merge(aa, bb))

        candidate = ["".join(sorted([a, b, c]))]
        min_length = len(candidate[0])
        for word in results:
            if len(word) < min_length:
                candidate = [word]
                min_length = len(word)
            elif len(word) == min_length:
                candidate.append(word)

        return sorted(candidate)[0]


if __name__ == "__main__":
    tests = [
        ["abc", "bca", "aaa"],
        ["ab", "ba", "aba"],
        ["xyyyz", "xzyz", "zzz"],
        ["a", "b", "c"],
        ["bb", "bb", "a"],
        ["a", "aac", "aa"],
        ["a", "c", "b"],
        ["b", "a", "ba"],
        ["cc", "bb", "ba"],
        ["aba", "ab", "c"],
        ["fqzhiqv", "vbrpmfpmvook", "sfharqqoqbjsfulmijqvyrgfragjjssqzlwdsvqvdmugw"],
    ]
    answers = [
        "aaabca",
        "aba",
        "xyyyzxzyzzz",
        "abc",
        "abb",
        "aac",
        "abc",
        "ba",
        "bbacc",
        "abac",
        "fqzhiqvbrpmfpmvooksfharqqoqbjsfulmijqvyrgfragjjssqzlwdsvqvdmugw",
    ]

    tester = Tester(Solution().shortestStringContainingThree)
    tester.test(tests, answers)
