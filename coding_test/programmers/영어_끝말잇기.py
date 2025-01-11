from tester import Tester

from typing import List

"""
끝말잇기에 참여하는 사람의 수 n과 사람들이 순서대로 말한 단어 words가 주어졌을 때, 가장 먼저 탈락하는 사람의 번호와 
그 사람이 자신의 몇 번째 차례에 탈락하는지를 구하세요.

제한 사항
- n은 2 이상 10 이하의 자연수입니다.
- words는 길이가 n 이상 100 이하인 배열입니다.
- 단어의 길이는 2 이상 50 이하입니다.
- 모든 단어는 알파벳 소문자로만 이루어져 있습니다.
- 정답은 [번호, 차례] 형태로 반환하며, 탈락자가 없으면 [0, 0]을 반환합니다.

입출력 예
n   words                                                                                       result
3   ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]               [3, 3]
5   ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", 
     "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]             [0, 0]
2   ["hello", "one", "even", "never", "now", "world", "draw"]                                  [1, 3]
"""


def solution(n: int, words: List[str]) -> List[int]:
    history = set([words[0]])

    for i in range(1, len(words)):
        player = (i % n) + 1
        turn = (i // n) + 1

        if words[i-1][-1] != words[i][0]:
            return [player, turn]

        if words[i] in history:
            return [player, turn]

        history.add(words[i])

    return [0, 0]


if __name__ == "__main__":
    tests = [
        [
            3,
            [
                "tank",
                "kick",
                "know",
                "wheel",
                "land",
                "dream",
                "mother",
                "robot",
                "tank",
            ],
        ],
        [
            5,
            [
                "hello",
                "observe",
                "effect",
                "take",
                "either",
                "recognize",
                "encourage",
                "ensure",
                "establish",
                "hang",
                "gather",
                "refer",
                "reference",
                "estimate",
                "executive",
            ],
        ],
        [2, ["hello", "one", "even", "never", "now", "world", "draw"]],
    ]
    answers = [
        [3, 3],
        [0, 0],
        [1, 3],
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
