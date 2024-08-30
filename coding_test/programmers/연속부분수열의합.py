from tester import Tester

from typing import List


def solution(sequence: List[int], k: int) -> List[int]:
    """

    Ex)
    [1, 2, 3, 4, 5], k=7
    Since 3+4=7, the start index is 2 and the end index is 3. Thus, return [2, 3]

    Args:
        sequence: Sequence numbers
        k: sum of the sequence to find. (5 <= k <= 10^9)

    Returns:
        indices of the start sequence index and the end sequence index
    """
    answer = [0, 0]
    final_answer = [0, 0]

    sum_of_candidate = 0
    min_length = len(sequence)

    for i, number in enumerate(sequence):
        sum_of_candidate += number
        answer[1] = i

        while sum_of_candidate > k:
            sum_of_candidate -= sequence[answer[0]]
            answer[0] += 1

        if sum_of_candidate == k:
            sequence_length = answer[1] - answer[0]
            if sequence_length < min_length:
                final_answer = [answer[0], answer[1]]
                min_length = sequence_length

    return final_answer


if __name__ == "__main__":
    tests = [
        [[1, 2, 3, 4, 5], 7],
        [[1, 1, 1, 2, 3, 4, 5], 5],
        [[2, 2, 2, 2, 2], 6],
    ]
    answers = [[2, 3], [6, 6], [0, 2]]

    tester = Tester(solution)
    tester.test(tests, answers)
