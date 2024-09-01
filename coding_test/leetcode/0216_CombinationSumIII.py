from tester import Tester

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        Constrain:
            Only numbers 1 through 9 are used.
            Each number is used at most once

        Args:
            k: number to use to make sum.
            n: target sum number.

        Return:
            All possible unique combinations with k number that sums to n
        """
        max_number = min(n - k + 1, 9)
        if max_number <= 0:
            return []

        result = []

        def backtrace(indices: List[int]):
            combination = [idx + 1 for idx in indices]

            if sum(combination) == n:
                result.append(combination)

            for i in range(k - 1, -1, -1):
                new_idx = indices[i] + 1

                if max_number <= new_idx or new_idx < i:
                    continue

                new_right_end_idx = new_idx + k - i
                if new_right_end_idx > max_number:
                    continue

                new_right_indices = list(range(new_idx + 1, new_right_end_idx))

                new_indices = indices[:i] + [new_idx] + new_right_indices
                backtrace(new_indices)
                break

        backtrace(list(range(k)))
        return result


class Solution2:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, combination: List[int], target: int):
            if len(combination) == k and target == 0:
                result.append(list(combination))
                return

            if len(combination) >= k or target < 0:
                return

            for i in range(start, 10):
                combination.append(i)
                backtrack(i + 1, combination, target - i)
                combination.pop()

        backtrack(1, [], n)
        return result


if __name__ == "__main__":
    tests = [
        [3, 7],
        [3, 9],
        [4, 1],
        [2, 6],
        [4, 24],
    ]
    answers = [
        [[1, 2, 4]],
        [[1, 2, 6], [1, 3, 5], [2, 3, 4]],
        [],
        [[1, 5], [2, 4]],
        [
            [1, 6, 8, 9],
            [2, 5, 8, 9],
            [2, 6, 7, 9],
            [3, 4, 8, 9],
            [3, 5, 7, 9],
            [3, 6, 7, 8],
            [4, 5, 6, 9],
            [4, 5, 7, 8],
        ],
    ]

    tester = Tester(Solution3().combinationSum3)
    tester.test(tests, answers)
