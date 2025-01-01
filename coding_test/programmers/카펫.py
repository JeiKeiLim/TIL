from tester import Tester

from typing import List

"""
Leo는 카펫을 사러 갔다가 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때
카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
- 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
- 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
- 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

입출력 예
brown yellow return
10    2      [4, 3]
8     1      [3, 3]
24    24     [8, 6]

※ 공지 - 2020년 2월 3일 테스트케이스가 추가되었습니다.
※ 공지 - 2020년 5월 11일 웹접근성을 고려하여 빨간색을 노란색으로 수정하였습니다.
"""


def solution(brown: int, yellow: int) -> List[int]:
    yellow_verticals = [1]
    for i in range(2, (yellow // 2) + 1):
        if yellow % i == 0:
            yellow_verticals.append(i)

    for inner_vertical in yellow_verticals:
        outer_vertical = inner_vertical + 2
        outer_horizontal = (yellow // inner_vertical) + 2

        if (outer_vertical * 2) + (outer_horizontal - 2) * 2 == brown:
            return [
                max(outer_horizontal, outer_vertical),
                min(outer_horizontal, outer_vertical),
            ]


if __name__ == "__main__":
    tests = [
        # Strictly extracted test cases from input examples
        [10, 2],
        [8, 1],
        [24, 24],
        [30, 42],
        [26, 10],
    ]
    """
    123456789
    2       8
    3       7
    4       6
    5       5
    6       4
    7       3
    876543210
    """
    answers = [[4, 3], [3, 3], [8, 6], [9, 8], [12, 3]]

    tester = Tester(solution)
    tester.test(tests, answers)
