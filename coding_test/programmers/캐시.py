from tester import Tester, generate_random_string
from typing import List
from collections import deque

"""
지도개발팀에서 근무하는 제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있습니다.
DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.

입력 형식
- 캐시 크기(cacheSize)는 0 ≦ cacheSize ≦ 30
- 도시이름 배열(cities)은 최대 100,000개이며 각 도시 이름은 영문자로 최대 20자, 대소문자 구분 없음

조건
- 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
- cache hit일 경우 실행시간은 1이다.
- cache miss일 경우 실행시간은 5이다.

입출력 예시:
cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
=> return 50

* No cache hit

cacheSize = 5
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
=> return 30

30
[Jeju, Pangyo, Seoul, NewYork, LA]
"""


def solution(cacheSize: int, cities: List[str]) -> int:
    queue = deque(maxlen=cacheSize)
    answer = 0
    for city in cities:
        city = city.lower()
        if city in queue:
            answer += 1
            queue.remove(city)
            queue.append(city)
        else:
            answer += 5
            queue.append(city)
    return answer


if __name__ == "__main__":
    tests = [
        [
            3,
            [
                "Jeju",
                "Pangyo",
                "Seoul",
                "NewYork",
                "LA",
                "Jeju",
                "Pangyo",
                "Seoul",
                "NewYork",
                "LA",
            ],
        ],
        [
            5,
            [
                "Jeju",
                "Pangyo",
                "Seoul",
                "NewYork",
                "LA",
                "Jeju",
                "Pangyo",
                "Seoul",
                "NewYork",
                "LA",
            ],
        ],
        [
            3,
            [
                "Jeju",
                "Pangyo",
                "Seoul",
                "Jeju",
                "Pangyo",
                "Seoul",
                "Jeju",
                "Pangyo",
                "Seoul",
            ],
        ],
        [
            2,
            [
                "Jeju",
                "Pangyo",
                "Seoul",
                "NewYork",
                "LA",
                "SanFrancisco",
                "Seoul",
                "Rome",
                "Paris",
                "Jeju",
                "NewYork",
                "Rome",
            ],
        ],
        [
            5,
            [
                "Jeju",
                "Pangyo",
                "Seoul",
                "NewYork",
                "LA",
                "SanFrancisco",
                "Seoul",
                "Rome",
                "Paris",
                "Jeju",
                "NewYork",
                "Rome",
            ],
        ],
        [2, ["Jeju", "Pangyo", "NewYork", "newyork"]],
        [0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]],
        [30, [generate_random_string(20, end_char="b") for _ in range(100_000)]]
    ]
    answers = [50, 30, 21, 60, 52, 16, 25, -1]

    tester = Tester(solution, verbose=0)
    tester.test(tests, answers)
