from tester import Tester, generate_random_int_array

from typing import List

"""
You are given an array of integers nums.
Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

Example 1:
Input: nums = [1,4,3,3,2]
Output: 2
Explanation:
- The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
- The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
- Hence, we return 2.

Example 2:
Input: nums = [3,3,3,3]
Output: 1
Explanation:
- The strictly increasing subarrays of nums are [3], [3], [3], and [3].
- The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
- Hence, we return 1.

Example 3:
Input: nums = [3,2,1]
Output: 3
Explanation:
- The strictly increasing subarrays of nums are [3], [2], and [1].
- The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].
- Hence, we return 3.

Constraints:
1. 1 <= nums.length <= 50
2. 1 <= nums[i] <= 50
"""


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incr_n = 1
        decr_n = 1

        prev_num = nums[0]
        answer = 0

        for num in nums:
            if prev_num > num:
                incr_n += 1
            else:
                incr_n = 1
            if prev_num < num:
                decr_n += 1
            else:
                decr_n = 1

            answer = max(answer, incr_n, decr_n)
            prev_num = num
        return answer


if __name__ == "__main__":
    tests = [
        [[1, 4, 3, 3, 2]],
        [[3, 3, 3, 3]],
        [[3, 2, 1]],
        [generate_random_int_array(12 ** 6)]
    ]
    answers = [2, 1, 3, -1]

    tester = Tester(Solution().longestMonotonicSubarray, verbose=0)
    tester.test(tests, answers)
