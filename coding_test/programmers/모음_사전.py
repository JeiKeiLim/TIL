from tester import Tester

from typing import List

"""
사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다.
사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.

단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.

제한사항
- word의 길이는 1 이상 5 이하입니다.
- word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.

입출력 예
word       result
"AAAAE"    6
"AAAE"     10
"I"        1563
"EIO"      1189

 1: A
 2: AA
 3: AAA
 4: AAAA
 5: AAAAA
 6: AAAAE
 7: AAAAI
 8: AAAAO
 9: AAAAU
10: AAAE
11: AAAEA
12: AAAEE
13: AAAEI
14: AAAEO
15: AAAEU
16: AAAI
17: AAAIA
18: AAAIE
19: AAAII
20: AAAIO
21: AAAIU

입출력 예 설명
1. "AAAAE"는 사전에서 6번째 단어입니다.
2. "AAAE"는 사전에서 10번째 단어입니다.
3. "I"는 1563번째 단어입니다.
4. "EIO"는 1189번째 단어입니다.
"""

def solution2(word: str) -> int:
    """
    781, 156, 31, 6, 1
    A: 1
    AA: 2
    AAA: 3
    AAAA: 4
    AAAE: 4+6
    AAAI: 4+6+6
    AAAO: 4+6+6+6
    AAAU: 4+6+6+6+6
    AAE: 3+6*5+1 = 34
    AAI: 3+6*5*2+2 = 65
    AE: 2+31*5+1 = 158
    E: 1+156*5+1 = 782
    """
    word_n = [781, 156, 31, 6, 1]
    answer = 0
    for i, w in enumerate(word):
        answer += word_n[i] * "AEIOU".index(w) + 1
    return answer


def solution(word: str) -> int:
    """
    "AAAAE"    6
    "AAAE"     10
    "I"        1563
    "EIO"      1189
    """
    answer = 0

    for i, w in enumerate(word):
        answer += (5 ** (5 - i) - 1) // 4 * "AEIOU".index(w) + 1

    return answer


if __name__ == "__main__":
    tests = [
        # Strictly extracted test cases from input examples
        ["AAAAE"],
        ["AAAE"],
        ["I"],
        ["EIO"],
        ["AAAIU"],
        ["UUUUU"],
        ["E"]
    ]
    answers = [6, 10, 1563, 1189, 21, 3905, 1+156*5+1]

    tester = Tester(solution2)
    tester.test(tests, answers)
