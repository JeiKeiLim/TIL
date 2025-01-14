from tester import Tester

from typing import List

"""
0과 1로 이루어진 2^n x 2^n 크기의 2차원 정수 배열 arr을 쿼드 트리와 같은 방식으로 압축했을 때,
최종적으로 남는 0의 개수와 1의 개수를 반환하세요.

제한사항
- arr의 행의 개수는 1 이상 1024 이하이며, 2의 거듭 제곱수 형태입니다.
- arr의 각 행의 길이는 arr의 행의 개수와 같습니다.
- arr의 각 행에 있는 모든 값은 0 또는 1 입니다.

입출력 예
arr                                         result
[[1, 1, 0, 0],
 [1, 0, 0, 0],
 [1, 0, 0, 1],
 [1, 1, 1, 1]]                              [4, 9]

[[1, 1, 1, 1, 1, 1, 1, 1],
 [0, 1, 1, 1, 1, 1, 1, 1],
 [0, 0, 0, 0, 1, 1, 1, 1],
 [0, 1, 0, 0, 1, 1, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 1, 0, 0, 1],
 [0, 0, 0, 0, 1, 1, 1, 1]]                  [10, 15]
"""


def solution(arr: List[List[int]]) -> List[int]:
    if len(arr) == 1:
        return [1 - arr[0][0], arr[0][0]]

    answer = [0, 0]
    n, m = len(arr), len(arr[0])

    stack = [(0, n, 0, m)]
    while stack:
        rs, re, cs, ce = stack.pop()
        flatten = [arr[ri][ci] for ri in range(rs, re) for ci in range(cs, ce)]
        total = sum(flatten)

        if total == 0 or total == len(flatten):
            answer[total == len(flatten)] += 1
            continue
        if len(flatten) == 1:
            answer[flatten[0]] += 1
            continue

        rh = (rs + re) // 2
        ch = (cs + ce) // 2
        stack.append((rs, rh, cs, ch))  # Top left
        stack.append((rs, rh, ch, ce))  # Top right
        stack.append((rh, re, cs, ch))  # Bottom left
        stack.append((rh, re, ch, ce))  # Bottom right

    return answer


if __name__ == "__main__":
    tests = [
        [[[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]],
        [
            [
                [1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 1, 1, 1],
                [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1],
            ]
        ],
    ]
    answers = [
        [4, 9],
        [10, 15],
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
