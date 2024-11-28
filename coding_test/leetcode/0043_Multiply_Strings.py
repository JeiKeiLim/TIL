from tester import Tester

"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note:
- You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Started @ 08:26
        Ended @ 08:36
        """
        num_map = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0,
        }
        str_map = {
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            0: "0",
        }
        n_num1 = len(num1)
        n_num2 = len(num2)

        num1_int = 0
        num2_int = 0

        for i in range(n_num1):
            num1_int += num_map[num1[i]] * 10 ** (n_num1 - i - 1)

        for i in range(n_num2):
            num2_int += num_map[num2[i]] * 10 ** (n_num2 - i - 1)

        result_int = num1_int * num2_int

        if result_int < 10:
            return str_map[result_int]

        result = ""
        i = 0
        while result_int > 0:
            last_digit = result_int % 10
            result = str_map[last_digit] + result
            result_int = result_int // 10

        return result


if __name__ == "__main__":
    tests = [
        ["2", "3"],
        ["123", "456"],
    ]
    answers = [
        "6",
        "56088",
    ]

    tester = Tester(Solution().multiply)
    tester.test(tests, answers)
