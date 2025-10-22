from tester import Tester
from typing import List

"""
문제 설명
1과 0으로 채워진 표(board)가 있습니다. 표의 각 칸은 1x1의 정사각형으로 이루어져 있으며, 
1로 이루어진 가장 큰 정사각형을 찾아 그 넓이를 반환해야 합니다. 
(정사각형은 축에 평행해야 합니다.)

예시:
입력 board
[[0,1,1,1],
 [1,1,1,1],
 [1,1,1,1],
 [0,0,1,0]]
가장 큰 정사각형은 3x3 → 넓이 9

제한사항
• board는 2차원 배열
• 행 크기 ≤ 1,000
• 열 크기 ≤ 1,000
• 값은 0 또는 1

입출력 예
board                                         answer
[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]      9
[[0,0,1,1],[1,1,1,1]]                          4

설명
예 #1: 위와 같은 3x3 정사각형이 있음 → 넓이 9
예 #2: 가장 큰 정사각형은 2x2 → 넓이 4


[[0,1,1,1],
 [1,1,2,2],
 [1,2,2,1],
 [0,0,1,0]]


 [0,0,0,0,0,0]
 [0,1,1,1,0,0]
 [0,1,1,0,0,0]
 [0,1,1,1,0,0]
 [0,0,0,0,0,0]
"""


def solution(board: List[List[int]]) -> int:
    n = len(board)
    m = len(board[0])
    answer = max(max(board[i]) for i in range(n))

    for i in range(1, n):
        for j in range(1, m):
            min_val = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1])
            if min_val > 0 and board[i][j] > 0:
                board[i][j] = min_val + 1
            answer = max(answer, board[i][j])
    return answer * answer


if __name__ == "__main__":
    tests = [
        [[[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]],
        [[[0, 0, 1, 1], [1, 1, 1, 1]]],
        [[[0, 0], [1, 0]]],
    ]
    answers = [9, 4, 1]

    tester = Tester(solution)
    tester.test(tests, answers)
