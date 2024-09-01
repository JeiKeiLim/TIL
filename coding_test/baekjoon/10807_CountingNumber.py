from tester import Tester

import sys
from typing import List, Any


def solution(nums: List[int], target: int) -> int:
    count = 0

    for num in nums:
        if num == target:
            count += 1

    return count


def get_args(lines: List[str]) -> List[Any]:
    n_line_per_case = 3

    args = []
    for i in range(len(lines) // n_line_per_case):
        n_nums = int(lines[i * n_line_per_case])
        nums = list(map(int, lines[i * n_line_per_case + 1].split()))
        target = int(lines[i * n_line_per_case + 2])

        args.append([nums, target])

    return args


if __name__ == "__main__":
    answers = None

    if sys.stdin.isatty():
        lines = """11
1 4 1 2 4 2 4 2 3 4 4
2
11
1 4 1 2 4 2 4 2 3 4 4
5""".split("\n")
        answers = [3, 0]
    else:
        lines = sys.stdin.readlines()
        lines = [line.strip() for line in lines]

    args = get_args(lines)
    if answers is None:  # submit mode
        for arg in args:
            print(solution(*arg))
    else:  # local test mode
        tester = Tester(solution)
        tester.test(args, answers)
