from tester import Tester

from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_of_chalk = sum(chalk)
        k = k - (sum_of_chalk * int(k // sum_of_chalk))
        k -= sum_of_chalk

        n_student = len(chalk)

        for i in range(n_student-1, -1, -1):
            k += chalk[i]
            if k >= 0:
                return i

        # while k >= 0:
        #     for i in range(n_student):
        #         k -= chalk[i]
        #
        #         if k < 0:
        #             return i
        return -1


if __name__ == "__main__":
    tests = [
        [[5, 1, 5], 22],
        [[3, 4, 1, 2], 25],
        [[22, 25, 39, 3, 45, 45, 12, 17, 32, 9], 835],
    ]
    answers = [0, 1, 3]

    tester = Tester(Solution().chalkReplacer)
    tester.test(tests, answers)
