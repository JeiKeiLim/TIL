from tester import Tester

from typing import List

"""
You are given an integer array nums.

A subsequence sub of nums with length x is called valid if it satisfies:
(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.

Return the length of the longest valid subsequence of nums.

A subsequence is an array that can be derived from another array by deleting some or no elements 
without changing the order of the remaining elements.

Example 1:

Input: nums = [1,2,3,4]
Output: 4
Explanation: The longest valid subsequence is [1, 2, 3, 4].

Example 2:

Input: nums = [1,2,1,1,2,1,2]
Output: 6
Explanation: The longest valid subsequence is [1, 2, 1, 2, 1, 2].

Example 3:

Input: nums = [1,3]
Output: 2
Explanation: The longest valid subsequence is [1, 3].

Constraints:
2 <= nums.length <= 2 * 10^5
1 <= nums[i] <= 10^7
"""


class Solution:
    def maxValidSubsequence(self, nums: List[int]) -> int:
        """
        Odd + Odd = Even
        Odd + Even = Odd
        Even + Odd = Odd
        Even + Even = Even
        """
        n_odd = 0
        n_even_even = 0
        n_even_odd = 0

        last_odd_even = nums[0] % 2 == 0
        if last_odd_even:
            n_even_even = 1
        else:
            n_even_odd = 1

        for i in range(1, len(nums)):
            is_odd = nums[i] % 2 == 1

            if is_odd:
                n_even_odd += 1
            else:
                n_even_even += 1

            if last_odd_even and is_odd:
                last_odd_even = not is_odd
                n_odd += 1
            elif not last_odd_even and not is_odd:
                last_odd_even = not is_odd
                n_odd += 1

        return max(n_odd + 1, max(n_even_even, n_even_odd))


if __name__ == "__main__":
    tests = [
        [[1, 2, 3, 4]],
        [[1, 2, 1, 1, 2, 1, 2]],
        [[1, 3]],
        [[4, 51, 68]],
        [[1, 5, 9, 4, 2]],
        [[2, 39, 23]],
    ]
    answers = [4, 6, 2, 3, 3, 2]

    tester = Tester(Solution().maxValidSubsequence)
    tester.test(tests, answers)
