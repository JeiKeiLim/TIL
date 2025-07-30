from tester import Tester, generate_random_int_array

from typing import List

"""
You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

Let k be the maximum value of the bitwise AND of any subarray of nums.
Only consider subarrays with bitwise AND equal to k.
Return the length of the longest such subarray.

The bitwise AND of an array is the AND of all the numbers in it.
A subarray is a contiguous sequence of elements within an array.

Example 1:
Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation: Max AND is 3. Longest subarray with AND 3 is [3,3].

Example 2:
Input: nums = [1,2,3,4]
Output: 1
Explanation: Max AND is 4. Longest subarray with AND 4 is [4].

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_and = max(nums)
        answer = 0
        cnt = 0
        for n in nums:
            if n == max_and:
                cnt += 1
            else:
                answer = max(cnt, answer)
                cnt = 0
        answer = max(cnt, answer)
        return answer


if __name__ == "__main__":
    tests = [
        [[1, 2, 3, 3, 2, 2]],
        [[1, 2, 3, 4]],
        [generate_random_int_array(10**5, start_n=1, end_n=10**6)]
    ]
    answers = [2, 1, -1]

    tester = Tester(Solution().longestSubarray)
    tester.test(tests, answers)
