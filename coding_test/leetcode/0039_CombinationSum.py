from tester import Tester

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrace(numbers: List[int], goal: int, start: int):
            if goal == 0:
                result.append(list(numbers))
                return
            elif goal < 0:
                return

            for i in range(start, len(candidates)):
                backtrace(numbers + [candidates[i]], goal - candidates[i], i)

        backtrace([], target, 0)
        return result


if __name__ == "__main__":
    tests = [
        [[2, 3, 6, 7], 7],
        [[2, 3, 5], 8],
        [[2], 1],
    ]
    answers = [
        [[2, 2, 3], [7]],
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
        [],
    ]

    tester = Tester(Solution().combinationSum)
    tester.test(tests, answers)
