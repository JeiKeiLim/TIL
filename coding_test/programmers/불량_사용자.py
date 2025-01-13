from tester import Tester

from typing import List
import itertools

"""
이벤트 응모자 아이디 목록 user_id와 불량 사용자 아이디 목록 banned_id가 주어질 때,
제재 아이디 목록이 몇 가지 경우의 수로 가능한지 반환하세요.

제한사항
- user_id 배열의 크기는 1 이상 8 이하입니다.
- user_id 배열 각 원소의 길이는 1 이상 8 이하입니다.
- 응모한 사용자 아이디는 중복되지 않습니다.
- 응모한 사용자 아이디는 알파벳 소문자와 숫자로만 구성되어 있습니다.
- banned_id 배열 각 원소는 '*' 문자를 하나 이상 포함하고 있습니다.
- 같은 응모자 아이디가 중복해서 제재 아이디 목록에 들어가는 경우는 없습니다.
- 제재 아이디 목록이 동일한 경우는 하나로 처리하여 반환합니다.

입출력 예
user_id                                  banned_id               result
["frodo", "fradi", "crodo",
 "abc123", "frodoc"]                     ["fr*d*", "abc1**"]     2

["frodo", "fradi", "crodo",
 "abc123", "frodoc"]                     ["*rodo", "*rodo",
                                          "******"]              2

["frodo", "fradi", "crodo",
 "abc123", "frodoc"]                     ["fr*d*", "*rodo",
                                          "******", "******"]    3

['frodo', 'fradi'], ['frodo', 'crodo'], ['abc123', 'frodoc'], ['abc123', 'frodoc']

'frodo', 'crodo', 'abc123', 'frodoc'
'fradi', 'frodo' 'abc123' 'frodoc'
'fradi' 'crodo' 'abc123' 'frodoc'
"""


def solution(user_id: List[str], banned_id: List[str]) -> int:
    id_by_length = [[] for _ in range(9)]
    for id in user_id:
        id_by_length[len(id)].append(id)

    ban_candidates = [[] for _ in range(len(banned_id))]
    for i, bid in enumerate(banned_id):
        len_bid = len(bid)
        for uid in id_by_length[len_bid]:
            is_all_match = True
            for j in range(len_bid):
                if bid[j] == "*":
                    continue
                if bid[j] != uid[j]:
                    is_all_match = False
                    break
            if is_all_match:
                ban_candidates[i].append(uid)

    stack = [(set([ban_candidate]), 1) for ban_candidate in ban_candidates[0]]
    final_candidates = set()
    while stack:
        local_candidate, step = stack.pop()

        if step == len(banned_id):
            final_candidates.add(tuple(sorted(local_candidate)))
            continue
        for ban_candidate in ban_candidates[step]:
            next_candidate = local_candidate.copy()
            next_candidate.add(ban_candidate)
            if len(next_candidate) < (step + 1):
                continue
            stack.append((next_candidate, step + 1))

    return len(final_candidates)


if __name__ == "__main__":
    tests = [
        [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]],
        [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]],
        [
            ["frodo", "fradi", "crodo", "abc123", "frodoc"],
            ["fr*d*", "*rodo", "******", "******"],
        ],
    ]
    answers = [
        2,
        2,
        3,
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
