from tester import Tester

"""
You are given two 0-indexed strings str1 and str2.

In an operation, you select a set of indices in str1 and increment str1[i] cyclically. That is:
- 'a' becomes 'b', 'b' becomes 'c', ..., and 'z' becomes 'a'.

Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.

Example 1:
Input: str1 = "abc", str2 = "ad"
Output: true
Explanation: Select index 2 in str1.
Increment str1[2] to become 'd'.
Hence, str1 becomes "abd" and str2 is now a subsequence. Therefore, true is returned.

Example 2:
Input: str1 = "zc", str2 = "ad"
Output: true
Increment str1[0] to become 'a'.
Increment str1[1] to become 'd'.
Hence, str1 becomes "ad" and str2 is now a subsequence. Therefore, true is returned.

Example 3:
Input: str1 = "ab", str2 = "d"
Output: false
Explanation: In this example, it can be shown that it is impossible to make str2 a subsequence of str1 using the operation at most once.
Therefore, false is returned.

Constraints:
1 <= str1.length <= 10^5
1 <= str2.length <= 10^5
str1 and str2 consist of only lowercase English letters.
"""


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """
        O(n)
        """
        len1 = len(str1)
        len2 = len(str2)

        if len2 > len1:
            return False

        idx1 = 0
        idx2 = 0

        ord_a = ord("a")

        while (len2-idx2) <= len1-idx1 and idx1 < len1 and idx2 < len2:
            char2 = str2[idx2]
            alt_char2 = chr(((ord(char2) - ord_a - 1) % 26) + ord_a)

            if char2 == str1[idx1] or alt_char2 == str1[idx1]:
                idx2 += 1
            idx1 += 1

        return idx2 == len2


if __name__ == "__main__":
    tests = [
        ["abc", "ad"],
        ["zc", "ad"],
        ["ab", "d"],
        ["eao", "ofa"],
        ["b", "c"],
        ["dzf", "fgi"],
        ["ymydm", "ydm"],
        ["xodcbhkabqp", "xdilbcp"],
        ["abc", "abcd"],
    ]
    answers = [True, True, False, False, True, False, True, True, False]

    tester = Tester(Solution().canMakeSubsequence)
    tester.test(tests, answers)
