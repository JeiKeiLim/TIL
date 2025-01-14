from tester import Tester

from typing import List

"""
길이가 같은 배열 A, B에서 각각 한 개의 숫자를 뽑아 곱하고, 이 과정을 반복하여 두 수를 곱한 값을 누적할 때,
최종 누적된 값이 최소가 되도록 반환하세요.

제한사항
- 배열 A, B의 크기 : 1,000 이하의 자연수
- 배열 A, B의 원소의 크기 : 1,000 이하의 자연수

입출력 예
A          B          answer
[1, 4, 2]  [5, 4, 4]  29
[1, 2]     [3, 4]     10
"""


def solution2(A: List[int], B: List[int]) -> int:
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])


def solution(A: List[int], B: List[int]) -> int:
    A.sort()
    B.sort(reverse=True)
    result = 0
    for i in range(len(A)):
        result += A[i] * B[i]
    return result


if __name__ == "__main__":
    tests = [
        [[1, 4, 2], [5, 4, 4]],
        [[1, 2], [3, 4]],
    ]
    answers = [
        29,
        10,
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
