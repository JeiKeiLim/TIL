from tester import Tester

"""
A happy string is a string that:
1. Consists only of letters of the set ['a', 'b', 'c'].
2. s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (1-indexed).

For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings.
However, strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

Example 1:
Input: n = 1, k = 3
Output: "c"
Explanation:
- The list ["a", "b", "c"] contains all happy strings of length 1.
- The third string is "c".

Example 2:
Input: n = 1, k = 4
Output: ""
Explanation:
- There are only 3 happy strings of length 1.

Example 3:
Input: n = 3, k = 9
Output: "cab"
Explanation:
- There are 12 different happy strings of length 3:
  ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"].
- The 9th string is "cab".

Constraints:
1. 1 <= n <= 10
2. 1 <= k <= 100

"""


class Solution:
    def getHappyString2(self, n: int, k: int) -> str:
        candidates = set()
        next_chars = {"a": "bc", "b": "ac", "c": "ab"}

        def dfs(candidate: str) -> None:
            if len(candidate) == n:
                candidates.add(candidate)
                return

            for postfix in next_chars[candidate[-1]]:
                dfs(candidate + postfix)

        dfs("a")
        if len(candidates) > k:
            return sorted(candidates)[k - 1]

        dfs("b")
        if len(candidates) > k:
            return sorted(candidates)[k - 1]

        dfs("c")
        if len(candidates) < k:
            return ""

        return sorted(candidates)[k - 1]

    def getHappyString(self, n: int, k: int) -> str:
        next_chars = {"a": "bc", "b": "ac", "c": "ab"}
        queue = ["a", "b", "c"]
        candidates = set()
        while queue:
            candidate = queue.pop()
            if len(candidate) == n:
                candidates.add(candidate)
                continue
            for postfix in next_chars[candidate[-1]]:
                queue.append(candidate + postfix)

        if len(candidates) < k:
            return ""

        return sorted(candidates)[k - 1]


if __name__ == "__main__":
    tests = [
        [1, 3],
        [1, 4],
        [3, 9],
        [10, 50],
        [18, 123456],
        [18, 393216],
    ]
    answers = ["c", "", "cab", "ababcbabac", "acbcbabacabacbcbcb", "cbcbcbcbcbcbcbcbcb"]

    tester = Tester(Solution().getHappyString2)
    tester.test(tests, answers)
