from tester import Tester, generate_random_int_array
from typing import List

"""
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다.
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고
나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
- 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
- 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

입출력 예
citations = [3, 0, 6, 1, 5]
return = 3

입출력 예 설명
이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다. 그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.

1,1,1,1,1,1

0 1 3 5 6

6 5 3 1 0
0 1 2 3 4
4 3 2 1 0
"""


def solution(citations: List[int]) -> int:
    citations.sort(reverse=True)
    n = len(citations)
    for i in range(n):
        if citations[i] <= i:
            return i

    return n


if __name__ == "__main__":
    tests = [
        [[3, 0, 6, 1, 5]],
        [[1, 2, 4, 5, 6, 7, 30]],
        [[1, 5, 2, 7, 4, 3, 7, 6, 9, 5]],
        [generate_random_int_array(10, start_n=0, end_n=10)],
    ]
    answers = [3, 3, 4, solution(*tests[-1])]
    """
    1: (1, 10)
    2: (2, 9)
    3: (3, 8)
    4: (4, 7)
    5: (6, 6)
    6: (7, 4)
    7: (9, 3)
    9: (10, 1)
    """

    tester = Tester(solution2, verbose=0)
    tester.test(tests, answers)
