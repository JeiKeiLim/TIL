from tester import Tester

from typing import List

"""
메리는 여름을 맞아 무인도로 여행을 가기 위해 지도를 보고 있습니다. 지도에는 바다와 무인도들에 대한 정보가 표시돼 있습니다. 지도는 1 x 1 크기의 사각형들로 이루어진 직사각형 격자 형태이며, 격자의 각 칸에는 'X' 또는 1에서 9 사이의 자연수가 적혀있습니다. 지도의 'X'는 바다를 나타내며, 숫자는 무인도를 나타냅니다.

상, 하, 좌, 우로 연결되는 땅들은 하나의 무인도를 이룹니다. 지도의 각 칸에 적힌 숫자는 식량을 나타내며, 상, 하, 좌, 우로 연결되는 칸에 적힌 숫자를 모두 합한 값은 해당 무인도에서 최대 며칠동안 머물 수 있는지를 나타냅니다.

지도 정보 maps가 주어질 때, 각 섬에서 최대 며칠씩 머무를 수 있는지를 오름차순으로 담아 return 하세요. 섬이 없으면 -1을 반환하세요.

제한사항
- 3 ≤ maps의 길이 ≤ 100
- 3 ≤ maps[i]의 길이 ≤ 100
- maps[i]는 'X' 또는 1과 9 사이의 자연수로 이루어진 문자열입니다.
- 지도는 직사각형 형태입니다.

입출력 예
maps	result
["X591X","X1X5X","X231X", "1XXX1"]	[1, 1, 27]
["XXX","XXX","XXX"]	                [-1]
"""


def solution(maps: List[str]) -> List[int]:
    answer = []
    visited = set()
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    stack = [(i, j) for i in range(len(maps)) for j in range(len(maps[i]))]

    while stack:
        row, col = stack.pop()

        if row < 0 or col < 0 or row >= len(maps) or col >= len(maps[row]):
            continue

        if (row, col) in visited:
            continue

        if maps[row][col] != "X":
            island_stack = [(row, col)]
            food = 0
            while island_stack:
                irow, icol = island_stack.pop()
                if (
                    (irow, icol) in visited
                    or irow < 0
                    or icol < 0
                    or irow >= len(maps)
                    or icol >= len(maps[irow])
                ):
                    continue
                visited.add((irow, icol))

                if maps[irow][icol] == "X":
                    continue

                food += int(maps[irow][icol])
                for dr, dc in directions:
                    island_stack.append((irow + dr, icol + dc))
            answer.append(food)

        visited.add((row, col))

    return sorted(answer) if answer else [-1]


if __name__ == "__main__":
    tests = [
        [["X591X", "X1X5X", "X231X", "1XXX1"]],
        [["XXX", "XXX", "XXX"]],
    ]
    answers = [
        [1, 1, 27],
        [-1],
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
