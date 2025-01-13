from tester import Tester

from typing import List
from collections import deque
from random import randint

"""
n개의 노드가 있는 그래프가 있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 개수를 구하세요.
가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

제한사항
- 노드의 개수 n은 2 이상 20,000 이하입니다.
- 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
- edge 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.

입출력 예
n   edge                                   result
6   [[3, 6], [4, 3], [3, 2], [1, 3],
     [1, 2], [2, 4], [5, 2]]                3

(1) - (2) - (5)
 |  /  |
(3) - (4)
 |
(6)

"""


def solution(n: int, edge: List[List[int]]) -> int:
    node_map = [[] for _ in range(n + 1)]
    for si, ei in edge:
        node_map[si].append(ei)
        node_map[ei].append(si)

    dists = [n for _ in range(n + 1)]
    dists[0] = 0
    dists[1] = 0

    stack = deque([(ei, 1) for ei in node_map[1]])
    while stack:
        now, dist = stack.popleft()

        if dists[now] < dist:
            continue
        dists[now] = min(dists[now], dist)

        for ei in node_map[now]:
            if dists[ei] > (dist + 1):
                dists[ei] = min(dists[ei], dist + 1)
                stack.append((ei, dist + 1))

    max_dist = max(dists)
    return sum([dist == max_dist for dist in dists])


if __name__ == "__main__":
    tests = [
        [6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]],
        [20000, [[randint(1, 20000), randint(1, 20000)] for _ in range(50000)]],
        # [20000, [[i, i+1] for i in range(1, 19999)] + [[randint(1, 20000), randint(1, 20000)] for _ in range(10000)]]
    ]
    answers = [
        3,
        -1,
        # 1
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
