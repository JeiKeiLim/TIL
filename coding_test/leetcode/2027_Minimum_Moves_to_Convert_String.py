from tester import Tester

"""
You are given a string s consisting of n characters which are either 'X' or 'O'.

A move is defined as selecting three consecutive characters of s and converting them to 'O'. Note that if a move is applied to the character 'O', it will stay the same.

Return the minimum number of moves required so that all the characters of s are converted to 'O'.

Example 1:
Input: s = "XXX"
Output: 1

Example 2:
Input: s = "XXOX"
Output: 2

Example 3:
Input: s = "OOOO"
Output: 0

Constraints:
3 <= s.length <= 1000
s[i] is either 'X' or 'O'.
"""


class Solution:
    def minimumMoves(self, s: str) -> int:
        """
        Started @ 19:43
        Ended @ 19:54
        """
        cnt = 0
        i = 0
        while i < len(s):
            if s[i] == "X":
                i += 3
                cnt += 1
            else:
                i += 1

        return cnt


if __name__ == "__main__":
    tests = [["XXX"], ["XXOX"], ["OOOO"], ["OXOX"], ["OXXOX"], ["OOOOXXXOXO"]]
    answers = [1, 2, 0, 1, 2, 2]

    tester = Tester(Solution().minimumMoves)
    tester.test(tests, answers)
