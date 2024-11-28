from tester import Tester

"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consists of only digits and English letters.
"""


class Solution:
    def longestPalindrome2(self, s: str) -> str:
        for size in range(len(s)+1, 0, -1):
            for i in range(len(s) - size + 1):
                target_s = s[i:(i+size)]
                if target_s == target_s[::-1]:
                    return target_s

        return ""

    def longestPalindrome(self, s: str) -> str:
        """
        Started @ 10:53
        Ended @ 11:35
        """
        memo = {}

        def backtrace(i: int, size: int) -> str:
            if (i, size) in memo:
                return memo[(i, size)]

            target_s = s[i:(i+size)]
            if target_s == target_s[::-1]:
                memo[(i, size)] = target_s
                return target_s

            if (i+size) < len(s):
                return backtrace(i+1, size)

            if size > 1:
                return backtrace(0, size-1)

        return backtrace(0, len(s))


if __name__ == "__main__":
    tests = [
        ["babad"],
        ["cbbd"],
        ["xaabacxcabaaxcabaax"],
        [
            "crbidxnkyieminyzchamldzjzglygkfbbyggagwdqdqamzpguppqjfrcewfduwvcmhliahovcwoupwxwhaoiiiguahuqxiqndwxqxweppcbeoasgtucyqlxnxpvtepwretywgjigjjuxsrbwucatffkrqyfkesakglyhpmtewfknevopxljgcttoqonxpdtzbccpyvttuaisrhdauyjyxgquinvqvfvzgusyxuqkyoklwslljbimbgznpvkdxmakqwwveqrpoiabmiegoyzuyoignfcgmqxvpcmldivknulqbpyxjuvyhrzcsgiusdhsogftokekbdynmksyebsnzbxjxfvwamccphzzlzuvotvubqvhmusdtwvlsnbqwqhqcigmlfoupnqcxdyflpgodnoqaqfekhcyxythaiqxzkahfnblyiznlqkbithmhhytzpcbkwicstapygjpjzvrjcombyrmhcusqtslzdyiiyvujnrxvkrwffwxtmdqqrawtvayiskcnpyociwkeopardpjeyuymipekbefbdfuybfvgzfkjtvurfkopatvusticwbtxdtfifgklpmjamiocalcocqwdivyulupammxhdbeazrrktxiyothnvbwwrsocxzxaxmoenigbhvxffddexrwsioqoyovaqvtmkwzupstkgkmvrddzolmuzjnsj"
        ],
    ]
    answers = [
        "bab",  # or "aba"
        "bb",
        "xaabacxcabaax",
        "wxqxw",
    ]

    tester = Tester(Solution().longestPalindrome2)
    tester.test(tests, answers)
