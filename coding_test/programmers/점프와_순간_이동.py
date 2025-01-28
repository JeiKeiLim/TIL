from tester import Tester

"""
OO 연구소는 한 번에 K 칸을 앞으로 점프하거나, (현재까지 온 거리) x 2에 해당하는 위치로 순간이동을 할 수 있는 특수한 기능을 가진 아이언 슈트를 개발하여 판매하고 있습니다.
이 아이언 슈트는 건전지로 작동되며, 점프 시 K만큼의 건전지 사용량이 들지만, 순간이동 시 사용량이 들지 않습니다.
아이언 슈트 구매자가 N만큼 떨어져 있는 장소로 갈 때 최소의 건전지 사용량을 구하는 solution 함수를 작성하세요.

제한사항:
- 숫자 N: 1 이상 10억 이하의 자연수
- 숫자 K: 1 이상의 자연수 (문제에서는 항상 1칸 점프 기준)

입출력 예
N    result
5    2
6    2
5000 5
"""


def solution2(n: int) -> int:
    answer = 0
    while n > 0:
        if n % 2 != 0:
            answer += 1
            n -= 1
        n = n // 2

    return answer


def solution(n: int) -> int:
    dp = [n] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        dp[i] = min(dp[i - 1] + 1, dp[i])
        if i*2 <= n:
            dp[i*2] = min(dp[i], dp[i*2])

    return dp[-1]


if __name__ == "__main__":
    tests = [
        [5],
        [6],
        [5000],
        [999999],
        [1000000000],
    ]
    answers = [2, 2, 5, 12, -1]

    tester = Tester(solution2)
    tester.test(tests, answers)
