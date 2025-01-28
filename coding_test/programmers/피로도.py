from tester import Tester
from typing import List

"""
현재 피로도 k와 각 던전별 ["최소 필요 피로도", "소모 피로도"]로 구성된 dungeons가 주어질 때,
유저가 탐험할 수 있는 최대 던전 수를 반환하는 solution 함수를 작성하세요.

제한사항:
- 1 ≤ k ≤ 5,000
- 1 ≤ len(dungeons) ≤ 8
- 각 던전의 [최소 필요 피로도, 소모 피로도]는 1 ≤ x ≤ 1,000
- 각 던전은 여러 번 탐험할 수 없으며, 순서를 바꿀 수 있음.

입출력 예:
k                 dungeons                       result
80                [[80, 20], [50, 40], [30, 10]] 3
"""


def solution3(k: int, dungeons: List[List[int]]) -> int:
    n = len(dungeons)

    def dfs(hp: int, idx: int, to_visit: List[int]) -> int:
        required_hp, damage_hp = dungeons[idx]
        if hp < required_hp:
            return 0

        hp -= damage_hp
        results = [0]
        for i in range(len(to_visit)):
            next_visit = to_visit.copy()
            next_idx = next_visit.pop(i)
            results.append(dfs(hp, next_idx, next_visit))

        return 1 + max(results)

    answer = 0
    for i in range(n):
        dungeons_to_go = [j for j in range(n) if i != j]
        answer = max(answer, dfs(k, i, dungeons_to_go))
    return answer


def solution2(k: int, dungeons: List[List[int]]) -> int:
    n = len(dungeons)

    def dfs(hp: int, idx: int, visited: set) -> int:
        required_hp, damage_hp = dungeons[idx]
        if idx in visited or hp < required_hp:
            return 0

        visited.add(idx)
        hp -= damage_hp
        result = 1 + max(
            dfs(hp, i, visited.copy())
            for i in range(n)
        )

        return result

    return max(dfs(k, i, set()) for i in range(n))


def solution(k: int, dungeons: List[List[int]]) -> int:
    n = len(dungeons)
    queue = [(k, i, set()) for i in range(n)]

    max_explore = 0

    while queue:
        hp, idx, visited = queue.pop()
        if idx in visited:
            continue
        visited.add(idx)
        required_hp, damage_hp = dungeons[idx]
        if hp < required_hp:
            continue

        hp -= damage_hp

        if hp < 0:
            continue

        max_explore = max(max_explore, len(visited))

        for i in range(n):
            if i in visited:
                continue
            queue.append((hp, i, visited.copy()))

    return max_explore


if __name__ == "__main__":
    tests = [
        [80, [[80, 20], [50, 40], [30, 10]]],
        [10, [[5, 4], [9, 2], [5, 2], [6, 1], [10, 1]]],
        [1000, [[5, 4], [9, 2], [5, 2], [6, 1], [10, 1], [100, 5], [123, 81], [5, 5]]],
    ]
    answers = [3, 4, 8]

    tester = Tester(solution3)
    tester.test(tests, answers)
