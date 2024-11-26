from tester import Tester  # Assuming you have a Tester class for running tests

"""
921. Minimum Add to Make Parentheses Valid
Medium

A parentheses string is valid if and only if:
- It is the empty string,
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.

Return the minimum number of moves required to make `s` valid.

### Example 1:
Input: s = "())"
Output: 1

### Example 2:
Input: s = "((("
Output: 3

### Constraints:
- 1 <= s.length <= 1000
- s[i] is either '(' or ')'.
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        ()))((
        """
        n_to_close = 0
        n_mismatch = 0

        for char in s:
            if char == '(':
                n_to_close += 1
            elif char == ')':
                n_to_close -= 1

                if n_to_close < 0:
                    n_mismatch += 1
                    n_to_close = 0

        return n_to_close + n_mismatch


if __name__ == "__main__":
    # Test cases
    tests = [
        ["())",],  # Example 1
        ["(((",],  # Example 2
        ["()",],  # Valid string
        [")(",],  # Mismatched string
        ["()))(("],
    ]
    answers = [
        1,  # Expected output for Example 1
        3,  # Expected output for Example 2
        0,  # Valid parentheses, no need to add anything
        2,  # Need to add one '(' at the beginning and one ')' at the end
        4,
    ]

    tester = Tester(Solution().minAddToMakeValid)
    tester.test(tests, answers)
