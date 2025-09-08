from tester import Tester
from typing import List

"""
n명의 사람이 일렬로 줄을 서고 있습니다. n명의 사람들에게는 각각 1번부터 n번까지 번호가 매겨져 있습니다.
n명이 사람을 줄을 서는 방법은 여러가지가 있습니다.

예를 들어 3명이 있다면 가능한 줄 서는 방법은:
• [1, 2, 3]
• [1, 3, 2]
• [2, 1, 3]
• [2, 3, 1]
• [3, 1, 2]
• [3, 2, 1]

사람의 수 n과, 자연수 k가 주어질 때, 사람을 나열하는 모든 방법을 사전 순으로 나열했을 때,
k번째 방법을 return 하는 solution 함수를 완성하세요.

제한사항
• n은 20 이하의 자연수입니다.
• k는 n! 이하의 자연수입니다.

입출력 예
n   k   result
3   5   [3, 1, 2]

입출력 예 설명
예 #1: 위에 주어진 6개의 줄 서는 방법 중, 사전 순으로 5번째인 [3, 1, 2]를 반환합니다.
"""
import math


def solution2(n: int, k: int) -> List[int]:
    k -= 1
    nums = [i for i in range(1, n + 1)]
    answer = []

    for i in range(n, 0, -1):
        m = math.factorial(i - 1)
        idx = k // m
        k %= m
        answer.append(nums.pop(idx))

    return answer


def solution(n: int, k: int) -> List[int]:
    """Naive"""
    from itertools import permutations

    lines = list(permutations(range(1, n + 1), n))
    first_one_cnt = 0
    for line in lines:
        if line[0] == 1:
            first_one_cnt += 1
    return list(lines[k])


if __name__ == "__main__":
    tests = [[3, 5], [4, 9], [9, 123456], [10, 123456], [20, 999999999991828374]]
    answers = [
        [3, 1, 2],
        [2, 3, 1, 4],
        [4, 1, 6, 5, 9, 2, 3, 7, 8],
        [1, 5, 2, 7, 6, 10, 3, 4, 8, 9],
        [9, 5, 4, 11, 17, 8, 14, 7, 18, 3, 15, 1, 16, 2, 12, 13, 6, 20, 19, 10],
    ]

    tester = Tester(solution2)
    tester.test(tests, answers)
