from tester import Tester

"""
올바른 괄호란 (())나 ()와 같이 올바르게 모두 닫힌 괄호를 의미합니다. )(나 ())() 와 같은 괄호는 올바르지 않은 괄호가 됩니다. 괄호 쌍의 개수 n이 주어질 때, n개의 괄호 쌍으로 만들 수 있는 모든 가능한 괄호 문자열의 갯수를 반환하는 함수 solution을 완성해 주세요.

제한사항
- 괄호 쌍의 개수 N : 1 ≤ n ≤ 14, N은 정수

입출력 예
n   result
2   2
3   5

입출력 예 설명
입출력 예 #1
2개의 괄호쌍으로 [ "(())", "()()" ]의 2가지를 만들 수 있습니다.
입출력 예 #2
3개의 괄호쌍으로 [ "((()))", "(()())", "(())()", "()(())", "()()()" ]의 5가지를 만들 수 있습니다.
"""


def solution2(n: int) -> int:
    stack = [(0, 0)]
    answer = 0
    while stack:
        pos, neg = stack.pop()

        if pos+1 <= n:
            stack.append((pos+1, neg))
        if pos-(neg+1) >= 0:
            stack.append((pos, neg+1))
        if pos == n and neg == n:
            answer += 1

    return answer


def solution(n: int) -> int:
    """
    1 1 1 -1 -1 -1
    """
    answer = 0
    arr = [1] * n
    arr += [-1] * n

    stack = [(arr)]
    visited = set()
    while stack:
        arr = stack.pop()
        if tuple(arr) in visited:
            continue
        is_good = True
        n_sum = 0
        for m in arr:
            n_sum += m
            if n_sum < 0:
                is_good = False
                break

        visited.add(tuple(arr))
        if is_good and n_sum == 0:
            answer += 1

        for i in range(len(arr)):
            new_arr = arr.copy()
            new_arr[i] *= -1
            stack.append(new_arr)

    return answer


if __name__ == "__main__":
    tests = [[2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14]]
    answers = [2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440]

    tester = Tester(solution2)
    tester.test(tests, answers)
