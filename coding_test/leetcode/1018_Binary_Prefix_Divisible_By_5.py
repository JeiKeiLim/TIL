from tester import Tester, generate_random_int_array

from typing import List

"""
You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is the subarray nums[0..i] 
(from most-significant-bit to least-significant-bit).
- For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.

Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

Example 1:
Input: nums = [0,1,1]
Output: [true,false,false]
Explanation:
- The input numbers in binary are: 
  - 0 => 0  (divisible by 5) -> true
  - 01 => 1 (not divisible by 5) -> false
  - 011 => 3 (not divisible by 5) -> false

Example 2:
Input: nums = [1,1,1]
Output: [false,false,false]

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
"""


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = 0
        answer = [False] * len(nums)
        for i in range(len(nums)):
            n = ((n << 1) + nums[i]) % 5

            if n == 0:
                answer[i] = True

        return answer


if __name__ == "__main__":
    tests = [
        [[0, 1, 1]],
        [[1, 1, 1]],
        [generate_random_int_array(10**5, end_n=1)]
    ]
    answers = [
        [True, False, False],
        [False, False, False],
        [False]
    ]

    tester = Tester(Solution().prefixesDivBy5)
    tester.test(tests, answers)
