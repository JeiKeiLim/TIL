from tester import Tester

from typing import List

"""
지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle, 초기 캐릭터의 위치 (characterX, characterY),
아이템의 위치 (itemX, itemY)가 주어질 때, 캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리를 반환하세요.

제한사항
- rectangle의 세로 길이는 1 이상 4 이하입니다.
- rectangle의 원소는 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 좌표 형태입니다.
- 모든 좌표값은 1 이상 50 이하인 자연수입니다.
- 서로 다른 두 직사각형의 x축 좌표, 혹은 y축 좌표가 같은 경우는 없습니다.
- characterX, characterY, itemX, itemY는 모두 1 이상 50 이하인 자연수입니다.
- 캐릭터와 아이템의 처음 위치가 같은 경우는 없습니다.

입출력 예
rectangle                                 characterX  characterY  itemX  itemY  result
[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]] 1           3           7      8      17
[[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]] 9           7           6      1      11
[[1,1,5,7]]                               1           1           4      7      9
[[2,1,7,5],[6,4,10,10]]                   3           1           7      10     15
[[2,2,5,5],[1,3,6,4],[3,1,4,6]]           1           4           6      3      10
"""


def solution2(
    rectangle: List[List[int]], characterX: int, characterY: int, itemX: int, itemY: int
) -> int:
    poly_set = set()
    # def is_inside(x: int, y: int) -> bool:
    #     states = [0, 0, 0, 0]
    #     for x, y in poly_set:

    for bl_x, bl_y, tr_x, tr_y in rectangle:
        poly_set.add((bl_x, bl_y))
        poly_set.add((bl_x, tr_y))
        poly_set.add((tr_x, bl_y))
        poly_set.add((tr_x, tr_y))

    __import__("pdb").set_trace()

    # r_map = [[0] * 12 for _ in range(12)]


def solution(
    rectangle: List[List[int]], characterX: int, characterY: int, itemX: int, itemY: int
) -> int:
    r_map = [[0] * 102 for _ in range(102)]
    for bl_x, bl_y, tr_x, tr_y in rectangle:
        for i in range(bl_x*2, tr_x*2 + 1):
            for j in range(bl_y*2, tr_y*2 + 1):
                r_map[j][i] = 1

    def is_valid(x: int, y: int) -> bool:
        if r_map[y][x] == 0:
            return False

        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if r_map[i][j] == 0:
                    return True
        return False

    direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
    dir_idx = 0
    row, col = characterY*2, characterX*2
    dr, dc = direction[dir_idx]
    while not is_valid(col + dc, row + dr):
        dir_idx = (dir_idx + 1) % len(direction)
        dr, dc = direction[dir_idx]

    row, col = characterY*2 + dr, characterX*2 + dc

    n_step = 1
    item_step = 0
    while row != characterY*2 or col != characterX*2:
        if not is_valid(col, row):
            row, col = row - dr, col - dc
            n_step -= 1

            back_dir = (-dr, -dc)
            for i in range(1, len(direction) + 1):
                dir_candidate = (dir_idx + i) % len(direction)
                ndr, ndc = direction[dir_candidate]

                if back_dir == (ndr, ndc):
                    continue

                if is_valid(col + ndc, row + ndr):
                    dr, dc = ndr, ndc
                    dir_idx = dir_candidate
                    break

        row, col = row + dr, col + dc
        n_step += 1

        if (row, col) == (itemY*2, itemX*2):
            item_step = n_step // 2

    return min(item_step, (n_step // 2) - item_step)


if __name__ == "__main__":
    tests = [
        [[[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8],
        [[[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1],
        [[[1, 1, 5, 7]], 1, 1, 4, 7],
        [[[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10],
        [[[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3],
    ]
    answers = [17, 11, 9, 15, 10]

    tester = Tester(solution)
    tester.test(tests, answers)
