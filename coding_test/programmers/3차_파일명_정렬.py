from tester import Tester

from typing import List

"""
저장소 서버에는 프로그램의 과거 버전을 모두 담고 있어, 이름 순으로 정렬된 파일 목록은 보기가 불편했습니다. 파일명을 이름 순이 아닌, 포함된 숫자를 고려하여 정렬하는 방식으로 개선합니다.

파일명은 HEAD, NUMBER, TAIL 세 부분으로 구성됩니다.
• HEAD는 숫자가 아닌 문자로 이루어지며 최소 한 글자 이상입니다.
• NUMBER는 최대 5자리 숫자이며 앞에 0이 올 수 있습니다.
• TAIL은 남은 나머지 부분입니다.

정렬 기준:
• HEAD를 기준으로 사전 순으로 정렬(대소문자 구분 X)
• NUMBER는 숫자 크기 기준 정렬
• 둘 다 같을 경우, 입력 순서 유지

입출력 예:
입력: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

{
"img": [12, "img12.png"]
}

입력: ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

입력 형식
    입력으로 배열 files가 주어진다.
    files는 1000 개 이하의 파일명을 포함하는 문자열 배열이다.
    각 파일명은 100 글자 이하 길이로, 영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")만으로 이루어져 있다. 파일명은 영문자로 시작하며, 숫자를 하나 이상 포함하고 있다.
    중복된 파일명은 없으나, 대소문자나 숫자 앞부분의 0 차이가 있는 경우는 함께 주어질 수 있다. (muzi1.txt, MUZI1.txt, muzi001.txt, muzi1.TXT는 함께 입력으로 주어질 수 있다.)
"""

import re


def solution2(files: List[str]) -> List[str]:
    return sorted(
        files,
        key=lambda x: (
            x[: re.search("[0-9]+", x).start()].lower(),
            int(re.search("[0-9]+", x).group()),
        ),
    )


def solution(files: List[str]) -> List[str]:
    file_map = {}
    for file in files:
        num_match = re.search("([0-9]+)", file)
        num = int(num_match.group())
        head = file[: num_match.start()].lower()

        if head not in file_map:
            file_map[head] = [(num, file)]
        else:
            file_map[head].append((num, file))

    ordered_keys = sorted(file_map.keys())
    answer = []
    for key in ordered_keys:
        sorted_files = sorted(file_map[key], key=lambda x: x[0])
        answer.extend([x[1] for x in sorted_files])

    return answer


if __name__ == "__main__":
    tests = [
        [["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]],
        [
            [
                "F-5 Freedom Fighter",
                "B-50 Superfortress",
                "A-10 Thunderbolt II",
                "F-14 Tomcat",
            ]
        ],
    ]
    answers = [
        ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"],
        [
            "A-10 Thunderbolt II",
            "B-50 Superfortress",
            "F-5 Freedom Fighter",
            "F-14 Tomcat",
        ],
    ]

    tester = Tester(solution2)
    tester.test(tests, answers, exact_match=True)
