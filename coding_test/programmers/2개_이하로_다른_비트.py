from tester import Tester

from typing import List

"""
2개 이하로 다른 비트

양의 정수 x에 대한 함수 f(x)를 다음과 같이 정의합니다.
 - x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수

예를 들어, 
 - f(2) = 3 입니다. 다음 표와 같이 2보다 큰 수들 중에서 비트가 다른 지점이 2개 이하이면서 제일 작은 수가 3이기 때문입니다.
   수   비트         다른 비트의 개수
   2    000...0010   
   3    000...0011    1


 - f(7) = 11 입니다. 다음 표와 같이 7보다 큰 수들 중에서 비트가 다른 지점이 2개 이하이면서 제일 작은 수가 11이기 때문입니다.
   수   비트         다른 비트의 개수
   7    000...0111
   8    000...1000    4
   9    000...1001    3
   10   000...1010    3
   11   000...1011    2

정수들이 담긴 배열 numbers가 매개변수로 주어집니다. numbers의 모든 수들에 대하여 각 수의 f 값을 배열에 차례대로 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
 - 1 ≤ numbers의 길이 ≤ 100,000
 - 0 ≤ numbers의 모든 수 ≤ 10^15

입출력 예
numbers      result
[2, 7]       [3, 11]
"""


def solution(numbers: List[int]) -> List[int]:
    answer = []
    for n in numbers:
        bin_arr = list(bin(n)[2:])
        bin_arr.insert(0, "0")
        for i in range(len(bin_arr) - 1, -1, -1):
            if bin_arr[i] == "0":
                bin_arr[i] = "1"
                if i < len(bin_arr) - 1:
                    bin_arr[i + 1] = "0"
                break
        answer.append(int("".join(bin_arr), 2))
    return answer


if __name__ == "__main__":
    tests = [
        [[2, 7]],
    ]
    answers = [[3, 11]]

    tester = Tester(solution)
    tester.test(tests, answers)
