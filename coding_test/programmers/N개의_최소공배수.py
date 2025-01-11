from tester import Tester

from typing import List

import math

"""
n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 
n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하세요.

제한사항
- arr은 길이 1 이상, 15 이하인 배열입니다.
- arr의 원소는 100 이하인 자연수입니다.

입출력 예
arr          result
[2, 6, 8, 14] 168
[1, 2, 3]     6
"""


def solution(arr: List[int]) -> int:
    val = arr[0]
    for i in range(1, len(arr)):
        val = (val * arr[i]) // math.gcd(val, arr[i])

    return val


if __name__ == "__main__":
    tests = [
        [[2, 6, 8, 14]],
        [[1, 2, 3]],
        [[12, 44, 10, 8, 18, 20, 26]],
    ]
    answers = [
        168,
        6,
        51480,
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
