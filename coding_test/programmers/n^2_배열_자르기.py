from tester import Tester
from typing import List

"""
정수 n, left, right가 주어집니다. 다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.
1. n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
2. i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
   - 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
3. 1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
4. 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.

정수 n, left, right가 매개변수로 주어집니다. 주어진 과정대로 만들어진 1차원 배열을 return 하도록 solution 함수를 완성해주세요.

제한사항
- 1 ≤ n ≤ 10^7
- 0 ≤ left ≤ right < n^2
- right - left < 10^5

입출력 예
n   left   right   result
3   2      5       [3,2,2,3]
4   7      14      [4,3,3,3,4,4,4,4]

3, 2, 5

[1, 2, 3]
[2, 2, 3]
[3, 3, 3]

[1,2,3,4,5]
[2,2,3,4,5]
[3,3,3,4,5]
[4,4,4,4,5]
[5,5,5,5,5]

"""


def solution(n: int, left: int, right: int) -> List[int]:
    s_row = left // n
    s_col = left % n
    e_row = right // n
    e_col = right % n

    answer = []
    for row in range(s_row, e_row + 1):
        sc = s_col if row == s_row else 0
        ec = e_col + 1 if row == e_row else n
        for col in range(sc, ec):
            answer.append(max(row + 1, col + 1))

    return answer


if __name__ == "__main__":
    tests = [
        [3, 2, 5],
        [3, 1, 8],
        [4, 7, 14],
        [1, 0, 0],
        [10, 40, 50],
        [10**7, (10**6) ** 2 + 1234567, ((10**6) ** 2) + 1334567],
    ]
    answers = [
        [3, 2, 2, 3],
        [2, 3, 2, 2, 3, 3, 3, 3],
        [4, 3, 3, 3, 4, 4, 4, 4],
        [1],
        [5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 6],
        [],
    ]

    tester = Tester(solution, verbose=0)
    tester.test(tests, answers)
