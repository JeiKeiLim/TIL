from tester import Tester

from typing import List, Dict
from collections import deque

import heapq
import random

"""
지점의 개수 n, 출발지점을 나타내는 s, A의 도착지점을 나타내는 a, B의 도착지점을 나타내는 b, 지점 사이의 예상 택시요금을 나타내는 fares가 주어집니다. 이때, A, B 두 사람이 s에서 출발해서 각각의 도착 지점까지 택시를 타고 간다고 가정할 때, 최저 예상 택시요금을 계산해서 return 하세요.

제한사항
- 지점갯수 n은 3 이상 200 이하인 자연수입니다.
- 지점 s, a, b는 1 이상 n 이하인 자연수이며, 서로 다른 값입니다.
- fares는 2차원 정수 배열이며, [c, d, f] 형태로 주어집니다.
  - c, d는 서로 다른 지점 번호이며, f는 c와 d 사이의 예상 택시요금입니다.

입출력 예
n   s   a   b   fares                                                                                  result
6   4   6   2   [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66],
                [2, 3, 22], [1, 6, 25]]                                                                82
7   3   4   1   [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]                                14
6   4   5   6   [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8],
                [4, 3, 9]]                                                                             18
"""


def solution2(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    def dijkstra(start):
        dist = [float("inf")] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            current_fare, node = heapq.heappop(pq)
            if dist[node] < current_fare:
                continue
            for nxt, fare in graph[node]:
                new_cost = current_fare + fare
                if dist[nxt] > new_cost:
                    dist[nxt] = new_cost
                    heapq.heappush(pq, (new_cost, nxt))
        return dist

    dist_s = dijkstra(s)
    dist_a = dijkstra(a)
    dist_b = dijkstra(b)

    answer = float("inf")
    for i in range(1, n + 1):
        answer = min(answer, dist_s[i] + dist_a[i] + dist_b[i])

    return answer


def solution(n: int, s: int, a: int, b: int, fares: List[List[int]]) -> int:
    """
    n: 지점의 개수
    s: 출발지점
    a: A의 도착지점
    b: B의 도착지점
    fares: 지점 사이의 예상 택시요금
    """
    fare_map = {}
    for si, ei, fare in fares:
        fare_map[si] = fare_map.get(si, {})
        fare_map[ei] = fare_map.get(ei, {})

        fare_map[si].update({ei: fare})
        fare_map[ei].update({si: fare})

    def find_single_path(start: int, dests: List[int]) -> Dict[int, int]:
        stack = deque()
        for ei, fare in fare_map[start].items():
            stack.append((ei, fare, set()))

        min_values = {d: 2**31 for d in dests}
        while stack:
            si, fare, visited = stack.popleft()

            if si in visited:
                continue

            if fare > max(min_values.values()):
                continue

            visited.add(si)
            if si in min_values.keys():
                min_values[si] = min(min_values[si], fare)
                continue

            if si not in fare_map.keys():
                continue

            for ei, ei_fare in fare_map[si].items():
                stack.append((ei, fare + ei_fare, set(list(visited))))

        return min_values

    a_fares = [2**31] * n
    b_fares = [2**31] * n
    s_fares = [2**31] * n
    for i in range(n):
        if (i + 1) not in fare_map.keys():
            continue

        min_fares = find_single_path(i + 1, [a, b, s])
        a_fares[i] = min_fares[a]
        b_fares[i] = min_fares[b]
        s_fares[i] = min_fares[s]

    a_fares[a - 1] = 0
    b_fares[b - 1] = 0
    s_fares[s - 1] = 0

    min_fare = min([a_fares[i] + b_fares[i] + s_fares[i] for i in range(n)])

    return min_fare


if __name__ == "__main__":
    tests = [
        [
            6,
            4,
            6,
            2,
            [
                [4, 1, 10],
                [3, 5, 24],
                [5, 6, 2],
                [3, 1, 41],
                [5, 1, 24],
                [4, 6, 50],
                [2, 4, 66],
                [2, 3, 22],
                [1, 6, 25],
            ],
        ],
        [7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]],
        [
            6,
            4,
            5,
            6,
            [
                [2, 6, 6],
                [6, 3, 7],
                [4, 6, 7],
                [6, 5, 11],
                [2, 5, 12],
                [5, 3, 20],
                [2, 4, 8],
                [4, 3, 9],
            ],
        ],
        # [
        #     200,
        #     random.randint(1, 200),
        #     random.randint(1, 200),
        #     random.randint(1, 200),
        #     [
        #         [
        #             random.randint(1, 200),
        #             random.randint(1, 200),
        #             random.randint(1, 100000),
        #         ]
        #         for _ in range(200 * 199 // 2)
        #     ],
        # ],
    ]
    answers = [82, 14, 18, -1]

    tester = Tester(solution2)
    tester.test(tests, answers)
