from tester import Tester

from typing import List

from collections import deque

import heapq

"""
운영체제의 역할 중 하나는 컴퓨터 시스템의 자원을 효율적으로 관리하는 것입니다. 이 문제에서는 운영체제가 다음 규칙에 따라 프로세스를 관리할 경우 특정 프로세스가 몇 번째로 실행되는지 알아내면 됩니다.

1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.

제한사항
- priorities의 길이는 1 이상 100 이하입니다.
- priorities의 원소는 1 이상 9 이하의 정수입니다.
- location은 0 이상 (대기 큐에 있는 프로세스 수 - 1) 이하의 값을 가집니다.

입출력 예
priorities             location      return
[2, 1, 3, 2]           2             1
[1, 1, 9, 1, 1, 1]     0             5

1: 1
2: 0, 3
3: 2
4:
5:
6:
7:
8:
9:

"""


def solution2(priorities: List[int], location: int) -> int:
    processes = deque([(priority, i) for i, priority in enumerate(priorities)])
    n_step = 0
    while processes:
        max_priority = max(processes, key=lambda x: x[0])[0]
        while max_priority in [priority for priority, _ in processes]:
            while processes[0][0] != max_priority:
                processes.append(processes.popleft())

            _, loc = processes.popleft()
            n_step += 1
            if loc == location:
                return n_step
    return -1


def solution(priorities: List[int], location: int) -> int:
    priority_que = [[] for _ in range(10)]
    possible_priorities = []

    for i, priority in enumerate(priorities):
        priority_que[priority].append(i)
        heapq.heappush(possible_priorities, -priority)

    n = len(priorities)
    n_step = 0
    next_idx = 0
    max_priority = -heapq.heappop(possible_priorities)
    for idx in priority_que[max_priority]:
        n_step += 1
        if idx == location:
            return n_step
        next_idx = (idx + 1) % n

    while possible_priorities:
        max_priority = -heapq.heappop(possible_priorities)
        while priority_que[max_priority]:
            if next_idx in priority_que[max_priority]:
                n_step += 1
                if next_idx == location:
                    return n_step
                priority_que[max_priority].remove(next_idx)
            next_idx = (next_idx + 1) % n
    return -1


if __name__ == "__main__":
    tests = [[[2, 1, 3, 2], 2], [[1, 1, 9, 1, 1, 1], 0], [[1, 2, 2, 4, 2, 1, 1, 2], 2]]
    answers = [1, 5, 5]

    tester = Tester(solution2)
    tester.test(tests, answers)
