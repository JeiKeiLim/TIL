from tester import Tester

from typing import List

import random

"""
어느 공원 놀이터에는 시소가 하나 설치되어 있습니다. 이 시소는 중심으로부터 2(m), 3(m), 4(m) 거리의 지점에 좌석이 하나씩 있습니다.
이 시소를 두 명이 마주 보고 탄다고 할 때, 시소가 평형인 상태에서 각각에 의해 시소에 걸리는 토크의 크기가 서로 상쇄되어 완전한 균형을 이룰 수 있다면 그 두 사람을 시소 짝꿍이라고 합니다. 즉, 탑승한 사람의 무게와 시소 축과 좌석 간의 거리의 곱이 양쪽 다 같다면 시소 짝꿍이라고 할 수 있습니다.
사람들의 몸무게 목록 weights이 주어질 때, 시소 짝꿍이 몇 쌍 존재하는지 구하여 return 하도록 solution 함수를 완성해주세요.

제한 사항
2 ≤ weights의 길이 ≤ 100,000
100 ≤ weights[i] ≤ 1,000
몸무게 단위는 N(뉴턴)으로 주어집니다.
몸무게는 모두 정수입니다.

입출력 예
weights	result
[100,180,360,100,270]	4
입출력 예 설명
{100, 100} 은 서로 같은 거리에 마주보고 앉으면 균형을 이룹니다.
{180, 360} 은 각각 4(m), 2(m) 거리에 마주보고 앉으면 균형을 이룹니다.
{180, 270} 은 각각 3(m), 2(m) 거리에 마주보고 앉으면 균형을 이룹니다.
{270, 360} 은 각각 4(m), 3(m) 거리에 마주보고 앉으면 균형을 이룹니다.
"""


def solution2(weights: List[int]) -> int:
    """
    O(n) solution
    """
    ratios = [(2, 3), (3, 4), (2, 4), (1, 1)]
    answer = 0
    weight_map = {}

    for w in weights:
        weight_map[w] = weight_map.get(w, 0) + 1

    for w in weight_map:
        if weight_map[w] > 1:
            answer += weight_map[w] * (weight_map[w] - 1) // 2

        for r1, r2 in ratios:
            common_weight = w * r2 / r1
            if common_weight in weight_map and common_weight != w:
                answer += weight_map[w] * weight_map[common_weight]

    return answer


def solution(weights: List[int]) -> int:
    """
    200, 300, 400
    360, 540, 720
    720, 1080, 1440
    200, 300, 400
    540, 810, 1080

    O(n^2) solution
    """
    weight_pairs = []
    for w in weights:
        pairs = set()
        pairs.add(w * 2)
        pairs.add(w * 3)
        pairs.add(w * 4)
        weight_pairs.append(pairs)

    answer = 0
    for i in range(len(weights) - 1):
        for j in range(i + 1, len(weights)):
            for k in range(2, 5):
                weight = weights[i] * k
                if weight in weight_pairs[j]:
                    answer += 1
                    break

    print(weights)
    return answer


if __name__ == "__main__":
    tests = [
        [[100, 180, 360, 100, 270]],
        [[279, 266, 291, 123, 249, 207, 188, 205, 133, 120, 177, 102, 114, 103, 134, 155, 258, 237, 171, 106]],
        [[228, 496, 187, 111, 473, 135, 425, 348, 324, 229, 464, 356, 129, 129, 381, 214, 292, 243, 415, 308]],
        [[16, 97, 97, 35, 11, 68, 46, 58, 77, 84, 14, 96, 33, 28, 58, 68, 92, 95, 16, 71, 38, 24, 12, 29, 86, 25, 91, 28, 27, 18, 92, 56, 17, 82, 46, 77, 80, 21, 13, 63, 65, 90, 100, 23, 80, 62, 52, 70, 46, 63, 98, 43, 88, 63, 88, 85, 93, 99, 35, 31, 67, 12, 71, 25, 50, 42, 22, 62, 98, 11, 72, 82, 23, 58, 74, 24, 30, 57, 25, 44, 82, 73, 90, 77, 31, 25, 10, 56, 60, 71, 21, 100, 34, 77, 43, 89, 37, 78, 100, 70]],
        [[random.randint(10, 100) for _ in range(10000)]],
    ]
    answers = [4, 2, 3, 147, -1]

    tester = Tester(solution2, verbose=0)
    tester.test(tests, answers)
