from tester import Tester

"""
문제 설명
신입사원 어피치는 카카오톡으로 전송되는 메시지를 압축하여 전송 효율을 높이는 업무를 맡게 되었다. 메시지를 압축하더라도 전달되는 정보가 바뀌어서는 안 되므로, 압축 전의 정보를 완벽하게 복원 가능한 무손실 압축 알고리즘을 구현하기로 했다.
어피치는 여러 압축 알고리즘 중에서 성능이 좋고 구현이 간단한 LZW(Lempel–Ziv–Welch) 압축을 구현하기로 했다. LZW 압축은 1983년 발표된 알고리즘으로, 이미지 파일 포맷인 GIF 등 다양한 응용에서 사용되었다.
LZW 압축은 다음 과정을 거친다.
1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
5. 단계 2로 돌아간다.

압축 알고리즘이 영문 대문자만 처리한다고 할 때, 사전은 다음과 같이 초기화된다. 사전의 색인 번호는 정수값으로 주어지며, 1부터 시작한다고 하자.

색인 번호: 1 ~ 26
단어: A ~ Z

제한사항
- 입력 문자열은 대문자 A-Z로만 이루어져 있으며, 길이는 1 이상 1,000 이하입니다.

입출력 예
msg         result
"KAKAO"     [11, 1, 27, 15]
"TOBEORNOTTOBEORTOBEORNOT"   [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
"ABABABABABABABAB"           [1, 2, 27, 29, 28, 31, 30]
"""


def solution(msg: str) -> list:
    char_map = {chr(i): i-ord('A')+1 for i in range(ord('A'), ord('Z')+1)}
    queue = list(msg + "?")
    c_msg = ""
    answer = []
    while queue:
        char = queue.pop(0)
        if c_msg + char in char_map:
            c_msg += char
            continue
        answer.append(char_map[c_msg])
        char_map[c_msg + char] = len(char_map) + 1
        c_msg = char

    return answer



if __name__ == "__main__":
    tests = [
        ["KAKAO"],
        ["TOBEORNOTTOBEORTOBEORNOT"],
        ["ABABABABABABABAB"],
    ]
    answers = [
        [11, 1, 27, 15],
        [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34],
        [1, 2, 27, 29, 28, 31, 30],
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
