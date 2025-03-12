from tester import Tester, generate_random_string

"""
짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾고 제거하는 과정을 반복합니다.
문자열이 모두 제거된다면 1을, 그렇지 않다면 0을 반환합니다.

제한사항:
- 문자열의 길이 : 1,000,000 이하의 자연수
- 문자열은 모두 소문자로 이루어져 있습니다.

입출력 예:
s         result
"baabaa"  1
"cdcd"    0

"""


def solution2(s: str) -> int:
    queue = []
    n = len(s)
    for i in range(n):
        queue.append(s[i])

        while len(queue) > 1 and queue[-1] == queue[-2]:
            queue.pop()
            queue.pop()

    return 1 if len(queue) == 0 else 0


def solution(s: str) -> int:
    iter = 0
    while s != "":
        si = -1
        remove_candidate = []
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                if si < 0:
                    si = i - 1
                    remove_candidate.append([si, i + 1])
                else:
                    remove_candidate[-1][1] = i - 2
            else:
                si = -1

        if len(remove_candidate) == 0:
            return 0

        new_s = s[: remove_candidate[0][0]]
        for i in range(len(remove_candidate) - 1):
            si = remove_candidate[i][1]
            ei = remove_candidate[i + 1][0]
            new_s += s[si:ei]
        s = new_s
        iter += 1
        print(iter, len(s))

    return 1


if __name__ == "__main__":
    tests = [["baabaa"], ["cdcd"], [generate_random_string(1_000_000)]]
    answers = [1, 0, 0]

    tester = Tester(solution2, verbose=0)
    tester.test(tests, answers)
