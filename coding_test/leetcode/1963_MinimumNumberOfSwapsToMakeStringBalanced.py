from tester import Tester  # Assuming you have a Tester class for running tests

"""
1963. Minimum Number of Swaps to Make the String Balanced
Medium

You are given a 0-indexed string `s` of even length `n`. The string consists of exactly `n / 2` opening brackets `[` and `n / 2` closing brackets `]`.

A string is called balanced if and only if:
- It is the empty string, or
- It can be written as AB, where both A and B are balanced strings, or
- It can be written as [C], where C is a balanced string.

You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make `s` balanced.

### Example 1:
Input: s = "][]["
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3. The resulting string is "[[]]".

### Example 2:
Input: s = "]]][[["
Output: 2
Explanation: You can do the following to make the string balanced:
- Swap index 0 with index 4. s = "[]][][".
- Swap index 1 with index 5. s = "[[][]]".
The resulting string is "[[][]]".

### Example 3:
Input: s = "[]"
Output: 0
Explanation: The string is already balanced.

### Constraints:
- n == s.length
- 2 <= n <= 10^6
- n is even.
- s[i] is either '[' or ']'.
- The number of opening brackets '[' equals `n / 2`, and the number of closing brackets ']' equals `n / 2`.
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        n_mismatch = 0
        n_to_close = 0

        for char in s:
            if char == "[":
                n_to_close += 1
            elif char == "]":
                n_to_close -= 1

                if n_to_close < 0:
                    n_mismatch += 1
                    n_to_close = 0

        return (n_mismatch // 2) + (n_mismatch % 2)


if __name__ == "__main__":
    # Test cases
    tests = [
        ("][][",),  # Example 1
        ("]]][[[",),  # Example 2
        ("[]",),  # Example 3
    ]
    answers = [
        1,  # Expected output for Example 1
        2,  # Expected output for Example 2
        0,  # Expected output for Example 3
    ]

    tester = Tester(Solution().minSwaps)
    tester.test(tests, answers)
