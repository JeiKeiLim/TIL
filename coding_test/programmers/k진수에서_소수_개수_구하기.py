from tester import Tester
from random import randint

"""
문제 설명
양의 정수 n이 주어집니다. 이 숫자를 k진수로 바꿨을 때, 변환된 수 안에 아래 조건에 맞는 소수(Prime number)가 몇 개인지 알아보려 합니다.
- 0P0처럼 소수 양쪽에 0이 있는 경우
- P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
- 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
- P처럼 소수 양쪽에 아무것도 없는 경우
- 단, P는 각 자릿수에 0을 포함하지 않는 소수입니다. 예를 들어, 101은 P가 될 수 없습니다.

예를 들어, 437674을 3진수로 바꾸면 211020101011입니다. 여기서 찾을 수 있는 조건에 맞는 소수는 왼쪽부터 순서대로 211, 2, 11이 있으며, 총 3개입니다. (211, 2, 11을 k진법으로 보았을 때가 아닌, 10진법으로 보았을 때 소수여야 한다는 점에 주의합니다.) 211은 P0 형태에서 찾을 수 있으며, 2는 0P0에서, 11은 0P에서 찾을 수 있습니다.

정수 n과 k가 매개변수로 주어집니다. n을 k진수로 바꿨을 때, 변환된 수 안에서 찾을 수 있는 위 조건에 맞는 소수의 개수를 return 하도록 solution 함수를 완성해 주세요.

13
111

13
1

제한사항
- 1 ≤ n ≤ 1,000,000
- 3 ≤ k ≤ 10

입출력 예
n       k   result
437674  3   3
110011  10  2
"""


def solution(n: int, k: int) -> int:
    converted = []
    while n > 0:
        converted.append(n % k)
        n = n // k
    converted = converted[::-1]
    if converted[-1] != 0:
        converted.append(0)

    answer = 0
    check_num = 0
    for num in converted:
        if num == 0:
            if check_num > 1:
                is_prime = 1
                for i in range(2, int(check_num**0.5) + 1):
                    if check_num % i == 0:
                        is_prime = 0
                        break
                answer += is_prime
            check_num = 0
        check_num = check_num * 10 + num
    return answer


if __name__ == "__main__":
    tests = [
        [437674, 3],
        [110011, 10],
        [977391, 3],
        [482475, 3],
        [875946, 3],
        [56011, 6],
        [9565681, 3],
        [randint(100000, 1000000), 3],
    ]
    answers = [3, 2, 0, 0, 1, 1, 1, -1]

    tester = Tester(solution)
    tester.test(tests, answers)
