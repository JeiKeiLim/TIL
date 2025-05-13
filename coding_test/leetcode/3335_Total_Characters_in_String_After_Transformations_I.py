from tester import Tester, generate_random_string

"""
You are given a string s and an integer t, representing the number of transformations to perform.
In one transformation, every character in s is replaced according to the following rules:
- If the character is 'z', replace it with the string "ab".
- Otherwise, replace it with the next character in the alphabet.

Return the length of the resulting string after exactly t transformations.
Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:
Input: s = "abcyy", t = 2
Output: 7

abcyy
bcdzz
cdeabab

25: 1
24: 1
23: 1
1: 2

Example 2:
Input: s = "azbk", t = 1
Output: 5

azbk
babcl

Constraints:
- 1 <= s.length <= 10^5
- s consists only of lowercase English letters.
- 1 <= t <= 10^5
"""


class Solution:
    def stringLengthAfterOperations2(self, s: str, t: int) -> int:
        s_map = [0] * 26
        for char in s:
            s_map[ord('z') - ord(char)] += 1

        for _ in range(t):
            nz = s_map.pop(0)
            s_map.append(0)
            s_map[-1] += nz
            s_map[-2] += nz

        answer = 0
        mod = 10**9 + 7
        for n in s_map:
            answer = (answer + n) % mod

        return answer
        
    def stringLengthAfterOperations(self, s: str, t: int) -> int:
        """Naive approach."""
        s_arr = list(s)
        for _ in range(t):
            b_locs = []
            for i in range(len(s_arr)):
                if s_arr[i] == 'z':
                    s_arr[i] = 'a'
                    b_locs.append(i+1+len(b_locs))
                    i += 1
                else:
                    s_arr[i] = chr(ord(s_arr[i]) + 1)
            for i in b_locs:
                s_arr.insert(i, 'b')
        return len(s_arr)


if __name__ == "__main__":
    tests = [
        ["abcyy", 2],
        ["azbk", 1],
        [generate_random_string(100_000), 100_000]
    ]
    answers = [
        7,
        5,
        # Solution().stringLengthAfterOperations(*tests[-1])
        -1
    ]

    tester = Tester(Solution().stringLengthAfterOperations2)
    tester.test(tests, answers)
