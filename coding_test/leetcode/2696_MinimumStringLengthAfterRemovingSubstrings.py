from tester import Tester  # Assuming you have a Tester class for running tests

"""
2696. Minimum String Length After Removing Substrings
Easy

You are given a string `s` consisting only of uppercase English letters.

You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from `s`.

Return the minimum possible length of the resulting string that you can obtain.

Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.

### Example 1:
Input: s = "ABFCACDB"
Output: 2
Explanation: 
We can do the following operations:
- Remove the substring "AB", so s = "FCACDB".
- Remove the substring "CD", so s = "FCAB".
- Remove the substring "AB", so s = "FC".
So the resulting length of the string is 2.

### Example 2:
Input: s = "ACBBD"
Output: 5
Explanation: 
We cannot do any operations on the string so the length remains the same.

### Constraints:
- 1 <= s.length <= 100
- `s` consists only of uppercase English letters.
"""


class Solution:
    def minLength(self, s: str) -> int:
        replace_set = ("AB", "CD")

        idx = 0
        while idx < len(s) - 1:
            if s[idx : idx + 2] in replace_set:
                s = s[:idx] + s[idx + 2 :]
                idx = max(idx - 1, 0)
                continue
            idx += 1

        return len(s)


if __name__ == "__main__":
    # Test cases
    tests = [
        ("ABFCACDB",),  # Example 1
        ("ACBBD",),  # Example 2
    ]
    answers = [
        2,  # Expected output for Example 1
        5,  # Expected output for Example 2
    ]

    tester = Tester(Solution().minLength)
    tester.test(tests, answers)
