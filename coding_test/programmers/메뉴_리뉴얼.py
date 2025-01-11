from tester import Tester

from typing import List
from itertools import combinations
from collections import Counter

"""
각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders, 추가하고 싶은 코스요리를 구성하는 단품메뉴들의
갯수가 담긴 배열 course가 주어질 때, 새로 추가할 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 반환하세요.

제한사항
- orders 배열의 크기는 2 이상 20 이하입니다.
- orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.
- 각 문자열은 알파벳 대문자로만 이루어져 있으며 중복된 알파벳은 없습니다.
- course 배열의 크기는 1 이상 10 이하입니다.
- course 배열의 각 원소는 2 이상 10 이하의 자연수가 오름차순으로 정렬되어 있습니다.
- 정답은 사전 순으로 오름차순 정렬된 문자열 배열로 반환합니다.

입출력 예
orders                            course    result
["ABCFG", "AC", "CDE",
 "ACDE", "BCFG", "ACDEH"]          [2, 3, 4] ["AC", "ACDE", "BCFG", "CDE"]
["ABCDE", "AB", "CD",
 "ADE", "XYZ", "XYZ", "ACD"]       [2, 3, 5] ["ACD", "AD", "ADE", "CD", "XYZ"]

 ABCDE: 1
 AB: 2
 AC: 2
 AD: 3  MAX 2
 AE: 2
 ACD: 2  MAX 3
 ADE: 2
 CD: 3  MAX 2
 XYZ: 2  MAX3

["XYZ", "XWY", "WXA"]              [2, 3, 4] ["WX", "XY"]
"""


def solution2(orders: List[str], course: List[int]) -> List[str]:
    course_cnt = []
    for n_course in course:
        course_sets = []
        for order in orders:
            course_sets.extend(
                ["".join(comb) for comb in combinations(sorted(order), n_course)]
            )
        course_cnt.append(Counter(course_sets))

    result = []
    for cnt in course_cnt:
        if len(cnt) == 0:
            continue
        max_cnt = max(cnt.values())
        if max_cnt < 2:
            continue
        for key, value in cnt.items():
            if value == max_cnt:
                result.append(key)

    return sorted(result)


def solution(orders: List[str], course: List[int]) -> List[str]:
    max_freq = {}
    course_freq = {}

    final_courses = {}

    for order in orders:
        for n_course in course:
            for comb in combinations(sorted(order), n_course):
                course_set = "".join(comb)
                n_course = len(course_set)

                course_freq[course_set] = course_freq.get(course_set, 0) + 1

    for key, value in course_freq.items():
        n_course = len(key)

        if max_freq.get(n_course, 0) < value > 1:
            max_freq[n_course] = value
            final_courses[n_course] = [key]
        elif max_freq.get(n_course, 0) == value:
            final_courses[n_course] = final_courses.get(n_course, []) + [key]

    results = []
    for vals in final_courses.values():
        for val in vals:
            results.append(val)

    return sorted(results)


if __name__ == "__main__":
    tests = [
        [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]],
        [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]],
        [["XYZ", "XWY", "WXA"], [2, 3, 4]],
    ]
    answers = [
        ["AC", "ACDE", "BCFG", "CDE"],
        ["ACD", "AD", "ADE", "CD", "XYZ"],
        ["WX", "XY"],
    ]

    tester = Tester(solution2)
    tester.test(tests, answers)
