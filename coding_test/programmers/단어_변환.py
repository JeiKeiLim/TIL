from tester import Tester

from typing import List

"""
두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.

제한사항
- 각 단어는 알파벳 소문자로만 이루어져 있습니다.
- 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
- words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
- begin과 target은 같지 않습니다.
- 변환할 수 없는 경우에는 0을 return 합니다.

입출력 예
begin   target  words                                   return
"hit"   "cog"   ["hot", "dot", "dog", "lot", "log", "cog"]  4
"hit"   "cog"   ["hot", "dot", "dog", "lot", "log"]         0
"""


def solution(begin: str, target: str, words: List[str]) -> int:
    """
    hit -> hot
    hot -> dot, lot
    dog -> dot, log, cog
    lot -> dot, hot,
    cog -> dog, log, dot
    """
    conv_map = {}
    for word1 in words + [begin]:
        for word2 in words:
            if word1 == word2:
                continue
            n_diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    n_diff += 1
                if n_diff > 1:
                    break
            if n_diff == 1:
                conv_map[word1] = conv_map.get(word1, []) + [word2]

    answer = 2**31
    if begin not in conv_map:
        return 0
    stack = [(word, 1) for word in conv_map[begin]]
    visited = set()

    while stack:
        word, step = stack.pop()

        if step >= answer or word in visited:
            continue

        if word == target:
            answer = min(answer, step)

        visited.add(word)
        if word in conv_map:
            stack.extend([(word, step + 1) for word in conv_map[word]])

    return answer if answer < 2**31 else 0


if __name__ == "__main__":
    tests = [
        ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]],
        ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]],
        ["awesome", "foreign", ["aowesome", "fwesome", "fowesome"]],
    ]
    answers = [4, 0, 0]

    tester = Tester(solution)
    tester.test(tests, answers)
