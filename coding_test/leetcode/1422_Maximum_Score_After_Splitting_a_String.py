from tester import Tester

"""
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e., left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Example 1:

Input: s = "011101"
Output: 5
Explanation:
All possible ways of splitting s into two non-empty substrings are:
- left = "0" and right = "11101", score = 1 + 4 = 5
- left = "01" and right = "1101", score = 1 + 3 = 4
- left = "011" and right = "101", score = 1 + 2 = 3
- left = "0111" and right = "01", score = 1 + 1 = 2
- left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:

Input: s = "1111"
Output: 3

Constraints:
2 <= s.length <= 500
The string s consists of characters '0' and '1' only.
"""


class Solution:
    def maxScore(self, s: str) -> int:
        n_ones = sum([1 for char in s if char == "1"])
        n_zeros = 0
        result = 0
        for char in s[:-1]:
            if char == "1":
                n_ones -= 1
            else:
                n_zeros += 1

            score = n_ones + n_zeros
            result = max(score, result)

        return result


if __name__ == "__main__":
    tests = [
        ["011101"],
        ["00111"],
        ["1111"],
        ["00"],
    ]
    answers = [5, 5, 3, 1]

    tester = Tester(Solution().maxScore)
    tester.test(tests, answers)
