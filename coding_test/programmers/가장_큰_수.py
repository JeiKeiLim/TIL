from tester import Tester, generate_random_int_array

from typing import List

"""
가장 큰 수

0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

100, 10, 1

제한 사항
 - numbers의 길이는 1 이상 100,000 이하입니다.
 - numbers의 원소는 0 이상 1,000 이하입니다.
 - 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

입출력 예
numbers             return
[6, 10, 2]          "6210"
[3, 30, 34, 5, 9]   "9534330"
"""


def solution(numbers: List[int]) -> str:
    if max(numbers) == 0:
        return "0"

    number_str = []
    for n in numbers:
        n_str = str(n)
        n_str = (n_str * 4)[:4]
        number_str.append((n_str, n))

    keys = sorted(
        number_str, key=lambda x: tuple(x[0]) + (4 - len(str(x[1])),), reverse=True
    )
    answer = ""
    for key in keys:
        answer += str(key[1])
    return answer


def solution3(numbers: List[int]) -> str:
    if max(numbers) == 0:
        return "0"

    num_str = list(map(str, numbers))
    num_str.sort(key=lambda x: (x * 4)[:4], reverse=True)

    return "".join(num_str)


def solution2(numbers: List[int]) -> str:
    if max(numbers) == 0:
        return "0"

    n = len(numbers)

    num_str = list(map(str, numbers))

    for i in range(n):
        for j in range(i + 1, n):
            if num_str[i] + num_str[j] < num_str[j] + num_str[i]:
                num_str[i], num_str[j] = num_str[j], num_str[i]

    return "".join(num_str)


if __name__ == "__main__":
    tests = [
        [[6, 10, 2]],
        [[3, 30, 34, 5, 9]],
        [[1, 10, 100, 1000]],
        [[33, 330, 334, 35, 39]],
        [[20, 200, 20]],
        [[0, 0, 0]],
        [[0, 0, 0, 1]],
        [[90, 99, 990, 999]],
        [[10, 11, 2, 110, 111]],
        [[90, 907, 99]],
        [[909, 90, 9]],
        [generate_random_int_array(100_000)]
    ]
    answers = [
        "6210",
        "9534330",
        "1101001000",
        "393533433330",
        "2020200",
        "0",
        "1000",
        "9999999090",
        "21111111010",
        "9990907",
        "990990",
        "-1",
    ]

    tester = Tester(solution3, verbose=0)
    tester.test(tests, answers)
