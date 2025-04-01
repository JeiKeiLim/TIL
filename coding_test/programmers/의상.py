from tester import Tester
from typing import List

from math import prod
from itertools import combinations

"""
코니는 매일 다른 옷을 조합하여 입는것을 좋아합니다.

예를 들어 코니가 가진 옷이 아래와 같고,
오늘 코니가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야합니다.

종류   이름
얼굴   동그란 안경, 검정 선글라스
상의   파란색 티셔츠
하의   청바지
겉옷   긴 코트

- 코니는 각 종류별로 최대 1가지 의상만 착용할 수 있습니다.
- 착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산합니다.
- 코니는 하루에 최소 한 개의 의상은 입습니다.

코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
- clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
- 코니가 가진 의상의 수는 1개 이상 30개 이하입니다.
- 같은 이름을 가진 의상은 존재하지 않습니다.
- clothes의 모든 원소는 문자열로 이루어져 있습니다.
- 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.

입출력 예
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
return = 5

clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
return = 3
"""


def solution(clothes: List[List[str]]) -> int:
    cloth_type_map = {}
    for cloth, cloth_type in clothes:
        if cloth_type not in cloth_type_map:
            cloth_type_map[cloth_type] = [cloth]
        else:
            cloth_type_map[cloth_type].append(cloth)

    n_cloth_types = [len(val) + 1 for val in cloth_type_map.values()]

    answer = sum(n_cloth_types)
    for i in range(2, len(n_cloth_types) + 1):
        answer += sum(prod(combs) for combs in combinations(n_cloth_types, i))

    return answer


def solution2(clothes: List[List[str]]) -> int:
    clothes_dict = {}
    for cloth in clothes:
        if cloth[1] in clothes_dict:
            clothes_dict[cloth[1]] += 1
        else:
            clothes_dict[cloth[1]] = 1

    return prod([count + 1 for count in clothes_dict.values()]) - 1


if __name__ == "__main__":
    tests = [
        [
            [
                ["yellow_hat", "headgear"],
                ["blue_sunglasses", "eyewear"],
                ["green_turban", "headgear"],
            ]
        ],
        [
            [
                ["crow_mask", "face"],
                ["blue_sunglasses", "face"],
                ["smoky_makeup", "face"],
            ]
        ],
        [
            [
                ["crow_mask", "face"],
                ["blue_sunglasses", "eyewear"],
                ["green_turban", "headgear"],
                ["yellow_hat", "headgear"],
            ]
        ],
        [[[str(i * 100), str(i)] for i in range(22)]],
    ]
    answers = [5, 3, 11, 4194303]

    tester = Tester(solution2, verbose=0)
    tester.test(tests, answers)
