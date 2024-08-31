from tester import Tester

from typing import List


def BracketCombinations3(num: int) -> int:
    """It's O(n^2) solution"""

    def generate_combination(num: int, current=[]) -> List[List[int]]:
        if len(current) == num:
            return [current]

        current_0 = generate_combination(num, current + [-1])
        current_1 = generate_combination(num, current + [1])

        return current_0 + current_1

    result = 0
    possible_candidates = generate_combination(num * 2)
    for candidate in possible_candidates:
        candidate_sum = 0
        for n in candidate:
            candidate_sum += n
            if candidate_sum < 0:
                break

        if candidate_sum == 0:
            result += 1
    return result


def BracketCombinations2(num: int) -> int:
    possible_candidates = []
    for i in range(2 ** (num * 2)):
        candidate = [((i & (1 << j) > 0) + 0.5) - 1 for j in range(num * 2)]
        candidate_sum = 0

        for candidate_num in candidate:
            candidate_sum += candidate_num
            if candidate_sum < 0:
                break

        if candidate_sum == 0:
            possible_candidates.append(candidate)

    return len(possible_candidates)


def BracketCombinations4(num: int) -> int:
    """O(n) solution with Catalan"""
    dp = [0] * (num + 1)
    dp[0] = 1

    for i in range(1, num + 1):
        dp[i] = 0
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]

    return dp[num]


def BracketCombinations(num: int) -> int:
    """
    O(4^n / sqrt(n))
    """

    def backtrack(open_count: int, close_count: int, path: str):
        if open_count == num and close_count == num:
            valid_combinations.append(path)
            return

        if open_count < num:
            backtrack(open_count + 1, close_count, path + "(")

        if close_count < open_count:
            backtrack(open_count, close_count + 1, path + ")")

    valid_combinations = []
    backtrack(0, 0, "")
    return len(valid_combinations)


if __name__ == "__main__":
    tests = [
        [3],
        [2],
        [8],
    ]
    answers = [5, 2, 1430]

    tester = Tester(BracketCombinations)
    tester.test(tests, answers)
