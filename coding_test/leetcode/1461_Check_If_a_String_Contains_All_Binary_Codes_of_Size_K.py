from tester import Tester, generate_random_string

"""
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s.
Otherwise, return false.

Example 1:
Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11".
They can be all found as substrings at indices 0, 1, 3, and 2 respectively.

Example 2:
Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as substrings.

Example 3:
Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array.

Constraints:
1. 1 <= s.length <= 5 * 10^5
2. s[i] is either '0' or '1'.
3. 1 <= k <= 20
"""


class Solution:
    def hasAllCodes2(self, s: str, k: int) -> bool:
        n = len(s)
        seen_subs = set()
        for i in range(k, n + 1):
            search_str = s[i - k : i]
            seen_subs.add(search_str)
        return len(seen_subs) == 2**k

    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        possible_subs = set()
        for i in range(2**k):
            possible_subs.add(bin(i)[2:].rjust(k, "0"))
        for i in range(k, n + 1):
            search_str = s[i - k : i]
            if search_str in possible_subs:
                possible_subs.remove(search_str)
        return len(possible_subs) == 0


if __name__ == "__main__":
    tests = [
        ["00110110", 2],
        ["0110", 1],
        ["0110", 2],
        [generate_random_string(5 * 10**5, start_char="0", end_char="1"), 20],
    ]
    answers = [True, True, False, False]

    tester = Tester(Solution().hasAllCodes2, verbose=0)
    tester.test(tests, answers)
