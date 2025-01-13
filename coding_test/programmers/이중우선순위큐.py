from tester import Tester

from typing import List

import heapq

"""
이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조입니다.
1. "I 숫자": 큐에 숫자를 삽입합니다.
2. "D 1": 큐에서 최댓값을 삭제합니다.
3. "D -1": 큐에서 최솟값을 삭제합니다.

모든 연산을 처리한 후, 큐가 비어있으면 [0, 0], 비어있지 않으면 [최댓값, 최솟값]을 반환하세요.

제한사항
- operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.
- 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.

입출력 예
operations                                            result
["I 16", "I -5643", "D -1", "D 1", "D 1",
 "I 123", "D -1"]                                     [0, 0]

["I -45", "I 653", "D 1", "I -642", "I 45",
 "I 97", "D 1", "D -1", "I 333"]                      [333, -45]

n_min = 4
n_max = 3

D -1, D 1

45, 97, 333, 653
45, -45, -642

"""


def solution2(operations: List[str]) -> List[int]:
    queue = []
    for operation in operations:
        op, data = operation.split(" ")
        data = int(data)
        if op == "I":
            queue.append(data)
            queue.sort()
        elif data == -1 and len(queue) > 0:
            queue.pop(0)
        elif data == 1 and len(queue) > 0:
            queue.pop()
    if len(queue) == 0:
        return [0, 0]
    return [queue[-1], queue[0]]


def solution(operations: List[str]) -> List[int]:
    n = 0
    min_queue = []
    max_queue = []

    deleted = set()

    for operation in operations:
        op, data = operation.split(" ")
        data = int(data)
        if op == "I":
            heapq.heappush(max_queue, -data)
            heapq.heappush(min_queue, data)
            if data in deleted:
                deleted.remove(data)
            n += 1
        elif data == -1 and n > 0:
            del_candidate = heapq.heappop(min_queue)
            while del_candidate in deleted:
                del_candidate = heapq.heappop(min_queue)
            deleted.add(del_candidate)
            n -= 1
        elif data == 1 and n > 0:
            del_candidate = -heapq.heappop(max_queue)
            while del_candidate in deleted:
                del_candidate = -heapq.heappop(max_queue)
            deleted.add(del_candidate)
            n -= 1

        if n == 0:
            min_queue = []
            max_queue = []
            deleted = set()

    if n == 0:
        return [0, 0]

    min_val = heapq.heappop(min_queue)
    while min_val in deleted:
        min_val = heapq.heappop(min_queue)

    max_val = -heapq.heappop(max_queue)
    while max_val in deleted:
        max_val = -heapq.heappop(max_queue)

    return [max_val, min_val]


if __name__ == "__main__":
    tests = [
        [["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]],
        [["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]],
        [["I 10", "I 20", "D 1", "I 30", "I 40", "D -1", "D -1"]],
        [
            ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
            * 100000
        ],
    ]

    """
    n = 1
    deleted: 20 10 30

    40
    40 30 10
    """

    answers = [[0, 0], [333, -45], [40, 40], [333, -45]]

    tester = Tester(solution, verbose=0)
    tester.test(tests, answers)
