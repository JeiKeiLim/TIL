from tester import Tester, generate_random_int_array

from typing import List
from itertools import product

"""
You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers.
There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2
(every integer in nums1 is paired with every integer in nums2 exactly once).

Return the bitwise XOR of all integers in nums3.

Example 1:
Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
Output: 13
Explanation:
A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
The bitwise XOR of all these numbers is 13, so we return 13.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 0
Explanation:
All possible pairs of bitwise XORs are nums1[0] ^ nums2[0], nums1[0] ^ nums2[1], nums1[1] ^ nums2[0], and nums1[1] ^ nums2[1].
Thus, one possible nums3 array is [2,5,1,6].
2 ^ 5 ^ 1 ^ 6 = 0, so we return 0.

Constraints:
1. 1 <= nums1.length, nums2.length <= 10^5
2. 0 <= nums1[i], nums2[j] <= 10^9


1101
1001 -> 0100
0101 -> 0001
0011 -> 0010
"""


class Solution:
    def xorAllNums2(self, nums1: List[int], nums2: List[int]) -> int:
        xor_num = 0
        len1 = len(nums1)
        len2 = len(nums2)

        if len2 % 2 != 0:
            for n1 in nums1:
                xor_num ^= n1

        if len1 % 2 != 0:
            for n2 in nums2:
                xor_num ^= n2

        return xor_num

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor_num = 0
        for n1, n2 in product(nums1, nums2):
            xor_num ^= n1
            xor_num ^= n2
        return xor_num


if __name__ == "__main__":
    tests = [
        [[2, 1, 3], [10, 2, 5, 0]],
        [[1, 2], [3, 4]],
        [
            generate_random_int_array(100000, max_n=1000000, end_n=10**9),
            generate_random_int_array(100000, max_n=1000000, end_n=10**9),
        ],
    ]
    answers = [13, 0, -1]

    tester = Tester(Solution().xorAllNums2, verbose=0)
    tester.test(tests, answers)