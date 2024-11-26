from tester import Tester

"""
Seven different symbols represent Roman numerals with the following values:

Symbol  Value
I       1
V       5
X       10
L       50
C       100
D       500
M       1000

Rules:
1. If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
2. If the value starts with 4 or 9, use the subtractive form representing one symbol subtracted from the following symbol (e.g., 4 = IV, 9 = IX). Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD), and 900 (CM).
3. Powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10.

Given an integer, convert it to a Roman numeral.

Example 1:
Input: num = 3749
Output: "MMMDCCXLIX"

Example 2:
Input: num = 58
Output: "LVIII"

Example 3:
Input: num = 1994
Output: "MCMXCIV"

Constraints:
1 <= num <= 3999
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Started @ 17:18
        Ended @ 17:31
        """
        num2char = [
            {1: "I", 4: "IV", 5: "V", 9: "IX"},
            {1: "X", 4: "XL", 5: "L", 9: "XC"},
            {1: "C", 4: "CD", 5: "D", 9: "CM"},
        ]
        num_str = list(str(num))
        n_num = len(num_str)

        result = ""
        for i in range(n_num):
            pos = (n_num - i - 1)
            current_num = int(num_str[i])
            if pos == 3:
                result += "M" * current_num
                continue

            while current_num > 0:
                if current_num in num2char[pos]:
                    result += num2char[pos][current_num]
                    current_num = 0
                elif current_num > 5:
                    result += num2char[pos][5]
                    current_num -= 5
                else:
                    result += num2char[pos][1]
                    current_num -= 1

        return result


if __name__ == "__main__":
    tests = [
        [3749],
        [58],
        [1994],
    ]
    answers = [
        "MMMDCCXLIX",
        "LVIII",
        "MCMXCIV",
    ]

    tester = Tester(Solution().intToRoman)
    tester.test(tests, answers)
