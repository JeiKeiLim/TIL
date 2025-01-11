from tester import Tester

from typing import List

"""
채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 주어질 때, 모든 기록이 처리된 후,
최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return 하세요.

제한사항
- record의 길이는 1 이상 100,000 이하입니다.
- 모든 유저는 [유저 아이디]로 구분합니다.
- record의 각 원소는 "Enter [유저 아이디] [닉네임]", "Leave [유저 아이디]", "Change [유저 아이디] [닉네임]" 형태입니다.
- 유저 아이디와 닉네임은 알파벳 대소문자 및 숫자로만 이루어져 있으며 길이는 1 이상 10 이하입니다.

입출력 예
record                                                                                     result
["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo",
 "Change uid4567 Ryan"]                                                                   ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", 
                                                                                           "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

[(Enter|Leave) userId, ...]
{userId: nickName}
"""


def solution(record: List[str]) -> List[str]:
    status = []
    nickname = {}

    for row in record:
        msgs = row.split(" ")
        user_id = msgs[1]

        if msgs[0] == "Enter":
            status.append((1, user_id))
            nickname[user_id] = msgs[2]
        elif msgs[0] == "Leave":
            status.append((0, user_id))
        elif msgs[0] == "Change":
            nickname[user_id] = msgs[2]

    answer = []
    for row in status:
        if row[0] == 1:
            postfix = "들어왔습니다."
        else:
            postfix = "나갔습니다."

        msg = f"{nickname[row[1]]}님이 {postfix}"
        answer.append(msg)

    return answer


if __name__ == "__main__":
    tests = [
        [
            [
                "Enter uid1234 Muzi",
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan",
            ]
        ],
    ]
    answers = [
        [
            "Prodo님이 들어왔습니다.",
            "Ryan님이 들어왔습니다.",
            "Prodo님이 나갔습니다.",
            "Prodo님이 들어왔습니다.",
        ]
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
