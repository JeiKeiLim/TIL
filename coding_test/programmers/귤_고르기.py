from tester import Tester
from collections import Counter

"""
경화가 귤 k개를 고를 때, 크기가 서로 다른 종류의 수의 최솟값을 구하세요.

제한사항
- 1 ≤ k ≤ len(tangerine) ≤ 100,000
- 1 ≤ tangerine[i] ≤ 10,000,000

입출력 예
k                         tangerine                     result
6                         [1, 3, 2, 5, 4, 5, 2, 3]      3
4                         [1, 3, 2, 5, 4, 5, 2, 3]      2
2                         [1, 1, 1, 1, 2, 2, 2, 3]      1
"""


def solution(k: int, tangerine: list) -> int:
    cnt = Counter(tangerine)
    sorted_keys = sorted(cnt.keys(), key=lambda x: cnt[x], reverse=True)
    n_basket = 0
    for i in range(len(sorted_keys)):
        k -= cnt[sorted_keys[i]]
        n_basket += 1
        if k <= 0:
            break
    return n_basket


if __name__ == "__main__":
    tests = [
        [6, [1, 3, 2, 5, 4, 5, 2, 3]],
        [4, [1, 3, 2, 5, 4, 5, 2, 3]],
        [2, [1, 1, 1, 1, 2, 2, 2, 3]],
    ]
    answers = [
        3,
        2,
        1,
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
