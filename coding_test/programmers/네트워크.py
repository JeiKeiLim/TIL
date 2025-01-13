from tester import Tester

from typing import List
from collections import deque

"""
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 주어질 때, 네트워크의 개수를 반환하세요.

제한사항
- 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
- 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
- i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
- computer[i][i]는 항상 1입니다.

입출력 예
n   computers                    result
3   [[1, 1, 0], [1, 1, 0], [0, 0, 1]]                  2

[1, 1, 0]
[1, 1, 0]
[0, 0, 1]

[1, 0, 1, 1, 0]
[0, 1, 0, 1, 0]
[1, 0, 1, 0, 0]
[1, 1, 0, 1, 0]
[0, 0, 0, 0, 1]

[4]
[]

0: [2, 3]
1: [3]
2: [0]
3: [0, 1]
4: []


3   [[1, 1, 0], [1, 1, 1], [0, 1, 1]]                  1

[1, 1, 0]
[1, 1, 1]
[0, 1, 1]
"""


def solution(n: int, computers: List[List[int]]) -> int:
    not_visited = deque(list(range(n)))
    not_visited.remove(0)
    visited = set()
    visited.add(0)

    answer = 0
    to_visit = deque()
    for i, connected in enumerate(computers[0]):
        if i == 0:
            continue
        if connected == 1:
            to_visit.append(i)

    while not_visited:
        if len(to_visit) == 0:
            answer += 1
            next_node = not_visited.popleft()
        else:
            next_node = to_visit.popleft()

        if next_node in visited:
            continue
        visited.add(next_node)
        if next_node in not_visited:
            not_visited.remove(next_node)

        for i, connected in enumerate(computers[next_node]):
            if i in visited:
                continue
            if i == next_node:
                continue

            if connected == 1 and i not in visited:
                to_visit.append(i)

    return answer + 1


if __name__ == "__main__":
    tests = [
        [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]],
        [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]],
        [
            5,
            [
                [1, 0, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [1, 0, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 1],
            ],
        ],
        [1, [[1]]],
        [2, [[1, 1], [1, 1]]],
    ]
    answers = [2, 1, 3, 1, 1]

    tester = Tester(solution)
    tester.test(tests, answers)
