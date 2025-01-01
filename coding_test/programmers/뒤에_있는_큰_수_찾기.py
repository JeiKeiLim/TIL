from tester import Tester

from typing import List

import heapq
import random

"""
정수로 이루어진 배열 numbers가 있습니다. 배열의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수라고 합니다.
정수 배열 numbers가 매개변수로 주어질 때, 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열을 return 하도록 solution 함수를 완성해주세요. 단, 뒷 큰수가 존재하지 않는 원소는 -1을 담습니다.

제한사항
4 ≤ numbers의 길이 ≤ 1,000,000
1 ≤ numbers[i] ≤ 1,000,000

입출력 예
numbers	            result
[2, 3, 3, 5]    	[3, 5, 5, -1]
[9, 1, 5, 3, 6, 2]	[-1, 5, 6, 6, -1, -1]
"""


def solution2(numbers: List[int]) -> List[int]:
    answer = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers)-1, -1, -1):
        while stack and stack[-1] <= numbers[i]:
            stack.pop()

        if stack:
            answer[i] = stack[-1]

        stack.append(numbers[i])

    return answer


def solution(numbers: List[int]) -> List[int]:
    """
    9, 1, 5, 3, 6, 2
    """
    answer = [-1] * len(numbers)

    i = 0
    while i < len(numbers):
        for j in range(i+1, len(numbers)):
            if numbers[j] > numbers[i]:
                answer[i] = numbers[j]
                break
        i += 1

    return answer


if __name__ == "__main__":
    tests = [
        # Strictly extracted test cases from input examples
        [[2, 3, 3, 5]],
        [[9, 1, 5, 3, 6, 2]],
        [[random.randint(1, 1000000) for _ in range(1000000)]],
    ]
    answers = [
        [3, 5, 5, -1],
        [-1, 5, 6, 6, -1, -1],
        [],
    ]

    tester = Tester(solution2, verbose=0)
    tester.test(tests, answers)
