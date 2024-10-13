from tester import Tester  # Assuming you have a Tester class for running tests

"""
567. Permutation in String
Medium

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is a substring of `s2`.

### Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

### Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

### Constraints:
- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_set = {}
        for char in s1:
            s1_set[char] = s1_set.get(char, 0) + 1

        s2_set = {}
        for j in range(len(s1)):
            s2_set[s2[j]] = s2_set.get(s2[j], 0) + 1

        if s1_set == s2_set:
            return True

        for i in range(len(s1), len(s2)):
            target_idx = i - len(s1)
            target_val = s2_set[s2[target_idx]]

            if target_val == 1:
                del s2_set[s2[target_idx]]
            else:
                s2_set[s2[target_idx]] -= 1

            s2_set[s2[i]] = s2_set.get(s2[i], 0) + 1
            if s1_set == s2_set:
                return True

        return False


if __name__ == "__main__":
    # Test cases
    tests = [
        ["ab", "eidbaooo"],  # Example 1
        ["ab", "eidboaoo"],  # Example 2
    ]
    answers = [
        True,  # Expected output for Example 1
        False,  # Expected output for Example 2
    ]

    tester = Tester(Solution().checkInclusion)
    tester.test(tests, answers)
