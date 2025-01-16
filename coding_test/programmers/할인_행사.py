from tester import Tester

from typing import List

"""
정현이가 원하는 제품을 모두 할인받을 수 있는 회원등록 날짜의 총 일수를 반환하세요.
가능한 날이 없으면 0을 반환하세요.

제한사항
- 1 ≤ want의 길이 = number의 길이 ≤ 10
- 1 ≤ number[i] ≤ 10
- number의 원소의 합은 10
- 10 ≤ discount의 길이 ≤ 100,000
- want와 discount의 원소는 알파벳 소문자로 이루어진 문자열입니다.
- 1 ≤ want의 원소의 길이, discount의 원소의 길이 ≤ 12

입출력 예
want                                  number          discount                                                                                       result
["banana", "apple", "rice", "pork", "pot"]
[3, 2, 2, 2, 1]
["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
3

j=0
1, -1, 0, 0, 1


["apple"]
[10]
["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
0
"""


def solution(want: List[str], number: List[int], discount: List[str]) -> int:
    desire_day = 10
    j = 0
    want_map = {want[i]: number[i] for i in range(len(want))}
    answer = 0

    for i in range(len(discount)):
        if discount[i] in want_map:
            want_map[discount[i]] -= 1

        if (i - j) >= desire_day:
            if discount[j] in want_map:
                want_map[discount[j]] += 1
            j += 1

        if sum([1 if val > 0 else 0 for val in want_map.values()]) == 0:
            answer += 1

    return answer


if __name__ == "__main__":
    tests = [
        [
            ["banana", "apple", "rice", "pork", "pot"],
            [3, 2, 2, 2, 1],
            [
                "chicken",
                "apple",
                "apple",
                "banana",
                "rice",
                "apple",
                "pork",
                "banana",
                "pork",
                "rice",
                "pot",
                "banana",
                "apple",
                "banana",
            ],
        ],
        [
            ["apple"],
            [10],
            [
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
            ],
        ],
    ]
    answers = [
        3,
        0,
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
