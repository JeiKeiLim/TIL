from tester import Tester  # Assuming you have a Tester class for running tests

"""
1143. Longest Common Subsequence
Medium

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

### Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

### Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

### Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

### Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.
"""


class Solution:
    """
    Started @ 03:55
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Code finished @ 03:59

        Time complexity: O(2^(n+m))
        """

        def trace(idx1: int, idx2: int, matched: int) -> int:
            if idx1 >= len(text1) or idx2 >= len(text2):
                return matched

            if text1[idx1] == text2[idx2]:
                matched += 1

            return max(trace(idx1, idx2 + 1, matched), trace(idx1 + 1, idx2, matched))

        return trace(0, 0, 0)

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        """
        Removing conditions
        Code finished @ 04:16
        It's making wrong answer in ["oxcpqrsvwf", "shmtulqrypy"] case
        """

        def trace(idx1: int, idx2: int, matched: int) -> int:
            if idx1 >= len(text1) or idx2 >= len(text2):
                return matched

            if text1[idx1] == text2[idx2]:
                matched += 1

                return trace(idx1 + 1, idx2 + 1, matched)

            return max(trace(idx1, idx2 + 1, matched), trace(idx1 + 1, idx2, matched))

        for idx1 in range(len(text1)):
            for idx2 in range(len(text2)):
                if text1[idx1] == text2[idx2]:
                    break
            if text1[idx1] == text2[idx2]:
                break

        return trace(idx1, idx2, 0)

    def longestCommonSubsequence3(self, text1: str, text2: str) -> int:
        """
        O(nm)
        """
        memo = {}

        def trace(idx1: int, idx2: int) -> int:
            if idx1 == len(text1) or idx2 == len(text2):
                return 0  # No more characters to compare
            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]

            if text1[idx1] == text2[idx2]:
                memo[(idx1, idx2)] = 1 + trace(idx1 + 1, idx2 + 1)
            else:
                memo[(idx1, idx2)] = max(trace(idx1 + 1, idx2), trace(idx1, idx2 + 1))
            return memo[(idx1, idx2)]

        return trace(0, 0)

    def longestCommonSubsequence4(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        # Initialize DP table with zeros
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill the DP table
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[n][m]


if __name__ == "__main__":
    # Test cases
    tests = [
        ["abcde", "ace"],  # Example 1
        ["abc", "abc"],  # Example 2
        ["abc", "def"],  # Example 3
        ["oxcpqrsvwf", "shmtulqrypy"],
        ["abcdefghijklmnopqrstuvwxyz", "dglmqxz"],  # Example 3
        ["dglmqxz", "abcdefghijklmnopqrstuvwxyz"],  # Example 3
        ["abcdefghijklmnopqrstuvwxyz", "bdglmqxz"],  # Example 3
        ["abcdefghijklmnopqrstuvwxyz", "bdgilmqxz"],  # Example 3
        ["abcdefghijklmnopqrstuvwxyz", "abcdgilmqxz"],  # Example 3
    ]
    answers = [
        3,  # Expected output for Example 1
        3,  # Expected output for Example 2
        0,  # Expected output for Example 3
        2,
        7,
        7,
        8,
        9,
        11,
    ]

    tester = Tester(Solution().longestCommonSubsequence4)
    tester.test(tests, answers)
