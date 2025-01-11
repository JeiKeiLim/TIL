from tester import Tester

from typing import List

"""
n개의 요소를 가진 튜플을 n-튜플(n-tuple)이라고 하며, 중복되지 않는 원소로 이루어진 튜플을 집합으로 표현할 때,
집합의 크기가 작은 순서대로 주어졌을 때 원래 튜플을 구하는 문제입니다.

제한사항
- s의 길이는 5 이상 1,000,000 이하입니다.
- s는 숫자와 '{', '}', ',' 로만 이루어져 있습니다.
- 숫자가 0으로 시작하는 경우는 없습니다.
- s는 항상 중복되는 원소가 없는 튜플을 올바르게 표현하고 있습니다.
- s가 표현하는 튜플의 원소는 1 이상 100,000 이하인 자연수입니다.
- return 하는 배열의 길이가 1 이상 500 이하인 경우만 입력으로 주어집니다.

입출력 예
s                                result
"{{2},{2,1},{2,1,3},{2,1,3,4}}"  [2, 1, 3, 4]
"{{1,2,3},{2,1},{1,2,4,3},{2}}"  [2, 1, 3, 4]
"{{20,111},{111}}"               [111, 20]
"{{123}}"                        [123]
"{{4,2,3},{3},{2,3,4,1},{2,3}}"  [3, 2, 4, 1]
"""


def solution(s: str) -> List[int]:
    s_map = {}
    nums = s.split("},{")
    for num in nums:
        num = num.replace("{", "").replace("}", "")
        num_list = [int(n) for n in num.split(",")]

        for n in num_list:
            s_map[n] = s_map.get(n, 0) + 1

    keys = sorted(s_map.keys(), key=lambda x: s_map[x], reverse=True)

    return keys


if __name__ == "__main__":
    tests = [
        ["{{2},{2,1},{2,1,3},{2,1,3,4}}"],
        ["{{1,2,3},{2,1},{1,2,4,3},{2}}"],
        ["{{20,111},{111}}"],
        ["{{123}}"],
        ["{{4,2,3},{3},{2,3,4,1},{2,3}}"],
    ]
    answers = [
        [2, 1, 3, 4],
        [2, 1, 3, 4],
        [111, 20],
        [123],
        [3, 2, 4, 1],
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
