from tester import Tester

from typing import List

"""
다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.
1. (), [], {} 는 모두 올바른 괄호 문자열입니다.
2. 만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다.
3. 만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다.

대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다.
이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
- s의 길이는 1 이상 1,000 이하입니다.

입출력 예
s          result
"[](){}"    3
"}]()[{"    2
"[)(]"      0
"}}}"       0
"""


def solution(s: str) -> int:
    closer_map = {
        "[": "]",
        "{": "}",
        "(": ")",
    }
    answer = 0
    for _ in range(len(s)):
        stack = []

        is_good = True
        for char in s:
            if char in closer_map:
                stack.append(closer_map[char])
            elif stack and char != stack[-1] or not stack:
                is_good = False
                break
            else:
                stack.pop()

        s = s[1:] + s[0]
        if is_good and len(stack) == 0:
            answer += 1

    return answer


if __name__ == "__main__":
    tests = [
        # Strictly extracted test cases from input examples
        ["[](){}"],
        ["}]()[{"],
        ["[)(]"],
        ["}}}"],
        ["{(})"]
    ]
    answers = [3, 2, 0, 0, 0]

    tester = Tester(solution)
    tester.test(tests, answers)
