from tester import Tester

"""
You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
1. Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.

Example 1:
Input: s = "abc"
Output: "abc"
Explanation:
- There is no digit in the string.

Example 2:
Input: s = "cb34"
Output: ""
Explanation:
- First, we apply the operation on s[2], and s becomes "c4".
- Then we apply the operation on s[1], and s becomes "".

Constraints:
1. 1 <= s.length <= 100
2. s consists only of lowercase English letters and digits.
3. The input is generated such that it is possible to delete all digits.
"""


class Solution:
    def clearDigits(self, s: str) -> str:
        ord_a = ord("0")
        ord_z = ord("9")
        answer = ""
        for i in range(len(s)):
            if ord_a <= ord(s[i]) <= ord_z:
                answer = answer[:-1]
            else:
                answer += s[i]
        return answer


if __name__ == "__main__":
    tests = [
        ["abc"],
        ["cb34"],
    ]
    answers = ["abc", ""]

    tester = Tester(Solution().clearDigits)
    tester.test(tests, answers)
