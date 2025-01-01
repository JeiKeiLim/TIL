from tester import Tester

from typing import List

"""
무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

제한사항
- 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
- 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
- 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
- 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

입출력 예
people          limit    return
[70, 50, 80, 50] 100     3
[70, 80, 50]     100     3

※ 2023년 07월 31일 테스트 케이스가 추가되었습니다. 기존에 제출한 코드가 통과하지 못할 수 있습니다.
"""


def solution(people: List[int], limit: int) -> int:
    answer = len(people)
    people.sort()

    i = 0
    j = len(people)-1

    while i < j:
        if people[j] + people[i] > limit:
            j -= 1
        else:
            i += 1
            j -= 1
            answer -= 1

    return answer


if __name__ == "__main__":
    tests = [
        # Strictly extracted test cases from input examples
        [[70, 50, 80, 50], 100],
        [[70, 80, 50], 100],
    ]
    answers = [3, 3]

    tester = Tester(solution)
    tester.test(tests, answers)
