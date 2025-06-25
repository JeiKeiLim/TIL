from tester import Tester, generate_random_int_array
from typing import List

"""
당신은 순서대로 n개의 퍼즐을 제한 시간 내에 풀어야 하는 퍼즐 게임을 하고 있습니다. 각 퍼즐은 난이도와 소요 시간이 정해져 있습니다. 당신의 숙련도에 따라 퍼즐을 풀 때 틀리는 횟수가 바뀌게 됩니다.
현재 퍼즐의 난이도를 diff, 현재 퍼즐의 소요 시간을 time_cur, 이전 퍼즐의 소요 시간을 time_prev, 당신의 숙련도를 level이라 하면, 게임은 다음과 같이 진행됩니다.
    • diff ≤ level이면 퍼즐을 틀리지 않고 time_cur만큼의 시간을 사용하여 해결합니다.
    • diff > level이면, 퍼즐을 총 diff - level번 틀립니다.
      퍼즐을 틀릴 때마다, time_cur만큼의 시간을 사용하며, 추가로 time_prev만큼의 시간을 사용해 이전 퍼즐을 다시 풀고 와야 합니다.
      이전 퍼즐을 다시 풀 때는 이전 퍼즐의 난이도에 상관없이 틀리지 않습니다.
      diff - level번 틀린 이후에 다시 퍼즐을 풀면 time_cur만큼의 시간을 사용하여 퍼즐을 해결합니다.

예를 들어 diff = 3, time_cur = 2, time_prev = 4인 경우:
    • level = 1: (3-1)=2번 틀림 → (2+4)*2 + 2 = 14
    • level = 2: (3-2)=1번 틀림 → (2+4) + 2 = 8
    • level ≥ 3: 틀리지 않음 → 2

퍼즐 게임에는 전체 제한 시간 limit가 정해져 있습니다.
제한 시간 내에 퍼즐을 모두 해결하기 위한 숙련도의 최솟값을 구하세요.
난이도, 소요 시간은 모두 양의 정수이며, 숙련도도 양의 정수여야 합니다.

제한사항
    • 1 ≤ diffs의 길이 = times의 길이 = n ≤ 300,000
    • diffs[i]는 i번째 퍼즐의 난이도, times[i]는 i번째 퍼즐의 소요 시간입니다.
    • diffs[0] = 1
    • 1 ≤ diffs[i] ≤ 100,000
    • 1 ≤ times[i] ≤ 10,000
    • 1 ≤ limit ≤ 10^15
    • 제한 시간 내에 퍼즐을 모두 해결할 수 있는 경우만 입력으로 주어집니다.

입출력 예
diffs               times              limit       result
[1, 5, 3]           [2, 4, 7]          30          3
[1, 4, 4, 2]        [6, 3, 8, 2]       59          2
[1, 328, 467, 209, 54] [2, 7, 1, 4, 3] 1723         294
[1, 99999, 100000, 99995] [9999, 9001, 9999, 9001] 3456789012 39354
"""


def solution(diffs: List[int], times: List[int], limit: int) -> int:
    n = len(diffs)

    def is_solvable(level: int) -> bool:
        t_spend = 0
        for i in range(n):
            if diffs[i] <= level:
                t_spend += times[i]
            else:
                t_spend += (diffs[i] - level) * (
                    (times[i - 1] if i > 0 else 0) + times[i]
                ) + times[i]

            if t_spend > limit:
                return False

        return True

    left = 1
    right = max(diffs) + 1
    answer = right

    while left <= right:
        mid = (left + right) // 2

        if is_solvable(mid):
            right = mid - 1
            answer = min(answer, mid)
        else:
            left = mid + 1

    return answer


if __name__ == "__main__":
    tests = [
        [[1, 5, 3], [2, 4, 7], 30],
        [[1, 4, 4, 2], [6, 3, 8, 2], 59],
        [[1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723],
        [[1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012],
        [[1, 1], [1, 2], 100],
        [
            generate_random_int_array(300_000, start_n=1, end_n=100_000),
            generate_random_int_array(300_000, start_n=1, end_n=10_000),
            10**14,
        ],
    ]
    answers = [3, 2, 294, 39354, 1, -1]

    tester = Tester(solution)
    tester.test(tests, answers)
