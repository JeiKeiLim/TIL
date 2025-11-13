from tester import Tester, generate_random_string

"""
You are given a binary string s.

You can perform the following operation on the string any number of times:
- Choose any index i from the string where i + 1 < s.length such that s[i] == '1' and s[i + 1] == '0'.
- Move the character s[i] to the right until it reaches the end of the string or another '1'. For example, for s = "010010", if we choose i = 1, the resulting string will be s = "000110".

Return the maximum number of operations that you can perform.

Example 1:
Input: s = "1001101"
Output: 4
Explanation:
- Choose index i = 0. The resulting string is s = "0011101".
- Choose index i = 4. The resulting string is s = "0011011".
- Choose index i = 3. The resulting string is s = "0010111".
- Choose index i = 2. The resulting string is s = "0001111".


Example 2:
Input: s = "00111"
Output: 0

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either '0' or '1'.
"""

from collections import deque
import re


class Solution:
    def maxOperations3(self, s: str) -> int:
        s = re.sub("0+", "0", s)
        n = len(s)
        answer = 0
        sub_cnt = 0
        for i in range(n):
            if s[i] == '0':
                answer += sub_cnt
            else:
                sub_cnt += 1
        return answer

    def maxOperations2(self, s: str) -> int:
        answer = 0
        sub_cnt = int(s[0])
        for i in range(1, len(s)):
            if s[i-1] > "0" and s[i] == "0":
                answer += sub_cnt
            elif s[i] == "1":
                sub_cnt += 1

        return answer

    def maxOperations(self, s: str) -> int:
        """Naive"""
        n_one = s.count("1")
        s_arr = deque([int(s[0])])
        for i in range(1, len(s)):
            if s_arr[-1] == 0 and s[i] == "0":
                continue
            if s_arr[-1] > 0 and s[i] == "1":
                s_arr[-1] = int(s_arr[-1]) + 1
                continue
            s_arr.append(int(s[i]))

        while s_arr and s_arr[0] == 0:
            s_arr.popleft()

        answer = 0
        while s_arr and s_arr[-1] < n_one:
            num = s_arr.popleft()
            if s_arr[0] == 0:
                s_arr.popleft()
            if not s_arr:
                s_arr.append(num)
            else:
                s_arr[0] += num
            answer += num

            while s_arr[0] == 0:
                s_arr.popleft()
        return answer


if __name__ == "__main__":
    tests = [
        ["1001101"],
        ["10011010"],
        ["00111"],
        ["0"],
        ["10"],
        [generate_random_string(10**5, start_char="0", end_char="1")],
    ]
    answers = [4, 8, 0, 0, 1, Solution().maxOperations(*tests[-1])]

    tester = Tester(Solution().maxOperations3)
    tester.test(tests, answers)
