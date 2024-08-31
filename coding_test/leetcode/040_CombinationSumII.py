from tester import Tester

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidate_set = {}
        for candidate in candidates:
            candidate_set[candidate] = candidate_set.get(candidate, 0) + 1

        unique_candidates = list(candidate_set.keys())

        def backtrace(numbers: List[int], goal: int, start: int):
            if goal == 0:
                result.append(list(numbers))
                return
            elif goal < 0:
                return

            for i in range(start, len(unique_candidates)):
                candidate_num = unique_candidates[i]
                for j in range(candidate_set[candidate_num]):
                    backtrace(
                        numbers + [candidate_num] * (j + 1),
                        goal - (candidate_num * (j + 1)),
                        i + 1,
                    )

        backtrace([], target, 0)
        return result


if __name__ == "__main__":
    tests = [
        [[10, 1, 2, 7, 6, 1, 5], 8],
        [[2, 5, 2, 1, 2], 5],
    ]
    answers = [
        [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
        [[1, 2, 2], [5]],
    ]

    tester = Tester(Solution().combinationSum2)
    tester.test(tests, answers)
