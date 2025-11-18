from tester import Tester, generate_random_int_array

from typing import List

"""
We have two special characters:
- The first character can be represented by one bit 0.
- The second character can be represented by two bits (10 or 11).

Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

Example 1:
Input: bits = [1,0,0]
Output: true
Explanation:
- The only way to decode it is: [1,0] => 2-bit character, then [0] => 1-bit character.
- So the last character is one-bit.

Example 2:
Input: bits = [1,1,1,0]
Output: false
Explanation:
- The only way to decode it is: [1,1] => 2-bit character, [1,0] => 2-bit character.
- So the last character is not one-bit.


10101101010011011010

10 10 11 0 10 10 0 11 0 11 0 10

Constraints:
- 1 <= bits.length <= 1000
- bits[i] is either 0 or 1.
"""


class Solution:
    def isOneBitCharacter2(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        while i < n - 1:
            i += 1 + (bits[i] == 1)
        return i == n - 1

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        was_one = False
        one_bit = True
        for bit in bits:
            if was_one:
                was_one = False
                one_bit = False
                continue
            was_one = bit == 1
            one_bit = True
        return one_bit


if __name__ == "__main__":
    tests = [
        [[1, 0, 0]],
        [[1, 1, 1, 0]],
        [[1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0]],
        [generate_random_int_array(100_000, end_n=1)],
    ]
    answers = [True, False, False, False]

    tester = Tester(Solution().isOneBitCharacter)
    tester.test(tests, answers)
