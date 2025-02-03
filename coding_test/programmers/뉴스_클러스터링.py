from tester import Tester

"""
두 문자열 간 자카드 유사도를 계산하는 solution 함수를 작성하세요.

제한사항:
- 입력 문자열 길이: 2 이상 1000 이하
- 문자열을 두 글자씩 끊어서 다중집합을 생성
- 영문자만 유효, 대소문자 구분 없음
- 자카드 유사도를 65536을 곱한 후 정수로 반환

입출력 예:
str1           str2         answer
"FRANCE"       "french"     16384
"handshake"    "shake hands" 65536
"aa1+aa2"      "AAAA12"     43690
"E=M*C^2"      "e=m*c^2"    65536

aa1+aa2
AAAA12
"""


def solution(str1: str, str2: str) -> int:
    str1 = str1.lower()
    str2 = str2.lower()

    str1_map = {}
    for i in range(len(str1) - 1):
        key = str1[i : i + 2]
        if ord("a") <= ord(key[0]) <= ord("z") and ord("a") <= ord(key[1]) <= ord("z"):
            str1_map[key] = str1_map.get(key, 0) + 1
    str2_map = {}
    for i in range(len(str2) - 1):
        key = str2[i : i + 2]
        if ord("a") <= ord(key[0]) <= ord("z") and ord("a") <= ord(key[1]) <= ord("z"):
            str2_map[key] = str2_map.get(key, 0) + 1

    union = 0
    intersection = 0
    for key, val in str1_map.items():
        if key in str2_map:
            intersection += min(val, str2_map[key])
            union += max(val, str2_map[key])
        else:
            union += val
    for key, val in str2_map.items():
        if key not in str1_map:
            union += val

    if union == 0:
        return 65536
    iou = float(intersection) / float(union)

    return int(iou * 65536)


if __name__ == "__main__":
    tests = [
        ["FRANCE", "french"],
        ["handshake", "shake hands"],
        ["aa1+aa2", "AAAA12"],
        ["E=M*C^2", "e=m*c^2"],
    ]
    answers = [16384, 65536, 43690, 65536]

    tester = Tester(solution)
    tester.test(tests, answers)
