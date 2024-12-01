from tester import Tester

"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
- The same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""


class Solution:
    def wordBreak2(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                s_idx = i - len(word)
                if s_idx >= 0 and dp[s_idx] and s[s_idx:i] == word:
                    dp[i] = True
                    break

        return dp[-1]

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        memo = {}

        def backtrace(target: str, idx: int) -> bool:
            if target + f"{idx}" in memo:
                return memo[target + f"{idx}"]

            idx = idx % len(wordDict)

            if target == s:
                return True

            if len(target) >= len(s):
                return False

            for i in range(len(wordDict)):
                key = target + wordDict[idx]
                result = backtrace(key, idx + i)

                memo[key + f"{idx + i}"] = result
                if result:
                    return True

            return False

        for i in range(len(wordDict)):
            if backtrace("", i):
                return True

        return False


if __name__ == "__main__":
    tests = [
        ["leetcode", ["leet", "code"]],
        ["applepenapple", ["apple", "pen"]],
        ["catsandog", ["cats", "dog", "sand", "and", "cat"]],
        ["bb", ["a", "b", "bbb", "bbbb"]],
        ["cars", ["car", "ca", "rs"]],
        ["a", ["b"]],
        ["cbca", ["bc", "ca"]],
        ["abcd", ["a", "abc", "b", "cd"]],
        [
            "bccdbacdbdacddabbaaaadababadad",
            [
              "cbc", "bcda", "adb", "ddca", "bad", "bbb", "dad",
              "dac", "ba", "aa", "bd", "abab", "bb", "dbda", "cb",
              "caccc", "d", "dd", "aadb", "cc", "b", "bcc", "bcd",
              "cd", "cbca", "bbd", "ddd", "dabb", "ab", "acd", "a",
              "bbcc", "cdcbd", "cada", "dbca", "ac", "abacd", "cba",
              "cdb", "dbac", "aada", "cdcda", "cdc", "dbc", "dbcb",
              "bdb", "ddbdd", "cadaa", "ddbc", "babb"
            ]
        ],
    ]
    answers = [True, True, False, True, True, False, False, True, True]

    tester = Tester(Solution().wordBreak2)
    tester.test(tests, answers)
