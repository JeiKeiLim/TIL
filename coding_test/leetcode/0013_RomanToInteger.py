from tester import Tester


class Solution:

    def romanToInt(self, s: str) -> int:
        """Convert a roman numeral to an integer

        I -> 1
        V -> 5
        X -> 10
        L -> 50
        C -> 100
        D -> 500
        M -> 1000

        IV -> 4
        IX -> 9
        XL -> 40
        XC -> 90
        CD -> 400
        CM -> 900

        Args:
            s: Roman numeral

        Returns:
            int: Integer value of the Roman numeral
        """
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        previous_num = roman_dict[s[0]]
        result = previous_num

        for i in range(1, len(s)):
            current_num = roman_dict[s[i]]

            if previous_num < current_num:
                result -= previous_num
                result += current_num - previous_num
            else:
                result += current_num

            previous_num = current_num

        return result


if __name__ == "__main__":
    tests = [
        ["III"],
        ["IV"],
        ["IX"],
        ["LVIII"],
        ["MCMXCIV"],
    ]
    answers = [3, 4, 9, 58, 1994]

    tester = Tester(Solution().romanToInt)
    tester.test(tests, answers)
