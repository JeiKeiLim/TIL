from tester import Tester

"""
튜브가 활동하는 코딩 동아리에서는 전통적으로 해오는 게임이 있다. 이 게임은 여러 사람이 둥글게 앉아서 숫자를 하나씩 차례대로 말하는 게임인데, 규칙은 다음과 같다.

- 숫자를 0부터 시작해서 차례대로 말한다. 첫 번째 사람은 0, 두 번째 사람은 1, … 열 번째 사람은 9를 말한다.
- 10 이상의 숫자부터는 한 자리씩 끊어서 말한다. 즉 열한 번째 사람은 10의 첫 자리인 1, 열두 번째 사람은 둘째 자리인 0을 말한다.

이진수, 16진수 등으로 확장하여 게임을 진행할 수 있다. 튜브가 말해야 하는 숫자 t개를 공백 없이 차례대로 나타낸 문자열을 구하라.

입력 형식
- 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
- 2 ≤ n ≤ 16
- 0 < t ≤ 1000
- 2 ≤ m ≤ 100
- 1 ≤ p ≤ m

출력 형식
튜브가 말해야 하는 숫자 t개를 공백 없이 차례대로 나타낸 문자열. 단, 10~15는 각각 대문자 A~F로 출력한다.

입출력 예
n   t   m   p   result
2   4   2   1   "0111"
16  16  2   1   "02468ACE11111111"
16  16  2   2   "13579BDF01234567"
"""


def solution(n: int, t: int, m: int, p: int) -> str:
    """
    Args:
        n: decimal
        t: number of me speaking
        m: number of people in the game
        p: number of my starting turn
    """
    dec_map = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }
    answer = ""

    i = 0
    n_str = []
    while i < m*t+1:
        num = i
        local_str = []
        while num >= n:
            rest = num % n
            local_str.append(dec_map[rest])
            num = num // n
        local_str.append(dec_map[num])
        n_str.extend(local_str[::-1])
        i += 1

    i = 0
    n_str = n_str[::-1]
    while len(answer) < t and n_str:
        i += 1
        now = n_str.pop()
        if (i-p) % m != 0 or i < p:
            continue
        answer += now

    return answer


if __name__ == "__main__":
    tests = [
        # Strictly extracted test cases from input examples as lists
        [2, 4, 2, 1],
        [16, 16, 2, 1],
        [16, 16, 2, 2],
        [15, 16, 2, 1],
        [15, 16, 3, 2],
        [7, 16, 9, 5],
        [10, 8, 10, 3],
        [2, 8, 10, 3],
        [8, 8, 5, 3],
    ]
    """
    0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20
    21, 22, 23, 24, 25, 26, 27, 30, 31, 32, 33, 34, 35, 36, 37
    40, 41, 42, 43, 44, 45, 46, 47, 50, 51, 52, 53, 54, 55, 56
    57, 60, 61, 62, 63, 64, 65, 66, 67, 70, 71, 72, 73, 74, 75
    """
    answers = [
        "0111",
        "02468ACE11111111",
        "13579BDF01234567",
        "02468ACE01234567",
        "147AD01316191C10",
        "4102244566111111",
        "21122334",
        "11111001",
        "27141126"
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
