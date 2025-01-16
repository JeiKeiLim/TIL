from tester import Tester

from typing import List

from itertools import product

"""
직사각형 모양의 동전 배열 beginning을 target으로 바꾸기 위해 필요한 최소 동전 뒤집기 횟수를 반환하세요.
목표 상태로 만들지 못하면 -1을 반환하세요.

제한사항
- 1 ≤ beginning의 길이 = target의 길이 ≤ 10
- 1 ≤ beginning[i]의 길이 = target[i]'s 길이 ≤ 10
- 각 값은 0 또는 1이며, 0은 동전 앞면, 1은 동전 뒷면을 의미합니다.

입출력 예
beginning                                               target                                                  result
[[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0],
 [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]                     [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1],
                                                       [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]                     5

[[0, 0, 0], [0, 0, 0], [0, 0, 0]]                     [[1, 0, 1], [0, 0, 0], [0, 0, 0]]                     -1

"""


def solution2(beginning: List[List[int]], target: List[List[int]]) -> int:
    n = len(beginning)
    m = len(beginning[0])

    flip_n = list(product(*([[False, True]] * n)))

    min_flip = 2**31
    for row_flip in flip_n:
        n_flip = sum(row_flip)
        board = [[beginning[i][j] for j in range(m)] for i in range(n)]

        for i, flip in enumerate(row_flip):
            if flip:
                for j in range(m):
                    board[i][j] = 1 - board[i][j]

        is_possible = True
        m_flip = 0
        for j in range(m):
            n_match = 0
            for i in range(n):
                if target[i][j] == board[i][j]:
                    n_match += 1
            if n_match == 0:
                m_flip += 1
            elif n_match != n:
                is_possible = False
                break
        if is_possible:
            n_flip += m_flip
        else:
            continue

        min_flip = min(min_flip, n_flip)

    return min_flip if min_flip < 2**31 else -1


def solution(beginning: List[List[int]], target: List[List[int]]) -> int:
    n = len(beginning)
    m = len(beginning[0])

    flip_n = list(product(*([[False, True]] * n)))
    flip_m = list(product(*([[False, True]] * m)))

    min_flip = 2**31
    for row_flip, col_flip in product(flip_n, flip_m):
        n_flip = sum(row_flip) + sum(col_flip)

        if n_flip >= min_flip:
            continue

        board = [[beginning[i][j] for j in range(m)] for i in range(n)]

        for i, flip in enumerate(row_flip):
            if flip:
                for j in range(m):
                    board[i][j] = 1 - board[i][j]

        for j, flip in enumerate(col_flip):
            if flip:
                for i in range(n):
                    board[i][j] = 1 - board[i][j]

        if board == target:
            min_flip = min(min_flip, n_flip)

    return min_flip if min_flip < 2**31 else -1


if __name__ == "__main__":
    tests = [
        [
            [
                [0, 1, 0, 0, 0],
                [1, 0, 1, 0, 1],
                [0, 1, 1, 1, 0],
                [1, 0, 1, 1, 0],
                [0, 1, 0, 1, 0],
            ],
            [
                [0, 0, 0, 1, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 1, 0, 1],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1],
            ],
        ],
        [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[1, 0, 1], [0, 0, 0], [0, 0, 0]],
        ],
        [
            [
                [0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
                [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
                [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
            ],
            [
                [0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                [0, 0, 1, 0, 1, 1, 1, 0, 1, 1],
                [0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                [0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
                [0, 0, 1, 0, 1, 1, 1, 0, 1, 1],
                [0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                [0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
            ],
        ],
    ]
    answers = [5, -1, -1]

    tester = Tester(solution2)
    tester.test(tests, answers)
