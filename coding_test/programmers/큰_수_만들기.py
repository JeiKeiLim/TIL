from tester import Tester, generate_random_string

"""
큰 수 만들기

어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다.
number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
 - number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
 - k는 1 이상 number의 자릿수 미만인 자연수입니다.

입출력 예
number         k     return
"1924"         2     "94"
"1231234"      3     "3234"
"4177252841"   4     "775841"

4177252841
k=4

77252841
k=2

1: [7]
2: [2,4]
5: [3]
4: [6]
7: [0, 1]
8: [5]
"""


def solution2(number: str, k: int) -> str:
    stack: list[str] = []
    to_remove = k

    for digit in number:
        while stack and to_remove and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    if to_remove:                 # same as `if to_remove > 0:`
        stack = stack[:-to_remove]

    return "".join(stack)


def solution(number: str, k: int) -> str:
    """Naive O(n^2)"""
    for _ in range(k, 0, -1):
        num_list = [number[:i] + number[i + 1 :] for i in range(len(number))]
        number = max(num_list)

    return number


if __name__ == "__main__":
    tests = [
        ["1924", 2],
        ["1942", 2],
        ["1231234", 3],
        ["4177252841", 4],
        ["2590533299", 3],
        ["6417376924", 3],
        ["4580866480", 4],
        [generate_random_string(10, start_char="0", end_char="9"), 4],
    ]
    answers = [
        "94",
        "94",
        "3234",
        "775841",
        "9533299",
        "7376924",
        "886680",
        solution(*tests[-1]),
    ]
    tester = Tester(solution2, verbose=1, incorrect_only=True)
    tester.test(tests, answers)
