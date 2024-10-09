from tester import Tester
from typing import List

"""
1493. Longest Subarray of 1's After Deleting One Element
Medium

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
"""


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Started @ 17:15
        Ended @ 17:24
        Restarted @ 17:30
        Ended @ 17:34

        O(n) solution
        """
        cnt = 0
        cnt_left = 0
        max_cnt = 0
        zero_cnt = 0
        for num in nums + [0]:
            if num == 1:
                cnt += 1
            else:
                if (cnt_left + cnt) > max_cnt and cnt_left > 0:
                    max_cnt = cnt_left + cnt
                cnt_left = cnt
                cnt = 0
                zero_cnt += 1

        if max_cnt == 0 and cnt_left > 0:
            if zero_cnt > 1:
                return cnt_left
            return cnt_left - 1

        return max_cnt


if __name__ == "__main__":
    tests = [
        [[1, 1, 0, 1]],
        [[0, 1, 1, 1, 0, 1, 1, 0, 1]],
        [[1, 1, 1]],
        [[0, 0, 0]],
        [[0, 0, 1, 1]],
    ]
    answers = [3, 5, 2, 0, 2]

    tester = Tester(Solution().longestSubarray)
    tester.test(tests, answers)
