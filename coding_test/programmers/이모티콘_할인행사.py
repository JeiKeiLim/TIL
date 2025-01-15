from tester import Tester

from typing import List, Tuple
from itertools import product

"""
n명의 카카오톡 사용자와 m개의 이모티콘에 대해 이모티콘 플러스 서비스 가입자를 최대한 늘리고,
그 다음으로 이모티콘 판매액을 최대한 늘렸을 때의 결과를 반환하세요.

제한사항
- users 배열의 길이(카카오톡 사용자 수) : 1 이상 100 이하
- emoticons 배열의 길이(이모티콘 수) : 1 이상 7 이하
- users의 원소는 [비율, 가격] 형태이며, 10 ≤ 비율 ≤ 40, 1000 ≤ 가격 ≤ 1,000,000입니다.
- emoticons의 원소는 100 ≤ 가격 ≤ 1,000,000입니다.
- 할인율은 10%, 20%, 30%, 40% 중 하나입니다.

입출력 예
users                       emoticons              result
[[40, 10000], [25, 10000]]  [7000, 9000]           [1, 5400]
[[30, 10000], [20, 9000],
 [40, 30000]]              [15000, 20000, 30000]   [2, 37000]

 7000, 10, 9000, 10
 7000, 10, 9000, 20
 ...
"""


def solution(users: List[Tuple[int, int]], emoticons: List[int]) -> List[int]:
    ne = len(emoticons)
    sale_rates = list(product(*([[10, 20, 30, 40]] * ne)))

    n_plus = 0
    max_emoji_sale = 0
    for rates in sale_rates:
        sale_total = 0
        user_plus = 0

        for rate_limit, total_limit in users:
            user_buy = 0
            for rate, price in zip(rates, emoticons):
                if rate < rate_limit:
                    continue

                sale_price = price * (1 - (rate * 0.01))
                user_buy += sale_price
                if user_buy >= total_limit:
                    user_plus += 1
                    user_buy = 0
                    break
            sale_total += user_buy

        if user_plus > n_plus:
            n_plus = user_plus
            max_emoji_sale = sale_total
        elif user_plus == n_plus:
            max_emoji_sale = max(max_emoji_sale, sale_total)

    return [n_plus, max_emoji_sale]


if __name__ == "__main__":
    tests = [
        [[[40, 10000], [25, 10000]], [7000, 9000]],
        [
            [
                [40, 2900],
                [23, 10000],
                [11, 5200],
                [5, 5900],
                [40, 3100],
                [27, 9200],
                [32, 6900],
            ],
            [1300, 1500, 1600, 4900],
        ],
        [[[20, 3000]], [3000]]
    ]
    answers = [
        [1, 5400],
        [4, 13860],
        [0, 2400]
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
