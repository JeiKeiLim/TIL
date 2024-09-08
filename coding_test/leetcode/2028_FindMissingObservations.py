from tester import Tester

from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """
        m + n rolls but n observations are missing.
        O(n)
        """
        total_sum = mean * (len(rolls) + n)
        sum_of_observation = sum(rolls)
        sum_of_missing = total_sum - sum_of_observation

        starting_num = sum_of_missing // n

        if starting_num > 6 or starting_num <= 0:
            return []

        sum_of_missing -= (starting_num * n)

        if starting_num == 6 and sum_of_missing > 0:
            return []

        dices = [starting_num] * n
        idx = 0
        while sum_of_missing > 0:
            bump_up = min(6 - dices[idx], sum_of_missing)
            dices[idx] += bump_up
            sum_of_missing -= bump_up
            idx += 1

        return dices


class Solution2:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """
        m + n rolls but n observations are missing.
        This solution exeeds time limits

        O(6^n)
        """
        total_sum = mean * (len(rolls) + n)
        sum_of_observation = sum(rolls)
        sum_of_missing = total_sum - sum_of_observation

        starting_num = sum_of_missing // n

        if starting_num > 6 or starting_num <= 0:
            return []

        result: List[List[int]] = list()

        def backtrace(target: int, dices: List[int]):
            if len(result) > 0:
                return
            if target == 0:
                result.append(dices)
                return
            elif target < 0:
                return

            for idx in range(len(dices)):
                if dices[idx] == 6:
                    continue

                new_dices = [dice for dice in dices]
                new_dices[idx] += 1
                backtrace(target - 1, new_dices)

        backtrace(sum_of_missing - (starting_num * n), [starting_num] * n)
        if len(result) > 0:
            return result[0]
        else:
            return []



if __name__ == "__main__":
    tests = [
        [[3, 2, 4, 3], 4, 2],
        [[1, 5, 6], 3, 4],
        [[1, 2, 3, 4], 6, 4],
        [[3, 5, 3], 5, 3],
        [[6, 3, 4, 3, 5, 3], 1, 6],
        [[4, 5, 6, 2, 3, 6, 5, 4, 6, 4, 5, 1, 6, 3, 1, 4, 5, 5, 3, 2, 3, 5, 3, 2, 1, 5, 4, 3, 5, 1, 5], 4, 40],
    ]
    answers = [
        [6, 6],
        [2, 3, 2, 2],
        [],
        [],
        [],
        [6, 6, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    ]

    tester = Tester(Solution().missingRolls)
    tester.test(tests, answers)
