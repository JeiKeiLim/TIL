from tester import Tester

from typing import List

"""
선행 스킬 순서 skill과 유저들이 만든 스킬트리들을 담은 배열 skill_trees가 주어질 때, 
가능한 스킬트리 개수를 반환하세요.

제한조건
- skill은 1 이상 26 이하 길이의 문자열이며, 중복되지 않는 알파벳 대문자로 구성됩니다.
- skill_trees는 길이 1 이상 20 이하인 배열입니다.
- skill_trees의 원소는 길이 2 이상 26 이하의 문자열이며, 중복되지 않는 알파벳 대문자로 구성됩니다.

입출력 예
skill        skill_trees                   result
"CBD"        ["BACDE", "CBADF", 
              "AECB", "BDA"]               2
"""


def solution(skill: str, skill_trees: List[str]) -> int:
    answer = 0
    for tree in skill_trees:
        is_possible = True
        skill_i = 0
        for j in range(len(tree)):
            if tree[j] in skill:
                if skill[skill_i] == tree[j]:
                    skill_i += 1
                else:
                    is_possible = False
                    break
        if is_possible:
            answer += 1

    return answer


if __name__ == "__main__":
    tests = [
        ["CBD", ["BACDE", "CBADF", "AECB", "BDA"]],
    ]
    answers = [
        2,
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
