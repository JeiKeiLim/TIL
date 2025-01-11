from tester import Tester
from typing import List

"""
주차장의 요금표와 차량이 들어오고 나간 기록이 주어졌을 때, 차량별로 주차 요금을 계산하려고 합니다.

제한사항
- fees의 길이 = 4
  fees[0] = 기본 시간(분)
  fees[1] = 기본 요금(원)
  fees[2] = 단위 시간(분)
  fees[3] = 단위 요금(원)
- 1 ≤ fees[0], fees[2] ≤ 1,439
- 0 ≤ fees[1] ≤ 100,000
- 1 ≤ fees[3] ≤ 10,000
- 1 ≤ records의 길이 ≤ 1,000
- records의 각 원소는 "시각 차량번호 내역" 형식의 문자열입니다.

입출력 예
fees               records                                                                                     result
[180, 5000, 10, 600] ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
                      "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]                     [14600, 34400, 5000]
"""


def solution(fees: List[int], records: List[str]) -> List[int]:
    in_map = {}

    parking_time = {}

    for record in records:
        time, plate, status = record.split(" ")
        plate = int(plate)
        hour, minute = time.split(":")
        time = int(hour)*60 + int(minute)
        if status == "IN":
            in_map[plate] = time
            continue
        park_time = time - in_map[plate]
        parking_time[plate] = parking_time.get(plate, 0) + park_time
        del in_map[plate]

    for key, value in in_map.items():
        park_time = (23*60 + 59) - value
        parking_time[key] = parking_time.get(key, 0) + park_time

    keys = sorted(parking_time.keys())
    results = []
    for key in keys:
        park_time = parking_time[key]
        park_time = max(0, park_time-fees[0])

        m_time = park_time / fees[2]
        m_time = int(m_time) + int((m_time-int(m_time)) > 0)

        park_fee = fees[1] + (m_time * fees[3])
        results.append(park_fee)

    return results


if __name__ == "__main__":
    tests = [
        [
            [180, 5000, 10, 600],
            [
                "05:34 5961 IN",
                "06:00 0000 IN",
                "06:34 0000 OUT",
                "07:59 5961 OUT",
                "07:59 0148 IN",
                "18:59 0000 IN",
                "19:09 0148 OUT",
                "22:59 5961 IN",
                "23:00 5961 OUT",
            ],
        ],
        [
            [120, 0, 60, 591],
            [
                "16:00 3961 IN",
                "16:00 0202 IN",
                "18:00 3961 OUT",
                "18:00 0202 OUT",
                "23:58 3961 IN",
            ],
        ],
        [[1, 461, 1, 10], ["00:00 1234 IN"]],
    ]
    answers = [
        [14600, 34400, 5000],
        [0, 591],
        [14841],
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
