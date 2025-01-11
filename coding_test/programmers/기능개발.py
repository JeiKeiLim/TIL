from tester import Tester

from typing import List
import math
import random

"""
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있지만, 뒤의 기능은 앞의 기능이 배포될 때 함께 배포됩니다.

제한사항
- 작업의 개수(progresses, speeds 배열의 길이)는 100개 이하입니다.
- 작업 진도는 100 미만의 자연수입니다.
- 작업 속도는 100 이하의 자연수입니다.

입출력 예
progresses             speeds            result
[93, 30, 55]           [1, 30, 5]        [2, 1]
[95, 90, 99, 99, 80, 99] [1, 1, 1, 1, 1, 1] [1, 3, 2]

day = (100-93) / 1

"""


def solution2(progresses: List[int], speeds: List[int]) -> List[int]:
    results = []
    i = 0
    while i < len(progresses):
        remain_task = max(100 - progresses[i], 0)

        remain_day = remain_task // speeds[i]
        if (remain_task % speeds[i]) != 0:
            remain_day += 1

        n_complete = 1
        is_continue = True
        for j in range(i + 1, len(progresses)):
            progresses[j] += speeds[j] * remain_day
            if is_continue and progresses[j] >= 100:
                i += 1
                n_complete += 1
            elif is_continue and j > (i + 1):
                is_continue = False
                i -= 1
            else:
                is_continue = False
        results.append(n_complete)
        i += 1

    return results


def solution(progresses: List[int], speeds: List[int]) -> List[int]:
    day = 0

    i = 0
    results = []
    days = []
    while i < len(progresses):
        remain_task = 100 - (progresses[i] + speeds[i] * day)
        remain_day = remain_task // (speeds[i] * max(day, 1))

        if remain_task % max((speeds[i] * day), speeds[i]) != 0:
            remain_day += 1
        day += remain_day
        days.append(day)
        i += 1

    prev_day = days[0]
    n_complete = 1
    for i in range(1, len(days)):
        if prev_day == days[i]:
            n_complete += 1
        else:
            results.append(n_complete)
            n_complete = 1
        prev_day = days[i]
    results.append(n_complete)

    return results


if __name__ == "__main__":
    tests = [
        [[93, 30, 55], [1, 30, 5]],
        [[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]],
        [[71, 23, 99, 96, 24, 76], [31, 34, 10, 37, 19, 2]],
        [
            [random.randint(1, 99) for _ in range(1000)],
            [random.randint(1, 50) for _ in range(1000)],
        ],
    ]
    answers = [
        [2, 1],
        [1, 3, 2],
        [1, 3, 1, 1],
        [-1]
    ]

    tester = Tester(solution2)
    tester.test(tests, answers)
