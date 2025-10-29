from tester import Tester, generate_random_int_array
from typing import List

"""
문제 설명
마인은 곡괭이로 광산에서 광석을 캐려고 합니다. 다이아몬드, 철, 돌 곡괭이를 각각 0~5개까지 가지고 있으며,
각 곡괭이로 광물을 캘 때의 피로도는 아래 표와 같습니다.

곡괭이 종류 | diamond | iron | stone
다이아몬드  |    1    |   1  |   1
철          |    5    |   1  |   1
돌          |   25    |   5  |   1

각 곡괭이는 광물 5개를 캘 수 있고, 광물은 주어진 순서대로만 캘 수 있습니다.
곡괭이를 선택해 5개 광물을 연속으로 캐고, 다음 곡괭이로 또 5개를 캐는 방식으로 작업을 진행하며,
더 이상 곡괭이가 없거나 광물이 없으면 종료됩니다.

목표: 최소 피로도로 모든 광물을 캐는 것

입력
• picks: [dia, iron, stone] 형식, 각 곡괭이의 개수
• minerals: "diamond", "iron", "stone" 으로 구성된 광물 리스트

제한사항
• 0 ≤ dia, iron, stone ≤ 5
• 곡괭이는 최소 하나 이상
• 5 ≤ len(minerals) ≤ 50

출력
• 최소 피로도 (정수)

입출력 예
picks           minerals                                                              result
[1, 3, 2]       ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]  12
[0, 1, 1]       ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]  50

설명
예 #1:
다이아 곡괭이로 앞 5개 → 피로도 5, 철 곡괭이로 나머지 3개 → 1 + 5 + 1 = 7 → 총 12

예 #2:
철 곡괭이로 다이아 5개 → 5x5=25, 돌 곡괭이로 철 5개 → 5x5=25 → 총 50
"""


def solution(picks: List[int], minerals: List[str]) -> int:
    cost_map = {
        "diamond": (1, 5, 25),
        "iron": (1, 1, 5),
        "stone": (1, 1, 1)
    }
    n = len(minerals)
    def dfs(idx: int, picks: list[int], cost: int) -> int:
        if idx >= n:
            return cost

        results = []

        for i in range(3):
            if picks[i] == 0:
                continue
            new_cost = cost
            for j in range(5):
                if idx+j >= n:
                    break
                new_cost += cost_map[minerals[idx+j]][i]
            new_picks = picks.copy()
            new_picks[i] -= 1
            results.append(dfs(idx+5, new_picks, new_cost))
        if not results:
            return cost
        return min(results)

    answer = dfs(0, picks, 0)
    return answer


def solution2(picks: List[int], minerals: List[str]) -> int:
    answer = 0
    fatigue_map = {
        "diamond": [1, 5, 25],
        "iron": [1, 1, 5],
        "stone": [1, 1, 1]
    }

    num_picks = sum(picks)
    minerals_to_mine = minerals[:num_picks * 5]

    chunks = []
    for i in range(0, len(minerals_to_mine), 5):
        chunk = minerals_to_mine[i:i+5]
        fatigue_with_stone = sum(fatigue_map[mineral][2] for mineral in chunk)
        chunks.append((fatigue_with_stone, chunk))
    
    chunks.sort(key=lambda x: x[0], reverse=True)

    for _, chunk in chunks:
        pick_idx = -1
        if picks[0] > 0:
            pick_idx = 0
            picks[0] -= 1
        elif picks[1] > 0:
            pick_idx = 1
            picks[1] -= 1
        elif picks[2] > 0:
            pick_idx = 2
            picks[2] -= 1
        
        if pick_idx == -1:
            break

        answer += sum(fatigue_map[mineral][pick_idx] for mineral in chunk)

    return answer


if __name__ == "__main__":
    picks = ("diamond", "iron", "stone")
    tests = [
        [
            [1, 3, 2],
            [
                "diamond",
                "diamond",
                "diamond",
                "iron",
                "iron",
                "diamond",
                "iron",
                "stone",
            ],
        ],
        [
            [0, 1, 1],
            [
                "diamond",
                "diamond",
                "diamond",
                "diamond",
                "diamond",
                "iron",
                "iron",
                "iron",
                "iron",
                "iron",
                "diamond",
            ],
        ],
        [
            [1, 3, 2],
            [
                "stone",
                "stone",
                "stone",
                "stone",
                "stone",
                "stone",
                "iron",
                "diamond",
                "diamond",
                "diamond",
                "diamond",
                "diamond",
            ],
        ],
        [
            generate_random_int_array(3, end_n=1000),
            list(map(lambda x: picks[x], generate_random_int_array(10000, end_n=2)))
        ]
    ]
    answers = [12, 50, 20, -1]

    tester = Tester(solution2)
    tester.test(tests, answers)
