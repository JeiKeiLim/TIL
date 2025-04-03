from tester import Tester
from typing import List

"""
게임 캐릭터가 명령어에 따라 움직이며 방문한 길의 수를 계산합니다.

- 명령어는 'U', 'D', 'L', 'R'
- 시작 위치는 (0, 0)
- 좌표 범위는 -5 ~ 5 (x, y 모두)

같은 길을 여러 번 지나가도 처음 한 번만 카운트합니다.
길은 양방향이므로 (a->b)나 (b->a)는 같은 길입니다.

예시:
dirs = "ULURRDLLU"
=> return 7

[0,p,p,p,0]
[0,p,p,p,0]
[0,0,C,0,0]
[0,0,0,0,0]
[0,0,0,0,0]

"LULLLLLLU"
[0,0,0,0,0]
[0,p,0,0,0]
[0,p,C,0,0]
[0,0,0,0,0]
[0,0,0,0,0]
"""


def solution(dirs: str) -> int:
    border = (-5, 5)
    y, x = 0, 0
    seen = set()

    py, px = 0, 0
    dir_map = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    for dir in dirs:
        dy, dx = dir_map[dir]
        y, x = y + dy, x + dx

        y = min(border[1], max(border[0], y))
        x = min(border[1], max(border[0], x))
        if y == py and x == px:
            continue
        seen.add((py, px, y, x))
        seen.add((y, x, py, px))
        py, px = y, x

    return len(seen) // 2


if __name__ == "__main__":
    tests = [
        ["ULURRDLLU"],
        ["LULLLLLLU"],
        ["LURDLURDLURD"],
        ["L"*10 + "R" * 10],
    ]
    answers = [7, 7, 4, 10]

    tester = Tester(solution)
    tester.test(tests, answers)
