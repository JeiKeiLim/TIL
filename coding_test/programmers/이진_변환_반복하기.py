from tester import Tester
from typing import List

"""
0과 1로 이루어진 어떤 문자열 x에 대해 다음과 같은 이진 변환을 정의합니다.
1. x의 모든 0을 제거합니다.
2. x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
s가 "1"이 될 때까지 반복했을 때의 이진 변환 횟수와 제거된 0의 개수를 구하세요.

제한사항:
- s의 길이는 1 이상 150,000 이하입니다.
- s에는 '1'이 최소 하나 이상 포함되어 있습니다.

입출력 예:
s               result
"110010101001"  [3,8]
"01110"         [3,3]
"1111111"       [4,1]
"""


def solution(s: str) -> List[int]:
    answer = [0, 0]

    while s != "1":
        answer[0] += 1
        prev_len = len(s)
        s = "1" * s.count("1")
        answer[1] += prev_len - len(s)
        s = bin(len(s))[2:]

    return answer


if __name__ == "__main__":
    tests = [
        ["110010101001"],
        ["01110"],
        ["1111111"],
    ]
    answers = [
        [3, 8],
        [3, 3],
        [4, 1],
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
