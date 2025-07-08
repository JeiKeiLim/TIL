from tester import Tester
from typing import List

"""
N개의 마을로 이루어진 나라가 있습니다. 이 나라의 각 마을에는 1부터 N까지의 번호가 각각 하나씩 부여되어 있습니다. 
각 마을은 양방향으로 통행할 수 있는 도로로 연결되어 있는데, 서로 다른 마을 간에 이동할 때는 이 도로를 지나야 합니다. 
도로를 지날 때 걸리는 시간은 도로별로 다릅니다.

현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달을 하려고 합니다. 
각 마을로부터 음식 주문을 받으려고 하는데, N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 합니다.

예시)
N = 5, K = 3인 경우
1번 마을에 있는 음식점은 [1, 2, 4, 5]번 마을까지는 3 이하의 시간에 배달할 수 있습니다. 
그러나 3번 마을까지는 3시간 이내로 배달할 수 있는 경로가 없으므로 3번 마을에서는 주문을 받지 않습니다. 
따라서 음식점이 배달 주문을 받을 수 있는 마을은 4개입니다.

입력값
- 마을의 개수 N: 1 이상 50 이하
- 도로 정보 road: 길이 3인 배열 (a, b, c) 형식. 
    a, b는 마을 번호(1 ≤ a, b ≤ N, a ≠ b), c는 걸리는 시간(1 ≤ c ≤ 10,000)
    두 마을을 연결하는 도로가 여러 개일 수 있음
- 음식 배달 가능 시간 K: 1 이상 500,000 이하
- road는 중복 정보 없음
- 모든 마을은 항상 연결되어 있음

출력값
- 1번 마을에서 K시간 이하로 배달할 수 있는 마을의 개수 반환

입출력 예
N    road                                                             K   result
5    [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]                3   4
6    [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]        4   4

입출력 예 설명
입출력 예 #1: 문제 예시와 같습니다.

1: [0, 1, 0, 2, 0]
2: [1, 0, 3, 0, 2] 
3: [0, 3, 0, 0, 1] 
4: [2, 0, 0, 0, 2] 
5: [0, 2, 1, 2, 0] 

입출력 예 #2:
1번 마을에서 배달에 4시간 이하가 걸리는 마을은 [1, 2, 3, 5]입니다. 따라서 4를 반환합니다.
"""


def solution(N: int, road: List[List[int]], K: int) -> int:
    road_map = [[K + 1] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        road_map[i][i] = 0

    for si, ei, cost in road:
        min_cost = min(cost, road_map[si][ei])
        road_map[si][ei] = min_cost
        road_map[ei][si] = min_cost

    queue = [(1, i, road_map[1][i]) for i in range(2, N + 1)]
    costs = [K + 1] * (N + 1)
    costs[1] = 0
    while queue:
        si, ei, cost = queue.pop()

        if cost >= costs[ei]:
            continue

        costs[ei] = cost

        for i in range(1, N + 1):
            if i == ei:
                continue
            queue.append((ei, i, cost + road_map[ei][i]))

    return sum(costs[i] <= K for i in range(1, N + 1))


if __name__ == "__main__":
    tests = [
        [5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3],
        [
            6,
            [
                [1, 2, 1],
                [1, 3, 2],
                [2, 3, 2],
                [3, 4, 3],
                [3, 5, 2],
                [3, 5, 3],
                [5, 6, 1],
            ],
            4,
        ],
    ]
    answers = [4, 4]

    tester = Tester(solution)
    tester.test(tests, answers)
