from tester import Tester

import sys
from typing import List, Any


def solution(letter: str) -> List[int]:
    result = [-1] * 26
    for i, l in enumerate(letter):
        if result[ord(l) - ord('a')] == -1:
            result[ord(l) - ord('a')] = i
    return result


def get_args(lines: List[str]) -> List[Any]:
    n_line_per_case = 1

    args = []
    for i in range(len(lines) // n_line_per_case):
        args.append([lines[i]])

    return args


if __name__ == "__main__":
    answers = None

    if sys.stdin.isatty():
        lines = """baekjoon""".split("\n")
        answers = [
            [1, 0, -1, -1, 2, -1, -1, -1, -1, 4, 3, -1, -1, 7, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        ]
    else:
        lines = sys.stdin.readlines()
        lines = [line.strip() for line in lines]

    args = get_args(lines)
    if answers is None:  # submit mode
        for arg in args:
            print(" ".join([str(c) for c in solution(*arg)]))
    else:  # local test mode
        tester = Tester(solution)
        tester.test(args, answers)
