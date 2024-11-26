from tester import Tester

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows.

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

P  I  N
A LS IG
YA HR
P  I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Started @ 17:32
        Ended @ 18:24
        """
        if numRows < 2:
            return s

        n_s = len(s)
        indices = []
        i = 0
        for i in range(0, n_s, max((numRows-1) * 2, 1)):
            indices.append(i)

        for row in range(1, numRows-1):
            for i in range(row, n_s, max((numRows-1) * 2, 1)):
                indices.append(i)

                second_idx = i + (2 * (numRows-1-row))
                if second_idx < n_s:
                    indices.append(second_idx)

        for i in range(numRows-1, n_s, max((numRows-1) * 2, 1)):
            indices.append(i)

        return "".join([str(s[i]) for i in indices])


if __name__ == "__main__":
    tests = [
        ["PAYPALISHIRING", 3],
        ["PAYPALISHIRING", 4],
        ["A", 1],
        ["ABC", 1],
        ["ABC", 2]
    ]
    answers = [
        "PAHNAPLSIIGYIR",
        "PINALSIGYAHRPI",
        "A",
        "ABC",
        "ACB",
    ]

    tester = Tester(Solution().convert)
    tester.test(tests, answers)
