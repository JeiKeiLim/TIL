from tester import Tester

from typing import List

"""
위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

제한사항
삼각형의 높이는 1 이상 500 이하입니다.
삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.

입출력 예
triangle	result
[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	30

                7
            3       8
        8       1       0
    2       7       4       4
4       5       2       6       5

            30
        23      21
    20      13      10
7       12      10      10
"""


def solution(triangle: List[List[int]]) -> int:
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(
                triangle[row + 1][col], triangle[row + 1][col + 1]
            )
    return triangle[0][0]


if __name__ == "__main__":
    tests = [
        # Strictly extracted test cases from input examples as lists
        [[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]],
    ]
    answers = [30]

    tester = Tester(solution)
    tester.test(tests, answers)
