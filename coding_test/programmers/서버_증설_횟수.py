from tester import Tester
from typing import List

"""
당신은 온라인 게임을 운영하고 있습니다. 같은 시간대에 게임을 이용하는 사람이 m명 늘어날 때마다 서버 1대가 추가로 필요합니다. 
어느 시간대의 이용자가 m명 미만이라면, 서버 증설이 필요하지 않습니다.
어느 시간대의 이용자가 n x m명 이상 (n + 1) x m명 미만이라면 최소 n대의 증설된 서버가 운영 중이어야 합니다. 
한 번 증설한 서버는 k시간 동안 운영하고 그 이후에는 반납합니다.

예를 들어, k = 5일 때 10시에 증설한 서버는 10 ~ 15시에만 운영됩니다.

0시에서 23시까지의 시간대별 게임 이용자의 수를 나타내는 1차원 정수 배열 players, 
서버 한 대로 감당할 수 있는 최대 이용자의 수 m, 
서버 한 대가 운영 가능한 시간을 나타내는 정수 k가 주어질 때, 
모든 게임 이용자를 감당하기 위한 최소 서버 증설 횟수를 구하세요.

제한사항
• players의 길이 = 24
    ◦ 0 ≤ players[i] ≤ 1,000
• 1 ≤ m ≤ 1,000
• 1 ≤ k ≤ 24

입출력 예
players                                                                    m   k   result
[0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5] 3   5   7
[0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0] 5   1   11
[0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]    1   1   12

[0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5] 3   5   7
[0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 2, 2, 1, 1,  1, 0, 0,  0, 0, 0, 0]
"""


def solution(players: List[int], m: int, k: int) -> int:
    n = len(players)
    answer = 0
    n_servers = [0] * n

    for i in range(n):
        need_n = players[i] // m
        if need_n < n_servers[i]:
            continue

        n_increase = need_n - n_servers[i]
        answer += n_increase

        for j in range(i, min(n, i + k)):
            if n_servers[j] >= need_n:
                continue
            n_servers[j] += n_increase

    return answer


if __name__ == "__main__":
    tests = [
        [
            [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5],
            3,
            5,
        ],
        [
            [
                0,
                0,
                0,
                10,
                0,
                12,
                0,
                15,
                0,
                1,
                0,
                1,
                0,
                0,
                0,
                5,
                0,
                0,
                11,
                0,
                8,
                0,
                0,
                0,
            ],
            5,
            1,
        ],
        [
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            1,
            1,
        ],
    ]
    answers = [7, 11, 12]

    tester = Tester(solution, verbose=1)
    tester.test(tests, answers)
