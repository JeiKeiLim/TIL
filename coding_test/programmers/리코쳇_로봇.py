from tester import Tester

from typing import List
from collections import deque

"""
보드게임판의 상태를 나타내는 문자열 배열 board가 주어졌을 때, 말이 목표 위치에 도달하는 데 필요한 최소 이동 횟수를 반환하세요.
도달할 수 없다면 -1을 반환하세요.

제한사항
- 3 ≤ board의 길이 ≤ 100
- 3 ≤ board의 원소의 길이 ≤ 100
- board의 원소는 ".", "D", "R", "G"로만 구성됩니다.
- "R"과 "G"는 한 번씩 등장합니다.

입출력 예
board                                  result
["...D..R", ".D.G...", "....D.D",
 "D....D.", "..D...."]                  7

[".D.R", "....", ".G..", "...D"]       -1
"""


def solution(board: List[str]) -> int:
    for i in range(len(board)):
        board[i] = f"D{board[i]}D"

    board.insert(0, "D" * len(board[0]))
    board.append("D" * len(board[0]))
    n, m = len(board), len(board[0])

    robot_start = None
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                robot_start = (i, j)
            if robot_start is not None:
                break
        if robot_start is not None:
            break

    if robot_start is None:
        return -1

    stack = deque([(robot_start[0], robot_start[1], 0, set())])

    n_obstacle = sum([1 if board[i][j] == "D" else 0 for i in range(n) for j in range(m)])

    min_step = n_obstacle
    possible_paths = {}
    min_path_step = {robot_start: 0}
    while stack:
        y, x, step, paths = stack.popleft()

        if (y, x) in paths or step >= min_step:
            continue

        if (y, x) not in min_path_step:
            min_path_step[(y, x)] = step
        elif step > min_path_step[(y, x)]:
            continue

        paths.add((y, x))

        min_path_step[(y, x)] = min(min_path_step[(y, x)], step)

        if board[y][x] == "G":
            min_step = min(min_step, step)
            continue

        if (y, x) in possible_paths:
            for next_y, next_x in possible_paths[(y, x)]:
                stack.append((next_y, next_x, step + 1, paths.copy()))
            continue

        possible_path = set()
        for i in range(y + 1, n):
            if board[i][x] == "D":
                possible_path.add((i - 1, x))
                break

        for i in range(y - 1, -1, -1):
            if board[i][x] == "D":
                possible_path.add((i + 1, x))
                break

        for j in range(x + 1, m):
            if board[y][j] == "D":
                possible_path.add((y, j - 1))
                break

        for j in range(x - 1, -1, -1):
            if board[y][j] == "D":
                possible_path.add((y, j + 1))
                break

        if (y, x) in possible_path:
            possible_path.remove((y, x))
        for next_y, next_x in possible_path:
            stack.append((next_y, next_x, step + 1, paths.copy()))

        possible_paths[(y, x)] = list(possible_path)

    return min_step if min_step < n_obstacle else -1


if __name__ == "__main__":
    tests = [
        [[
            "...D..R",
            ".D.G...",
            "....D.D",
            "D....D.",
            "..D...."
        ]],
        [[".D.R", "....", ".G..", "...D"]],
    ]
    tests[-1][0][2] = tests[-1][0][2][:15] + "R" + tests[-1][0][2][16:]
    tests[-1][0][32] = tests[-1][0][32][:26] + "G" + tests[-1][0][32][27:]
    answers = [
        7,
        -1,
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
