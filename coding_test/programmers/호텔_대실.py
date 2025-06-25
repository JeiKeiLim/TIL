from tester import Tester
from typing import List

"""
호텔을 운영 중인 코니는 최소한의 객실만을 사용하여 예약 손님들을 받으려고 합니다. 
한 번 사용한 객실은 퇴실 시간을 기준으로 10분간 청소를 하고 다음 손님들이 사용할 수 있습니다.
예약 시각이 문자열 형태로 담긴 2차원 배열 book_time이 매개변수로 주어질 때, 
코니에게 필요한 최소 객실의 수를 return 하는 solution 함수를 완성해주세요.

제한사항
    • 1 ≤ book_time의 길이 ≤ 1,000
        ◦ book_time[i]는 ["HH:MM", "HH:MM"]의 형태로 이루어진 배열입니다
            ▪ [대실 시작 시각, 대실 종료 시각] 형태입니다.
        ◦ 시각은 HH:MM 형태로 24시간 표기법을 따르며, "00:00" 부터 "23:59" 까지로 주어집니다.
            ▪ 예약 시각이 자정을 넘어가는 경우는 없습니다.
            ▪ 시작 시각은 항상 종료 시각보다 빠릅니다.

입출력 예
book_time
result
[["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]  -> 3
[["09:10", "10:10"], ["10:20", "12:20"]]  -> 1
[["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]  -> 3

[900, 1030],
[1000, 1210],

입출력 예 설명
입출력 예 #1: 위 사진과 같습니다.
입출력 예 #2: 첫 번째 손님이 10시 10분에 퇴실 후 10분간 청소한 뒤 두 번째 손님이 10시 20분에 입실하여 사용할 수 있으므로 방은 1개만 필요합니다.
입출력 예 #3: 세 손님 모두 동일한 시간대를 예약했기 때문에 3개의 방이 필요합니다.
"""

import heapq


def solution2(book_time: List[List[str]]) -> int:
    reserve_states = [0] * (24 * 60 + 10)

    for b_time in book_time:
        split_times = list(map(lambda x: list(map(int, x.split(":"))), b_time))
        s_time = split_times[0][0] * 60 + split_times[0][1]
        e_time = split_times[1][0] * 60 + split_times[1][1] + 10

        reserve_states[s_time] += 1
        reserve_states[e_time] -= 1

    answer = 0
    cum_sum = 0
    for state in reserve_states:
        cum_sum += state
        answer = max(answer, cum_sum)
    return answer


def solution(book_time: List[List[str]]) -> int:
    answer = 0
    reserve_times = []
    for b_time in book_time:
        split_times = list(map(lambda x: list(map(int, x.split(":"))), b_time))
        s_time = split_times[0][0] * 60 + split_times[0][1]
        e_time = split_times[1][0] * 60 + split_times[1][1] + 10
        reserve_times.append((s_time, e_time))

    answer = 1
    reserve_times.sort()
    guest = []
    for s_time, e_time in reserve_times:
        if guest and guest[0] > s_time:
            answer += 1
        elif guest:
            heapq.heappop(guest)

        heapq.heappush(guest, e_time)
    return answer


if __name__ == "__main__":
    tests = [
        [
            [
                ["15:00", "17:00"],
                ["16:40", "18:20"],
                ["14:20", "15:20"],
                ["14:10", "19:20"],
                ["18:20", "21:20"],
            ]
        ],
        [[["09:10", "10:10"], ["10:20", "12:20"]]],
        [[["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]],
        [
            [
                ["09:00", "10:00"],
                ["09:00", "11:00"],
                ["09:00", "12:00"],
                ["10:10", "12:00"],
            ]
        ],
    ]
    answers = [3, 1, 3, 3]

    tester = Tester(solution)
    tester.test(tests, answers)
