from tester import Tester

from typing import List

import random

"""
원형 수열 elements가 주어질 때, 연속 부분 수열 합으로 만들 수 있는 서로 다른 수의 개수를 반환하세요.

제한사항
- 3 ≤ elements의 길이 ≤ 1,000
- 1 ≤ elements의 원소 ≤ 1,000

입출력 예
elements               result
[7, 9, 1, 1, 4]        18
"""


def solution(elements: List[int]) -> int:
    n = len(elements)

    result = set()
    for elem in elements:
        result.add(elem)

    for m in range(2, len(elements)):
        total = sum(elements[:m])
        result.add(total)
        for i in range(len(elements)):
            idx = (m + i) % n
            total -= elements[i]
            total += elements[idx]
            result.add(total)

    result.add(sum(elements))

    return len(result)


if __name__ == "__main__":
    tests = [[[7, 9, 1, 1, 4]], [[random.randint(1, 1000) for _ in range(1000)]]]
    answers = [18, -1]

    tester = Tester(solution)
    tester.test(tests, answers)
