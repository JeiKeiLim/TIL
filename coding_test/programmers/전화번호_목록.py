from tester import Tester, generate_random_string
from typing import List

"""
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.

입력 형식:
- phone_book: 길이 1 이상 1,000,000 이하, 각 전화번호 길이는 1 이상 20 이하
- 중복 전화번호는 없음

출력 형식:
- 어떤 번호가 다른 번호의 접두어인 경우가 있으면 False, 그렇지 않으면 True

예시:
phone_book = ["119", "97674223", "1195524421"]
=> return False

119: 0, 2
976: 1

"""


def solution2(phone_book: List[str]) -> bool:
    phone_book.sort(key=lambda x: len(x))
    n = len(phone_book)
    si = len(phone_book[0])
    ei = len(phone_book[-1])

    for i in range(si, ei + 1):
        seen = set()
        for j in range(n):
            if phone_book[j][:i] in seen:
                return False
            seen.add(phone_book[j])

    return True


def solution(phone_book: List[str]) -> bool:
    phone_book.sort(key=lambda x: len(x))
    n = len(phone_book)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if phone_book[j].startswith(phone_book[i]):
                return False

    return True


if __name__ == "__main__":
    tests = [
        [["119", "97674223", "1195524421"]],
        [["123", "456", "789"]],
        [["12", "123", "1235", "567", "88"]],
        [
            [
                generate_random_string(10, 20, start_char="1", end_char="9")
                for _ in range(5000)
            ]
        ],
    ]
    answers = [False, True, False, True]

    tester = Tester(solution2, verbose=0)
    tester.test(tests, answers)
