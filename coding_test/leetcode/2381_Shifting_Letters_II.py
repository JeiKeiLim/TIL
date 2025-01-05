from tester import Tester

from typing import List
import heapq

import random

"""
You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni].
For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1,
or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a').
Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.

Example 1:
Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation:
1. Shift the characters from index 0 to index 1 backward. Now s = "zac" <- abc.
2. Shift the characters from index 1 to index 2 forward. Now s = "zbd" <- zac.
3. Shift the characters from index 0 to index 2 forward. Now s = "ace" <- zbd.

Example 2:
Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
Output: "catz"
Explanation:
1. Shift the characters from index 0 to index 0 backward. Now s = "cztz".
2. Shift the characters from index 1 to index 1 forward. Now s = "catz".

Constraints:
1. 1 <= s.length, shifts.length <= 5 * 10^4
2. shifts[i].length == 3
3. 0 <= starti <= endi < s.length
4. 0 <= directioni <= 1
5. s consists of lowercase English letters.
"""


class Solution:
    def shiftingLetters4(self, s: str, shifts: List[List[int]]) -> str:
        dis = [0] * (len(s) + 1)
        for i in range(len(shifts)):  # O (m)
            di = (shifts[i][2] * 2) - 1

            dis[shifts[i][0]] += di
            dis[shifts[i][1] + 1] -= di

        prefix = 0
        ord_a = ord("a")
        ss = [ord(s[i]) - ord_a for i in range(len(s))]  # O (n)
        for i in range(len(ss)):  # O (n)
            prefix += dis[i]
            ss[i] = (ss[i] + prefix) % 26

        return "".join([chr(ord_a + ss[i]) for i in range(len(ss))])

    def shiftingLetters3(self, s: str, shifts: List[List[int]]) -> str:
        for i in range(len(shifts)):
            shifts[i][2] = -1 if shifts[i][2] == 0 else 1

        shifts.sort(reverse=True)  # O(m log m)
        stack = []
        prefix = 0

        ord_a = ord("a")
        ss = [ord(s[i]) - ord_a for i in range(len(s))]
        for i in range(len(s)):  # O (n)
            while shifts and shifts[-1][0] <= i:  # O (m)
                shift = shifts.pop()
                prefix += shift[2]
                heapq.heappush(stack, (shift[1], shift[2]))  # O (log m)

            ss[i] = (ss[i] + prefix) % 26
            while stack and stack[0][0] <= i:  # O (m)
                shift = heapq.heappop(stack)  # O(log m)
                prefix -= shift[1]
        return "".join([chr(ord_a + ss[i]) for i in range(len(ss))])

    def shiftingLetters2(self, s: str, shifts: List[List[int]]) -> str:
        dis = [0] * len(s)

        shift_up = [shift[:2] for shift in shifts if shift[2] == 1]
        shift_down = [shift[:2] for shift in shifts if shift[2] == 0]

        for si, ei in shift_up:
            for i in range(si, ei + 1):
                dis[i] += 1

        for si, ei in shift_down:
            for i in range(si, ei + 1):
                dis[i] -= 1

        ord_a = ord("a")
        ss = [ord(s[i]) - ord_a for i in range(len(s))]
        for i in range(len(ss)):
            ss[i] = (ss[i] + dis[i]) % 26

        return "".join([chr(ord_a + ss[i]) for i in range(len(ss))])

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        """
        Naive approach
        """
        ord_a = ord("a")
        ss = [ord(s[i]) - ord_a for i in range(len(s))]
        for si, ei, di in shifts:
            di = -1 if di == 0 else 1
            for i in range(si, ei + 1):
                ss[i] = (ss[i] + di) % 26

        return "".join([chr(ord_a + ss[i]) for i in range(len(ss))])


if __name__ == "__main__":
    tests = [
        ["abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]]],
        ["dztz", [[0, 0, 0], [1, 1, 1]]],
        [
            "".join([chr(random.randint(ord("a"), ord("z"))) for _ in range(10**4)]),
            [
                [
                    random.randint(0, 1000),
                    random.randint(1001, 10**4 - 1),
                    random.randint(0, 1),
                ]
                for _ in range(10**4)
            ],
        ],
    ]
    answers = ["ace", "catz", ""]

    tester = Tester(Solution().shiftingLetters4, verbose=0)
    tester.test(tests, answers)
