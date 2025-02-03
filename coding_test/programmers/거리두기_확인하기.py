from tester import Tester
from typing import List

"""
각 대기실에서 거리두기 규칙이 지켜지고 있는지 확인하는 solution 함수를 작성하세요.

제한사항:
- places는 5x5 크기의 문자열 리스트 5개로 구성됨
- 'P'는 응시자, 'O'는 빈 테이블, 'X'는 파티션
- 맨해튼 거리 2 이하로 응시자가 앉아 있으면 거리두기 실패 (단, 파티션이 있으면 예외)

입출력 예:
places
[[
    "POOOP",
    "OXXOX",
    "OPXPX",
    "OOXOX",
    "POXXP"
],
 [
     "POOPX",
     "OXPXP",
     "PXXXO",
     "OXXXO",
     "OOOPP"
 ],
 (0, 0): 0
    (0, 1), (0, 2)
    (1, 0), (1, 1)
 (0, 3): 0
    (0, 2), (0, 4)
    (1, 2), (1, 4)
 (1, 2): 0
    (0, 1), (0, 2), (0, 3)
    (1, 0), (1, 1), (1, 3), (1, 4)
    (2, 1), (2, 2), (2, 3)
    (3, 2)
 (1, 4): 0
 (2, 0): 0

 [
     "PXOPX",
     "OXOXP",
     "OXPOX",
     "OXXOP",
     "PXPOX"
 ],
 ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
 ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
result
[1, 0, 1, 1, 1]
"""


def solution(places: List[List[str]]) -> List[int]:
    check_ds = (
        ((0, -1), (0, -2)),  # W
        ((0, 1), (0, 2)),  # E
        ((-1, 0), (-2, 0)),  # N
        ((1, 0), (2, 0)),  # S
        ((0, -1), (-1, 0), (-1, -1)),  # WN
        ((0, 1), (-1, 0), (-1, 1)),  # EN
        ((0, -1), (1, 0), (1, -1)),  # WS
        ((0, 1), (1, 0), (1, 1)),  # ES
    )

    def check_neighbor(place: List[str]) -> int:
        n = len(place)
        m = len(place[0])
        for i in range(n):
            for j in range(m):
                if place[i][j] == "P":
                    for check_dir in check_ds:
                        n_partition = 0
                        for dr, dc in check_dir:
                            row, col = i + dr, j + dc
                            if row < 0 or col < 0 or row >= n or col >= m:
                                continue
                            if place[row][col] == "X":
                                n_partition += 1
                            elif place[row][col] == "P" and n_partition < (
                                len(check_dir) - 1
                            ):
                                return 0
        return 1

    answer = [check_neighbor(place) for place in places]

    return answer


if __name__ == "__main__":
    tests = [
        [
            [
                ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
            ]
        ],
    ]
    answers = [[1, 0, 1, 1, 1]]

    tester = Tester(solution)
    tester.test(tests, answers)
