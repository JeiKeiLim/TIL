from tester import Tester

from typing import List

"""
자연수 x를 y로 변환하려고 합니다. 사용할 수 있는 연산은 다음과 같습니다.
    • x에 n을 더합니다
    • x에 2를 곱합니다.
    • x에 3을 곱합니다.
자연수 x, y, n이 매개변수로 주어질 때, x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return하도록 solution 함수를 완성해주세요. 이때 x를 y로 만들 수 없다면 -1을 return 해주세요.

제한사항
    • 1 ≤ x ≤ y ≤ 1,000,000
    • 1 ≤ n < y

입출력 예
x   y   n   result
10  40  5   2
10  40  30  1
2   5   4   -1

입출력 예 설명
입출력 예 #1
x에 2를 2번 곱하면 40이 되고 이때가 최소 횟수입니다.

입출력 예 #2
x에 n인 30을 1번 더하면 40이 되고 이때가 최소 횟수입니다.

입출력 예 #3
x를 y로 변환할 수 없기 때문에 -1을 return합니다.
"""


def solution3(x: int, y: int, n: int) -> int:
    dp = [2**31] * (y + 1)
    dp[x] = 0

    for i in range(x, y + 1):
        if dp[i] == 2**31:
            continue

        for idx in [i + n, i * 2, i * 3]:
            if idx <= y:
                dp[idx] = min(dp[i] + 1, dp[idx])

    return dp[y] if dp[y] < 2**31 else -1


def solution2(x: int, y: int, n: int) -> int:
    stack = [(x, 0)]
    min_op = 2**31
    while stack:
        m, step = stack.pop()

        if m == y:
            min_op = min(step, min_op)

        next_vals = [m + n, m * 2, m * 3]

        for val in next_vals:
            if (step + 1) < min_op and val <= y:
                stack.append((val, step + 1))

    return min_op if min_op < 2**15 else -1


def solution(x: int, y: int, n: int) -> int:
    def trace(m: int, step: int) -> int:
        if m > y:
            return 2**15
        if m == y:
            return step

        result1 = trace(m + n, step + 1)
        result2 = trace(m * 2, step + 1)
        result3 = trace(m * 3, step + 1)

        return min(result1, result2, result3)

    result = trace(x, 0)

    return result if result < 2**15 else -1


if __name__ == "__main__":
    tests = [
        # Strictly extracted test cases from input examples
        [10, 40, 5],
        [10, 40, 30],
        [2, 5, 4],
        [11, 1000000, 2],
    ]
    answers = [2, 1, -1, -1]

    tester = Tester(solution3)
    tester.test(tests, answers)
