from tester import Tester, generate_random_string

"""
Given a binary string s, return the number of substrings with all characters 1's. 
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: s = "0110111"
Output: 9
Explanation:
- "1" appears 5 times.
- "11" appears 3 times.
- "111" appears 1 time.
- Total substrings with only '1's = 5 + 3 + 1 = 9

Example 2:
Input: s = "101"
Output: 2
Explanation:
- "1" appears 2 times.

Example 3:
Input: s = "111111"
Output: 21
Explanation:
- All possible substrings are made of 1's:
  6 single "1"s, 5 "11", 4 "111", 3 "1111", 2 "11111", 1 "111111"
  => 6 + 5 + 4 + 3 + 2 + 1 = 21

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either '0' or '1'.
"""


class Solution:
    def numSub2(self, s: str) -> int:
        answer = 0
        MOD = 10**9 + 7
        ones = [one for one in s.split("0") if len(one) > 0]
        for one in ones:
            n = len(one)
            answer = (answer + (((n + 1) * n) // 2)) % MOD
        return answer

    def numSub(self, s: str) -> int:
        answer = 0
        sub_cnt = 0
        MOD = 10**9 + 7
        n = len(s)
        for i in range(n):
            if s[i] == "1":
                sub_cnt += 1
                answer = (answer + sub_cnt) % MOD
            else:
                sub_cnt = 0
        return answer


if __name__ == "__main__":
    tests = [
        ["0110111"],
        ["101"],
        ["111111"],
        [generate_random_string(10**5, start_char="0", end_char="1")],
    ]
    answers = [9, 2, 21, Solution().numSub(*tests[-1])]

    tester = Tester(Solution().numSub2)
    tester.test(tests, answers)
