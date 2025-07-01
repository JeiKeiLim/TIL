from tester import Tester, generate_random_int_array
from typing import List

"""
철수와 영희는 선생님으로부터 숫자가 하나씩 적힌 카드들을 절반씩 나눠서 가진 후, 다음 두 조건 중 하나를 만족하는 가장 큰 양의 정수 a의 값을 구하려고 합니다.
1. 철수가 가진 카드들에 적힌 모든 숫자를 나눌 수 있고 영희가 가진 카드들에 적힌 모든 숫자들 중 하나도 나눌 수 없는 양의 정수 a
2. 영희가 가진 카드들에 적힌 모든 숫자를 나눌 수 있고, 철수가 가진 카드들에 적힌 모든 숫자들 중 하나도 나눌 수 없는 양의 정수 a

조건을 만족하는 가장 큰 정수 a를 구하세요. 없다면 0을 return 하세요.

제한사항
• 1 ≤ arrayA의 길이 = arrayB의 길이 ≤ 500,000
• 1 ≤ arrayA[i], arrayB[i] ≤ 100,000,000
• arrayA와 arrayB에는 중복된 원소가 있을 수 있습니다.

입출력 예
arrayA              arrayB              result
[10, 17]            [5, 20]             0
[10, 20]            [5, 17]             10
[14, 35, 119]       [18, 30, 102]       7

입출력 예 설명
예 #1: 조건을 만족하는 양의 정수 a는 존재하지 않습니다.
예 #2: 철수가 가진 숫자들은 10으로 나눌 수 있고, 영희의 카드 숫자 중 어떤 것도 10으로 나눠지지 않습니다.
예 #3: 철수는 7로 나누어지고, 영희는 7로 나눠지지 않기 때문에 7을 return 합니다.
"""

import math


def solution2(arrayA: List[int], arrayB: List[int]) -> int:
    def multi_gcd(arr: List[int]) -> int:
        if not arr:
            return 0
        n = len(arr)
        if n < 2:
            return arr[0]

        result = math.gcd(arr[0], arr[1])
        for i in range(2, n):
            result = math.gcd(result, arr[i])
        return result

    def get_max_div(arr1: List[int], arr2: list[int]) -> int:
        max_gcd = multi_gcd(arr1)

        for n2 in arr2:
            if n2 % max_gcd == 0:
                return 0

        return max_gcd

    return max(get_max_div(arrayA, arrayB), get_max_div(arrayB, arrayA))


def solution(arrayA: List[int], arrayB: List[int]) -> int:
    def get_max_div(arr1: List[int], arr2: list[int]) -> int:
        for div in range(min(arr1), 1, -1):
            is_dividible = True
            for num1, num2 in zip(arr1, arr2):
                if num1 % div != 0 or num2 % div == 0:
                    is_dividible = False
                    break
            if is_dividible:
                return div

        return 0

    return max(get_max_div(arrayA, arrayB), get_max_div(arrayB, arrayA))


if __name__ == "__main__":
    tests = [
        [[10, 17], [5, 20]],
        [[10, 20], [5, 17]],
        [[14, 35, 119], [18, 30, 102]],
        [[163, 151, 2], [144, 138, 30]],
        [[191, 51, 25], [51, 84, 21]],
        [
            generate_random_int_array(3, start_n=1, end_n=200),
            generate_random_int_array(3, start_n=1, end_n=200),
        ],
        [
            generate_random_int_array(500_000, start_n=10_000_000, end_n=100_000_000),
            generate_random_int_array(500_000, start_n=10_000_000, end_n=100_000_000),
        ],
    ]
    answers = [0, 10, 7, 6, 0, solution(*tests[-1]), -1]

    tester = Tester(solution2)
    tester.test(tests, answers)
