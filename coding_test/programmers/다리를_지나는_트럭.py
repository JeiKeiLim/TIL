from tester import Tester
from typing import List

from collections import deque

"""
트럭이 강을 가로지르는 일차선 다리를 정해진 순서로 건널 때, 모든 트럭이 다리를 건너는 최소 시간을 반환하는 solution 함수를 작성하세요.

제한사항:
- 1 ≤ bridge_length ≤ 10,000 (다리에 올라갈 수 있는 최대 트럭 수)
- 1 ≤ weight ≤ 10,000 (다리가 견딜 수 있는 최대 무게)
- 1 ≤ len(truck_weights) ≤ 10,000 (트럭 대수)
- 1 ≤ truck_weights[i] ≤ weight (각 트럭의 무게)

입출력 예:
bridge_length    weight    truck_weights            result
2               10        [7,4,5,6]               8
100             100       [10]                    101
100             100       [10,10,10,10,10,10,10,10,10,10] 110
"""


def solution(bridge_length: int, weight: int, truck_weights: List[int]) -> int:
    n = len(truck_weights)
    c_time = 0
    c_weight = truck_weights[0]
    queue = deque()
    queue.append((c_time, c_weight))
    i = 1

    while queue:
        t_time, t_weight = queue[0]
        if c_time - t_time >= bridge_length:
            queue.popleft()
            c_weight -= t_weight

        if i < n and (c_weight + truck_weights[i]) <= weight:
            c_weight += truck_weights[i]
            queue.append((c_time, truck_weights[i]))
            i += 1

        c_time += 1

    return c_time


if __name__ == "__main__":
    tests = [
        [2, 10, [7, 4, 5, 6]],
        [100, 100, [10]],
        [100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]],
        [2, 1, [1, 1, 1]],
        [10000, 10000, [1] * 100000],
    ]
    answers = [8, 101, 110, 4, 110000]

    tester = Tester(solution, verbose=0)
    tester.test(tests, answers)
