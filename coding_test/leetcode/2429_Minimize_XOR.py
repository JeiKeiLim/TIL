from tester import Tester

"""
Given two positive integers num1 and num2, find the positive integer x such that:
1. x has the same number of set bits as num2, and
2. The value x XOR num1 is minimal.

Note:
- XOR is the bitwise XOR operation.
- The number of set bits of an integer is the number of 1's in its binary representation.

Return the integer x. The test cases are generated such that x is uniquely determined.

Example 1:
Input: num1 = 3, num2 = 5
Output: 3
Explanation:
- The binary representations of num1 and num2 are 0011 and 0101, respectively.
- The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.

Example 2:
Input: num1 = 1, num2 = 12
Output: 3
Explanation:
- The binary representations of num1 and num2 are 0001 and 1100, respectively.
- The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.

Constraints:
1. 1 <= num1, num2 <= 10^9
"""


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def to_bits(n: int) -> str:
            result = ""
            n_shift = 0
            while (n >> n_shift) > 0:
                result += str((n >> n_shift) % 2)
                n_shift += 1
            return result[::-1]

        bit1 = to_bits(num1)
        bit2 = to_bits(num2)

        n_bit2 = sum([int(char) for char in bit2])

        bit1_arr = [0] * (len(bit1) + len(bit2))
        for i in range(len(bit1)):
            if bit1[i] == "1":
                bit1_arr[len(bit1) - i - 1] = 1
                n_bit2 -= 1
            if n_bit2 == 0:
                break

        i = -1
        while n_bit2 > 0:
            i += 1
            if bit1_arr[i] == 1:
                continue
            bit1_arr[i] = 1
            n_bit2 -= 1

        answer = 0
        for n_shift, val in enumerate(bit1_arr):
            answer += val << n_shift
        return answer


if __name__ == "__main__":
    tests = [
        [3, 5],
        [1, 12],
        [4, 9],
        [4, 8],
        [189237217, 8123]
    ]
    answers = [3, 3, 5, 4, 189236992]

    tester = Tester(Solution().minimizeXor)
    tester.test(tests, answers)
