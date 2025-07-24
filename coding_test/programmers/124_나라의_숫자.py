from tester import Tester

"""
124 나라에서는 10진법과는 다른 규칙으로 수를 표현합니다.
124 나라의 규칙:
1. 자연수만 존재합니다.
2. 모든 수는 1, 2, 4만 사용하여 표현합니다.

124 나라 숫자 변환 예시:
10진법  ->  124 나라
1       ->  1
2       ->  2
3       ->  4
4       ->  11
5       ->  12
6       ->  14
7       ->  21
8       ->  22
9       ->  24
10      ->  41
11      ->  42
12      ->  44
13      ->  111
14      ->  112
15      ->  114
16      ->  121
17      ->  122
18      ->  124
19      ->  141
20      ->  142
21      ->  144
22      ->  211

입력: 자연수 n (1 ≤ n ≤ 50,000,000)
출력: 124 나라에서 사용하는 수로 변환한 문자열

입출력 예
n   result
1   "1"
2   "2"
3   "4"
4   "11"
"""


def solution2(n: int) -> str:
    digits = ["1", "2", "4"]
    res = []
    while n > 0:
        n -= 1
        res.append(digits[n % 3])
        n //= 3
    return "".join(reversed(res))


def solution(n: int) -> str:
    div_third = n // 3
    answer = str(n % 3)
    while div_third > 2:
        answer = str(div_third % 3) + answer
        div_third //= 3
    answer = list(map(int, list(str(div_third) + answer)))

    for i in range(len(answer) - 1, 0, -1):
        if answer[i] > 0:
            continue
        answer[i] = 3
        if answer[i - 1] == 0:
            continue
        answer[i - 1] -= 1

    while answer[0] == 0:
        answer.pop(0)

    answer = "".join(map(str, answer))

    return answer.replace("3", "4")


if __name__ == "__main__":
    tests = [
        # [1],
        # [2],
        # [3],
        # [4],
        # [5],
        # [6],
        # [7],
        # [8],
        [9],
        # [10],
        # [11],
        # [12],
        # [13],
        [22],
        [115],
        [937],
        [50_000_000],
    ]
    answers = [
        # "1",
        # "2",
        # "4",
        # "11",
        # "12",
        # "14",
        # "21",
        # "22",
        "24",
        # "41",
        # "42",
        # "44",
        # "111",
        "211",
        "4421",
        "421141",
        "-1",
    ]

    tester = Tester(solution2, incorrect_only=True)
    tester.test(tests, answers)
