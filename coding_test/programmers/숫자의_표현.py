from tester import Tester

"""
자연수 n을 연속된 자연수들로 표현하는 방법의 수를 반환하세요.

제한사항
- n은 10,000 이하의 자연수입니다.

입출력 예
n     result
15    4
"""


def solution(n: int) -> int:
    nums = [i for i in range(1, n+1)]

    j = 0

    total = 0
    answer = 0
    for i in range(len(nums)):
        total += nums[i]
        while total > n:
            total -= nums[j]
            j += 1
        if total == n:
            answer += 1

    return answer


if __name__ == "__main__":
    tests = [
        [15],
    ]
    answers = [
        4,
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
