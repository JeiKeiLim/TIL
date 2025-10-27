from tester import Tester
from typing import List

"""
문제 설명
콜라츠 추측이란 로타르 콜라츠(Lothar Collatz)가 1937년에 제기한 추측으로 
모든 자연수 k에 대해 다음 작업을 반복하면 항상 1로 만들 수 있다는 추측입니다.

1-1. 입력된 수가 짝수라면 2로 나눕니다.
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
2. 결과로 나온 수가 1보다 크다면 1번 작업을 반복합니다.

예를 들어 주어진 수가 5라면 5 → 16 → 8 → 4 → 2 → 1이 되어 총 5번만에 1이 됩니다.
수가 커졌다 작아지기를 반복하는 모습이 비구름에서 빗방울이 오르락내리락하며 우박이 되는 모습과 비슷하다고 하여 
‘우박수’ 또는 ‘우박수열’이라고 부르기도 합니다. 

현재 이 추측이 참인지 거짓인지 증명되지 않았지만 약 1해까지의 수에서 반례가 없음이 밝혀져 있습니다.

은지는 우박수열을 좌표 평면 위에 꺾은선 그래프로 나타내보려고 합니다.
초항이 k인 우박수열이 있다면, x = 0일 때 y = k이고 다음 우박수는 x = 1에 표시합니다.
이런 식으로 우박수가 1이 될 때까지 점들을 찍고 인접한 점들끼리 직선으로 연결하면 꺾은선 그래프가 됩니다.

은지는 이렇게 만든 꺾은선 그래프를 정적분 해보고 싶어졌습니다.
x에 대한 어떤 범위 [a, b]가 주어진다면 이 범위에 대한 정적분 결과는 
꺾은선 그래프와 x = a, x = b, y = 0으로 둘러싸인 공간의 면적과 같습니다.

은지는 이것을 ‘우박수열 정적분’이라고 정의하였고, 다양한 구간에 대해서 이를 계산하려고 합니다.

0 이상의 수 b에 대해 [a, -b]에 대한 정적분 결과는 
x = a, x = n - b, y = 0으로 둘러싸인 공간의 면적으로 정의하며, 
이때 n은 k가 초항인 우박수열이 1이 될 때까지의 횟수를 의미합니다.

예시)
5를 초항으로 하는 우박수열은 5 → 16 → 8 → 4 → 2 → 1 입니다.
좌표 평면으로 옮기면 (0, 5), (1, 16), (2, 8), (3, 4), (4, 2), (5, 1) 이 되며 
이 점들을 연결하면 꺾은선 그래프가 됩니다.
[0, 0] 구간에 대한 정적분은 전체 구간의 넓이,
[1, -2] 구간에 대한 정적분은 1 ≤ x ≤ 3 구간의 넓이를 의미합니다.

초항 k와, 정적분을 구하는 구간들의 목록 ranges가 주어졌을 때 
정적분의 결과 목록을 return 하도록 solution 함수를 완성하세요.

단, 구간의 시작점이 끝점보다 크면 (-1)로 정의합니다.

제한사항
• 2 ≤ k ≤ 10,000
• 1 ≤ ranges의 길이 ≤ 10,000
  ◦ ranges의 원소는 [a, b] 형식이며 0 ≤ a < 200, -200 < b ≤ 0
• 주어진 모든 입력에 대해 정적분의 결과는 2^27을 넘지 않습니다.
• 정답은 실수형으로 출력합니다.

입출력 예
k   ranges                                result
5   [[0,0],[0,-1],[2,-3],[3,-3]]         [33.0, 31.5, 0.0, -1.0]
3   [[0,0],[1,-2],[3,-3]]                [47.0, 36.0, 12.0]

입출력 예 설명
예 #1
• 5로 시작하는 우박수열: 5 → 16 → 8 → 4 → 2 → 1
• 각 구간의 넓이: 10.5, 12, 6, 3, 1.5
예 #2
• 3으로 시작하는 우박수열: 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
• 각 구간의 넓이: 47, 36, 12
"""


def solution2(k: int, ranges: List[List[int]]) -> List[float]:
    prev_k = k
    integrates = []
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        integrates.append((k + prev_k) / 2)
        prev_k = k

    answer = []
    n = len(integrates)
    prefix_sum = [0.0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + integrates[i]

    for a, b in ranges:
        b = n + b
        if a > b:
            answer.append(-1.0)
        else:
            answer.append(prefix_sum[b] - prefix_sum[a])
    return answer


def solution(k: int, ranges: List[List[int]]) -> List[float]:
    prev_k = k
    integrates = []
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        integrates.append((k + prev_k) / 2)
        prev_k = k

    n = len(integrates) + 1
    answer = []
    for a, b in ranges:
        if a == 0 and b == 0:
            answer.append(sum(integrates))
        elif b < 0 and a >= (n + b):
            answer.append(-1)
        elif a > n - 1:
            answer.append(-1)
        elif b == 0:
            answer.append(sum(integrates[a:]))
        else:
            answer.append(sum(integrates[a:b]))

    return answer


if __name__ == "__main__":
    tests = [
        [5, [[0, 0], [0, -1], [2, -3], [3, -3]]],
        [3, [[0, 0], [1, -2], [3, -3]]],
        [5, [[1, 0], [6, 0]]],
        [10_000, [[0, 0] for _ in range(10_000)]],
    ]
    answers = [[33.0, 31.5, 0.0, -1.0], [47.0, 36.0, 12.0], [22.5, -1], [20710.5] * 10_000]

    tester = Tester(solution2)
    tester.test(tests, answers)
