from tester import Tester

from tester import generate_random_string

"""
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:
1. It is ().
2. It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
3. It can be written as (A), where A is a valid parentheses string.

You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's.
For each index i of locked:
- If locked[i] is '1', you cannot change s[i].
- If locked[i] is '0', you can change s[i] to either '(' or ')'.

Return true if you can make s a valid parentheses string. Otherwise, return false.

Example 1:
Input: s = "))()))", locked = "010100"
Output: true
Explanation:
- locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
- We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.


Example 2:
Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.

Example 3:
Input: s = ")", locked = "0"
Output: false
Explanation:
- locked permits us to change s[0]. Changing s[0] to either '(' or ')' will not make s valid.

Constraints:
1. n == s.length == locked.length
2. 1 <= n <= 10^5
3. s[i] is either '(' or ')'.
4. locked[i] is either '0' or '1'.
"""


class Solution:
    def canBeValid3(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False

        n_open, n_close = 0, 0
        for char, lock in zip(s, locked):
            n_open += 1 if char == "(" or lock == "0" else -1
            if n_open < 0:
                return False

        for char, lock in zip(s[::-1], locked[::-1]):
            n_close += 1 if char == ")" or lock == "0" else -1
            if n_close < 0:
                return False

        return True

    def canBeValid2(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False

        n_open, n_close = 0, 0
        for char, lock in zip(s, locked):
            if char == "(":
                n_open += 1
            else:
                n_close += 1

            if lock == "1" and char == ")":
                m = n_open + n_close
                if n_open > n_close or m % 2 == 1:
                    return False
                n_open = 0
                n_close = 0

        return (n_open + n_close) % 2 == 0

    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        cumsum = [0] * n
        cumsum[0] = 1 if s[0] == "(" else -1

        for i in range(1, len(s)):
            num = 1 if s[i] == "(" else -1
            cumsum[i] = cumsum[i - 1] + num

        prefix = 0
        for val, lock in zip(cumsum, locked):
            val += prefix
            if val < 0 and lock == "0":
                prefix += 2
            elif val > 1 and lock == "0":
                prefix -= val

        return (cumsum[-1] + prefix) == 0


if __name__ == "__main__":
    tests = [
        ["))()))", "010100"],
        ["()()", "0000"],
        [")", "0"],
        [")(", "00"],
        ["((()(()()))()((()()))))()((()(()", "10111100100101001110100010001001"],
        [
            generate_random_string(1000, 1000, "(", ")"),
            generate_random_string(1000, 1000, "0", "1"),
        ],
    ]
    answers = [
        True,
        True,
        False,
        True,
        True,
        False,
    ]

    tester = Tester(Solution().canBeValid3)
    tester.test(tests, answers)
