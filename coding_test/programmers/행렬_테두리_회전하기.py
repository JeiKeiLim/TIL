from tester import Tester
from typing import List

"""
rows x columns 크기인 행렬이 있습니다. 행렬에는 1부터 rows x columns까지의 숫자가 한 줄씩 순서대로 적혀있습니다.

이 행렬에서 직사각형 모양의 범위를 여러 번 선택해, 테두리 부분에 있는 숫자들을 시계방향으로 회전시키려 합니다.

회전은 (x1, y1, x2, y2)인 정수 4개로 표현되며, 
이는 x1행 y1열부터 x2행 y2열까지의 영역에 해당하는 직사각형 테두리 숫자를 시계방향으로 회전하는 의미입니다.

중앙 영역은 회전하지 않으며, 각 회전마다 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자를 기록합니다.

입력값:
• rows: 행의 수 (2 ≤ rows ≤ 100)
• columns: 열의 수 (2 ≤ columns ≤ 100)
• queries: 회전 명령 리스트 (1 ≤ len(queries) ≤ 10,000)
    - 각 쿼리는 [x1, y1, x2, y2] 형식 (1 ≤ x1 < x2 ≤ rows, 1 ≤ y1 < y2 ≤ columns)

출력값:
• 각 회전에서 이동한 숫자들 중 가장 작은 수를 순서대로 담은 리스트 반환

입출력 예시
rows  columns  queries                                          result
6     6        [[2,2,5,4],[3,3,6,6],[5,1,6,3]]                   [8, 10, 25]
3     3        [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]         [1, 1, 5, 3]
100   97       [[1,1,100,97]]                                   [1]

설명
예시 1:
- 2,2,5,4: 2행 2열부터 5행 4열 테두리 시계방향 회전 → 가장 작은 값 8
- 3,3,6,6: → 최솟값 10
- 5,1,6,3: → 최솟값 25
"""


def solution(rows: int, columns: int, queries: List[List[int]]) -> List[int]:
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    matrix = [
        list(range(i * columns + 1, i * columns + columns + 1)) for i in range(rows)
    ]
    answer = []
    for row_s, col_s, row_e, col_e in queries:
        i, j = row_s, col_s
        indices = [(i - 1, j - 1)]
        dir_idx = 0
        dr, dc = directions[dir_idx]
        while dir_idx < len(directions):
            i += dr
            j += dc
            if i < row_s or j < col_s or i > row_e or j > col_e:
                i -= dr
                j -= dc
                dir_idx += 1
                if dir_idx >= len(directions):
                    break
                dr, dc = directions[dir_idx]
                i += dr
                j += dc
            indices.append((i - 1, j - 1))
        indices.pop()
        indices_idx = list(range(1, len(indices))) + [0]
        answer.append(min(matrix[row][col] for row, col in indices))
        swap_values = [matrix[row][col] for row, col in indices]
        for i, j in enumerate(indices_idx):
            row_j, col_j = indices[j]
            matrix[row_j][col_j] = swap_values[i]

    return answer


if __name__ == "__main__":
    tests = [
        [6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]],
        [3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]],
        [100, 97, [[1, 1, 100, 97]]],
    ]
    answers = [
        [8, 10, 25],
        [1, 1, 5, 3],
        [1],
    ]

    tester = Tester(solution, exact_match=True)
    tester.test(tests, answers)
