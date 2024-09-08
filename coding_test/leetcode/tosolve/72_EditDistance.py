from tester import Tester  # Assuming you have a Tester class for running tests

"""
72. Edit Distance
Medium

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

### Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
- horse -> rorse (replace 'h' with 'r')
- rorse -> rose (remove 'r')
- rose -> ros (remove 'e')

### Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
- intention -> inention (remove 't')
- inention -> enention (replace 'i' with 'e')
- enention -> exention (replace 'n' with 'x')
- exention -> exection (replace 'n' with 'c')
- exection -> execution (insert 'u')

### Constraints:
- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        ("horse", "ros"),  # Example 1
        ("intention", "execution"),  # Example 2
    ]
    answers = [
        3,  # Expected output for Example 1
        5,  # Expected output for Example 2
    ]

    tester = Tester(Solution().minDistance)
    tester.test(tests, answers)
