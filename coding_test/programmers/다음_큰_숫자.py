from tester import Tester

"""
자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

제한사항
- n은 1,000,000 이하의 자연수입니다.

입출력 예
n    result
78   83
15   23
"""


def solution(n: int) -> int:
    binary_n = bin(n)[2:]
    n_ones = 0
    n_zeros = 0
    swap_idx = -1
    for i in range(len(binary_n) - 1, 0, -1):
        if binary_n[i] == "1" and binary_n[i - 1] == "0":
            swap_idx = i
            break
        elif binary_n[i] == "1":
            n_ones += 1
        elif binary_n[i] == "0":
            n_zeros += 1

    binary_list = [1] * n_ones
    binary_list += [0] * n_zeros
    binary_list.extend([0, 1])
    if swap_idx > -1:
        for i in range(swap_idx - 2, -1, -1):
            binary_list.append(int(binary_n[i]))

    answer = 0
    for i in range(len(binary_list)):
        answer += binary_list[i] << i

    return answer


if __name__ == "__main__":
    tests = [
        [78],
        [15],
    ]
    answers = [
        83,
        23,
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
