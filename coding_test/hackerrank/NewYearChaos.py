from tester import Tester

from typing import List


def minimumBribes(q: List[int]) -> int:
    """
    1, 2, 5, 3, 7, 8, 6, 4

    5 -> 3
    7 -> 5
    8 -> 6
    6 -> 4

    1, 2, 3, 4, 5, 6, 7, 8
    1, 2, 5, 3, 4, 6, 7, 8
    1, 2, 5, 3, 7, 4, 6, 8
    1, 2, 5, 3, 7, 8, 4, 6
    1, 2, 5, 3, 7, 8, 6, 4
    """
    bribes = 0
    for i in range(len(q)):
        queue_diff = q[i] - (i + 1)

        if queue_diff > 2:
            return 0

        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    return bribes


"""
2, 1, 5, 3, 4

1, 2, 3, 4, 5
2, 1, 3, 4, 5
2, 1, 5, 4, 3
"""

if __name__ == "__main__":
    tests = [
        [[1, 2, 3, 5, 4, 6, 7, 8]],
        [[4, 1, 2, 3]],
        [[2, 1, 5, 3, 4]],
        [[2, 5, 1, 3, 4]],
        [[1, 2, 5, 3, 7, 8, 6, 4]],
        [[5, 1, 2, 3, 7, 8, 6, 4]],
    ]
    answers = [1, 0, 3, 0, 7, 0]

    tester = Tester(minimumBribes)
    tester.test(tests, answers)
