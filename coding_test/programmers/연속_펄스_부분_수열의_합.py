from tester import Tester

from typing import List

import random

"""
어떤 수열의 연속 부분 수열에 같은 길이의 펄스 수열을 각 원소끼리 곱하여 연속 펄스 부분 수열을 만들려 합니다.
펄스 수열이란 [1, -1, 1, -1 …] 또는 [-1, 1, -1, 1 …] 과 같이 1 또는 -1로 시작하면서 1과 -1이 번갈아 나오는 수열입니다.

정수 수열 sequence가 매개변수로 주어질 때, 연속 펄스 부분 수열의 합 중 가장 큰 것을 return 하도록 solution 함수를 완성해주세요.

제한 사항
- 1 ≤ sequence의 길이 ≤ 500,000
- -100,000 ≤ sequence의 원소 ≤ 100,000
- sequence의 원소는 정수입니다.

입출력 예
sequence                   result
[2, 3, -6, 1, 3, -1, 2, 4] 10

입출력 예 설명
주어진 수열의 연속 부분 수열 [3, -6, 1]에 펄스 수열 [1, -1, 1]을 곱하여 
연속 펄스 부분 수열 [3, 6, 1]을 얻을 수 있고 그 합은 10으로서 가장 큽니다.
"""


def solution2(sequence: List[int]) -> int:
    """O(N) solution"""

    def get_max_subsequence_sum(seq: List[int]) -> int:
        answer = seq[0]
        seq_sum = seq[0]

        for i in range(1, len(seq)):
            seq_sum = max(seq[i], seq_sum + seq[i])
            answer = max(answer, seq_sum)

        return answer

    seq1 = [s if i % 2 == 0 else -s for i, s in enumerate(sequence)]
    seq2 = [-s for s in seq1]

    return max(get_max_subsequence_sum(seq1), get_max_subsequence_sum(seq2))


def solution(sequence: List[int]) -> int:
    answer = 0
    seq1 = [s if i % 2 == 0 else -s for i, s in enumerate(sequence)]
    seq2 = [s if i % 2 == 1 else -s for i, s in enumerate(sequence)]

    seq1_sum = sum(seq1)
    seq2_sum = sum(seq2)
    for i in range(len(sequence)):
        s1_sum = seq1_sum
        s2_sum = seq2_sum

        for j in range(len(sequence) - 1, i, -1):
            answer = max(answer, s1_sum, s2_sum)

            s1_sum -= seq1[j]
            s2_sum -= seq2[j]

        seq1_sum -= seq1[i]
        seq2_sum -= seq2[i]

    return answer


if __name__ == "__main__":
    tests = [
        [[2, 3, -6, 1, 3, -1, 2, 4]],
        [[random.randint(-100000, 100000) for _ in range(2000)]],
    ]
    answers = [10, solution(tests[-1][0])]

    tester = Tester(solution2, verbose=0)
    tester.test(tests, answers)
