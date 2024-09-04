from tester import Tester


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        base_num = ord("a") - 1

        number_s: str = "".join([str(ord(char) - base_num) for char in s])
        result: int = 0

        for _ in range(k):
            result = sum([int(char) for char in str(number_s)])
            number_s = str(result)

        return result


if __name__ == "__main__":
    tests = [
        ["iiii", 1],
        ["leetcode", 2],
        ["zbax", 2],
    ]
    answers = [36, 6, 8]

    tester = Tester(Solution().getLucky)
    tester.test(tests, answers)
