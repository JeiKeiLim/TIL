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
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        ("abcde", "ace"),  # Example 1
        ("abc", "abc"),  # Example 2
        ("abc", "def"),  # Example 3
    ]
    answers = [
        3,  # Expected output for Example 1
        3,  # Expected output for Example 2
        0,  # Expected output for Example 3
    ]

    tester = Tester(Solution().longestCommonSubsequence)
    tester.test(tests, answers)
