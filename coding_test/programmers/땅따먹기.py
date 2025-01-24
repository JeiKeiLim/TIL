from tester import Tester

from typing import List
from collections import deque
import random

"""
땅따먹기 게임을 하려고 합니다. 땅따먹기 게임의 땅(land)은 총 N행 4열로 이루어져 있고, 모든 칸에는 점수가 쓰여 있습니다. 1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 합니다. 단, 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.

예를 들면,

| 1 | 2 | 3 | 5 |
| 5 | 6 | 7 | 8 |
| 4 | 3 | 2 | 1 |

| 12 | 4 | 7  | 4 |
| 6  | 3 | 12 | 4 |



로 땅이 주어졌다면, 1행에서 네번째 칸 (5)를 밟았으면, 2행의 네번째 칸 (8)은 밟을 수 없습니다.

마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 return하는 solution 함수를 완성해 주세요.
위 예의 경우, 1행의 네번째 칸 (5), 2행의 세번째 칸 (7), 3행의 첫번째 칸 (4) 땅을 밟아 16점이 최고점이 되므로 16을 return 하면 됩니다.


제한사항
- 행의 개수 N: 100,000 이하의 자연수
- 열의 개수는 4개
- 점수: 100 이하의 자연수

입출력 예
land                     answer
[[1, 2, 3, 5],
 [5, 6, 7, 8],
 [4, 3, 2, 1]]           16
"""


def solution2(land: List[List[int]]) -> int:
    for i in range(1, len(land)):
        land[i][0] += max(land[i - 1][1], land[i - 1][2], land[i - 1][3])
        land[i][1] += max(land[i - 1][0], land[i - 1][2], land[i - 1][3])
        land[i][2] += max(land[i - 1][0], land[i - 1][1], land[i - 1][3])
        land[i][3] += max(land[i - 1][0], land[i - 1][1], land[i - 1][2])

    return max(land[-1])


def solution(land: List[List[int]]) -> int:
    """Wrong case"""
    n = len(land)
    m = len(land[0])

    prev_col = -1
    answer = 0
    for row in range(n - 1):
        max_score = -(2**63)
        max_idx = -1
        for col in range(m):
            if col == prev_col:
                continue
            next_row = land[row + 1].copy()
            next_row.pop(col)
            score = land[row][col] + max(next_row)
            if max_score < score:
                max_score = score
                max_idx = col
        answer += land[row][max_idx]
        prev_col = max_idx

    next_row = land[-1].copy()
    if n > 1:
        next_row.pop(prev_col)
    answer += max(next_row)
    return answer


if __name__ == "__main__":
    tests = [
        [[[1, 2, 3, 5]]],
        [[[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]],
        [[[2, 2, 2, 2], [2, 2, 2, 2], [4, 3, 2, 1], [5, 4, 7, 4], [5, 3, 12, 4]]],
        [[[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]],
        [[[10, 1, 1, 1], [5, 1, 1, 1]]],
        [[[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1], [5, 4, 7, 4], [5, 3, 12, 4]]],
        [[[random.randint(0, 100) for _ in range(4)] for _ in range(10000)]],
    ]
    answers = [5, 16, 24, 20, 11, 32, solution2(*tests[-1])]

    tester = Tester(solution, verbose=0)
    tester.test(tests, answers)
