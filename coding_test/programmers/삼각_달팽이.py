from tester import Tester

from typing import List

"""
정수 n이 매개변수로 주어집니다. 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1 이상 1,000 이하입니다.

입출력 예
n	result
4	[1,2,9,3,10,8,4,5,6,7]
    1
  2  9
 3 10 8
4 5 6  7

5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]

         1
       2    12
    3   13    11
  4  14   15    10
5   6     7   8    9

6	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]

                    1
                2       15
            3       16      14
        4      17       21      13
    5      18       19     20       12
6       7       8       9       10      11


7
                        1
                    2       18
                3       19      17
            4       20      27       16
        5       21      28      26      15
    6       22      23      24     25       14
7       8       9       10      11      12      13
"""


def solution(n: int) -> List[int]:
    """
    1, 2, n*3-3, 3, n*3-2, n*3-(n-1), 4, n*3-1, n*3-0, n*2, 6, 7, 8, 9
    """
    arr = [[0] * (i + 1) for i in range(n)]
    total = sum([len(nums) for nums in arr])
    directions = [(1, 0), (0, 1), (-1, -1)]
    dir_idx = 0

    row, col = 0, 0
    offset = 0
    for i in range(1, total + 1):
        arr[row][col] = i

        next_row = row + directions[dir_idx][0]
        next_col = col + directions[dir_idx][1]

        if (
            next_row < offset
            or next_row >= len(arr) - offset
            or next_col < offset
            or next_col >= len(arr[row]) - offset
        ):
            dir_idx = (dir_idx + 1) % len(directions)

            if dir_idx == len(directions) - 1:
                offset += 1

        row += directions[dir_idx][0]
        col += directions[dir_idx][1]

    result = []
    for nums in arr:
        result.extend(nums)
    return result


if __name__ == "__main__":
    tests = [
        # Strictly extracted test cases from input examples as lists
        [4],
        [5],
        [6],
    ]
    answers = [
        [1, 2, 9, 3, 10, 8, 4, 5, 6, 7],
        [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9],
        [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11],
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
