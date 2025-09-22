from tester import Tester
from typing import List
import heapq

"""
준호는 디펜스 게임을 하고 있으며, 병사 n명과 무적권 k개를 가지고 연속되는 적의 공격을 막아야 합니다.

게임 규칙:
• 매 라운드 enemy[i]명의 적이 등장
• 병사가 enemy[i]명 이상 있으면 막고 병사 소모
• 병사가 부족하면 무적권으로 막을 수 있음
• 무적권은 최대 k번 사용 가능
• 병사가 부족하고 무적권도 없으면 게임 종료

목표:
적절히 병사와 무적권을 사용하여 최대한 많은 라운드를 막을 수 있도록 하자.

입력값:
• n (1 ≤ n ≤ 1,000,000,000): 병사의 수
• k (1 ≤ k ≤ 500,000): 무적권 사용 가능 횟수
• enemy (1 ≤ len(enemy) ≤ 1,000,000, 1 ≤ enemy[i] ≤ 1,000,000): 각 라운드의 적 수

출력값:
• 막을 수 있는 최대 라운드 수 (모든 라운드 가능하면 len(enemy))

입출력 예
n   k   enemy                        result
7   3   [4, 2, 4, 5, 3, 3, 1]       5
2   4   [3, 3, 3, 3]                4

입출력 예 설명
예 #1: 1,3,5 라운드를 무적권으로, 2,4 라운드를 병사로 막고 5라운드까지 가능
예 #2: 모든 라운드 무적권으로 처리하여 4라운드 가능
"""


def solution(n: int, k: int, enemy: List[int]) -> int:
    queue = []
    for i in range(len(enemy)):
        heapq.heappush(queue, enemy[i])

        if len(queue) > k:
            n -= heapq.heappop(queue)

        if n < 0:
            return i

    return len(enemy)


if __name__ == "__main__":
    tests = [
        [7, 3, [4, 2, 4, 5, 3, 3, 1]],
        [2, 4, [3, 3, 3, 3]],
    ]
    answers = [5, 4]

    tester = Tester(solution)
    tester.test(tests, answers)
