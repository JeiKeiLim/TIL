from tester import Tester, generate_random_int_array

from typing import List

"""
두 큐 합 같게 만들기

길이가 같은 두 개의 큐가 주어집니다. 하나의 큐를 골라 원소를 추출(pop)하고, 추출된 원소를 다른 큐에 집어넣는(insert) 작업을 통해 각 큐의 원소 합이 같도록 만들려고 합니다. 이때 필요한 작업의 최소 횟수를 구하고자 합니다. 한 번의 pop과 한 번의 insert를 합쳐서 작업을 1회 수행한 것으로 간주합니다.

큐는 먼저 집어넣은 원소가 먼저 나오는 구조입니다. 이 문제에서는 큐를 배열로 표현하며, 원소가 배열 앞쪽에 있을수록 먼저 집어넣은 원소임을 의미합니다. 즉, pop을 하면 배열의 첫 번째 원소가 추출되며, insert를 하면 배열의 끝에 원소가 추가됩니다.

제한사항
 - 1 ≤ queue1의 길이 = queue2의 길이 ≤ 300,000
 - 1 ≤ queue1의 원소, queue2의 원소 ≤ 10^9
 - 언어에 따라 산술 오버플로우 발생 가능성 있음

입출력 예
queue1              queue2              result
[3, 2, 7, 2]        [4, 6, 5, 1]         2
[1, 2, 1, 2]        [1, 10, 1, 2]        7
[1, 1]              [1, 5]              -1

[3,2,7,2]: 14, [4,6,5,1]: 16
[3,2,7,2,4]: 18, [6,5,1]: 12
[2,7,2,4]: 15, [6,5,1,3]: 15
"""

from collections import deque


def solution(queue1: List[int], queue2: List[int]) -> int:
    q1 = deque(queue1)
    q2 = deque(queue2)

    max_op = (len(q1) + len(q2)) * 2
    answer = 0

    sum1 = sum(q1)
    sum2 = sum(q2)

    for _ in range(max_op):
        if sum1 == sum2:
            return answer

        if sum1 > sum2:
            n = q1.popleft()
            sum1 -= n
            sum2 += n
            q2.append(n)
        else:
            n = q2.popleft()
            sum1 += n
            sum2 -= n
            q1.append(n)
        answer += 1

    return -1


if __name__ == "__main__":
    tests = [
        [[1, 1, 1, 1], [1, 1, 7, 1]],
        [[1, 1], [1, 5]],
        [[3, 2, 7, 2], [4, 6, 5, 1]],
        [[1, 2, 1, 2], [1, 10, 1, 2]],
        [
            generate_random_int_array(30_000, start_n=1, end_n=10**9),
            generate_random_int_array(30_000, start_n=1, end_n=10**9),
        ],
    ]
    answers = [9, -1, 2, 7, -1, -1]

    tester = Tester(solution)
    tester.test(tests, answers)
