from tester import Tester

"""
Given two strings s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2,
or vice-versa. In other words, s2 can break s1 or vice-versa.

A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.

Example 1:
Input: s1 = "abc", s2 = "xya"
Output: true
Explanation: "ayx" is a permutation of s2="xya" which can break string "abc" (a permutation of s1="abc").

Example 2:
Input: s1 = "abe", s2 = "acd"
Output: false
Explanation: All permutations for s1="abe" and s2="acd" show that no permutation from s1 can break s2 and vice-versa.

Example 3:
Input: s1 = "leetcodee", s2 = "interview"
Output: true

abcdefghijklmnopqrstuvwxyz

interview

e: 2
i: 2
n: 1
r: 1
t: 1
v: 1
w: 1

leetcodee

c: 1
d: 1
e: 4
l: 1
o: 1
t: 1

i = 4
j = 2

Constraints:
1. s1.length == n
2. s2.length == n
3. 1 <= n <= 10^5
4. All strings consist of lowercase English letters.
"""


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        ord_a = ord("a")
        s1_map = [0] * 26
        s2_map = [0] * 26

        for char1, char2 in zip(s1, s2):
            idx1 = ord(char1) - ord_a
            idx2 = ord(char2) - ord_a

            s1_map[idx1] += 1
            s2_map[idx2] += 1

        i = len(s1_map) - 1
        j = len(s2_map) - 1
        while s1_map[i] == s2_map[j]:
            i -= 1
            j -= 1

        if s1_map[i] < s2_map[j]:
            x_map, y_map = s2_map, s1_map
        else:
            x_map, y_map = s1_map, s2_map

        while i >= j and i >= 0 and j >= 0:
            min_val = min(x_map[i], y_map[j])
            x_map[i] -= min_val
            y_map[j] -= min_val

            if x_map[i] == 0:
                i -= 1
            if y_map[j] == 0:
                j -= 1

        return j == -1


if __name__ == "__main__":
    tests = [
        ["abc", "xya"],
        ["abe", "acd"],
        ["leetcodee", "interview"],
    ]
    answers = [True, False, True]

    tester = Tester(Solution().checkIfCanBreak)
    tester.test(tests, answers)
