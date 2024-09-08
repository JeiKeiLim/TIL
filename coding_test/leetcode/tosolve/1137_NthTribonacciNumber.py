from tester import Tester  # Assuming you have a Tester class for running tests

"""
1137. N-th Tribonacci Number
Easy

The Tribonacci sequence Tn is defined as follows: 
- T0 = 0, T1 = 1, T2 = 1
- For n >= 0, Tn+3 = Tn + Tn+1 + Tn+2

Given n, return the value of Tn.

### Example 1:
Input: n = 4
Output: 4
Explanation:
T3 = 0 + 1 + 1 = 2
T4 = 1 + 1 + 2 = 4

### Example 2:
Input: n = 25
Output: 1389537

### Constraints:
- 0 <= n <= 37
- The answer is guaranteed to fit within a 32-bit integer, i.e., answer <= 2^31 - 1.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        (4),  # Example 1
        (25),  # Example 2
    ]
    answers = [
        4,  # Expected output for Example 1
        1389537,  # Expected output for Example 2
    ]

    tester = Tester(Solution().tribonacci)
    tester.test(tests, answers)
