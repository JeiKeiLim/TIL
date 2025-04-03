from tester import Tester
from typing import List
from collections import deque

"""
게임 맵의 상태 maps가 주어질 때,
(1,1)에서 (n,m)까지 도달하는 최단 거리를 반환합니다.
도달할 수 없으면 -1을 반환합니다.

제한사항:
- maps는 n x m 2차원 배열 (1 ≤ n, m ≤ 100)
- 0은 벽, 1은 길
- 시작점 maps[0][0], 도착점 maps[n-1][m-1]

입출력 예시:
maps = [
 [1,0,1,1,1],
 [1,0,1,0,1],
 [1,0,1,1,1],
 [1,1,1,0,1],
 [0,0,0,0,1]
]
=> return 11
"""


def solution(maps: List[List[int]]) -> int:
    n = len(maps)
    m = len(maps[0])

    queue = deque([((0, 0), 1)])
    min_dist = (n * m) + 1
    seen = set()

    while queue:
        (y, x), dist = queue.popleft()

        if (y, x) in seen:
            continue
        seen.add((y, x))

        if dist >= min_dist:
            continue

        if y == (n - 1) and x == (m - 1):
            min_dist = min(min_dist, dist)
            continue

        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            cy, cx = y + dy, x + dx
            if cy < 0 or cx < 0 or cy >= n or cx >= m:
                continue
            if maps[cy][cx] == 1:
                queue.append(((cy, cx), dist + 1))

    return min_dist if min_dist < ((n * m) + 1) else -1


if __name__ == "__main__":
    tests = [
        [
            [
                [1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 1, 0, 1],
                [0, 0, 0, 0, 1],
            ]
        ],
        [
            [
                [1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 1, 0, 0],
                [0, 0, 0, 0, 1],
            ]
        ],
        [
            [
                [1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 0, 0, 1],
                [0, 1, 1, 0, 1],
                [0, 0, 1, 1, 1],
                [0, 0, 0, 0, 1],
            ]
        ],
        [[[1, 1, 1, 1, 1]]],
    ]
    answers = [11, -1, 13, 5]

    tester = Tester(solution)
    tester.test(tests, answers)
