from tester import Tester

"""
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3^x.

Example 1:
Input: n = 12
Output: true
Explanation: 12 = 3^1 + 3^2

Example 2:
Input: n = 91
Output: true
Explanation: 91 = 3^0 + 3^2 + 3^4

Example 3:
Input: n = 21
Output: False

0: 1
1: 3
2: 9
3: 27
4: 81

Constraints:
1. 1 <= n <= 10^7
"""


class Solution:
    def checkPowersOfThree2(self, n: int) -> bool:
        possible_sets = []
        power = 0
        while 3**power <= n:
            possible_sets.append(3**power)
            power += 1

        num = 0
        while possible_sets:
            power = possible_sets.pop()
            if num + power < n:
                num += power
            elif num + power > n:
                continue
            else:
                return True

        return False

    def checkPowersOfThree(self, n: int) -> bool:
        possible_sets = []
        power = 0
        while 3**power <= n:
            possible_sets.append(3**power)
            power += 1

        queue = [(possible_sets[-1], possible_sets[:-1].copy())]
        seen = set()
        while queue:
            num, current_set = queue.pop()

            if num in seen:
                continue
            seen.add(num)

            if num == n:
                return True

            for i in range(len(current_set)):
                next_set = current_set.copy()
                next_n = num + next_set.pop(i)
                queue.append((next_n, next_set))

        return False


if __name__ == "__main__":
    tests = [
        [12],
        [91],
        [21],
        [10**7],
    ]
    answers = [True, True, False, False]

    tester = Tester(Solution().checkPowersOfThree2)
    tester.test(tests, answers)
