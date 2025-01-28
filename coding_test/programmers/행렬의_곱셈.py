from tester import Tester
from typing import List

"""
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수를 작성하세요.

제한 조건
- 행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
- 행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
- 곱할 수 있는 배열만 주어집니다.

입출력 예
arr1	                        arr2	                                    return
[[1, 4], [3, 2], [4, 1]]	    [[3, 3], [3, 3]]	                        [[15, 15], [15, 15], [15, 15]]

[1, 4]  [3, 3, 4, 5]
[3, 2]  [3, 3, 4, 5]
[4, 1]

[[2, 3, 2], [4, 2, 4], [3, 1, 4]]	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	    [[22, 22, 11], [36, 28, 18], [29, 20, 14]]

[2, 3, 2]  [5, 4, 3]
[4, 2, 4]  [2, 4, 1]
[3, 1, 4]  [3, 1, 1]

2*5+3*2+2*3 2*4+3*4+2*1 2*3+3*1+2*1
"""


def solution(arr1: List[List[int]], arr2: List[List[int]]) -> List[List[int]]:
    n1 = len(arr1)
    m1 = len(arr1[0])
    n2 = len(arr2)
    m2 = len(arr2[0])

    answer = [[0] * m2 for _ in range(n1)]

    for row in range(n1):
        arr1_row = arr1[row]
        for col in range(m2):
            arr2_col = [arr2[i][col] for i in range(n2)]
            answer[row][col] = sum(arr1_row[i] * arr2_col[i] for i in range(m1))

    return answer


if __name__ == "__main__":
    tests = [
        [[[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]],
        [[[1, 4], [3, 2], [4, 1]], [[3, 3, 4, 5], [3, 3, 4, 5]]],
        [[[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]],
    ]
    answers = [
        [[15, 15], [15, 15], [15, 15]],
        [[15, 15, 20, 25]] * 3,
        [[22, 22, 11], [36, 28, 18], [29, 20, 14]],
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
