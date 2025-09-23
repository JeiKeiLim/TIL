from tester import Tester

from typing import List

"""
Given two version strings, version1 and version2, compare them.

A version string consists of revisions separated by dots '.'. 
The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. 
If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:
• If version1 < version2, return -1.
• If version1 > version2, return 1.
• Otherwise, return 0.

Example 1:
Input: version1 = "1.2", version2 = "1.10"
Output: -1
Explanation: 2 < 10

Example 2:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: "01" and "001" represent same integer "1".

Example 3:
Input: version1 = "1.0", version2 = "1.0.0.0"
Output: 0
Explanation: Missing revisions are treated as 0.

Constraints:
• 1 <= version1.length, version2.length <= 500
• version1 and version2 only contain digits and '.'
• All the given revisions in version1 and version2 can be stored in a 32-bit integer
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_split = list(map(int, version1.split(".")))
        v2_split = list(map(int, version2.split(".")))
        max_length = max(len(v1_split), len(v2_split))
        v1_split.extend([0] * (max_length-len(v1_split)))
        v2_split.extend([0] * (max_length-len(v2_split)))

        for v1, v2 in zip(v1_split, v2_split):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0



if __name__ == "__main__":
    tests = [
        ["1.2", "1.10"],
        ["1.01", "1.001"],
        ["1.0", "1.0.0.0"],
    ]
    answers = [-1, 0, 0]

    tester = Tester(Solution().compareVersion)
    tester.test(tests, answers)
