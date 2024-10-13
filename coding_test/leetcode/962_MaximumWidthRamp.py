from tester import Tester  # Assuming you have a Tester class for running tests

from typing import List

"""
962. Maximum Width Ramp
Medium

A ramp in an integer array `nums` is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is `j - i`.

Given an integer array `nums`, return the maximum width of a ramp in `nums`. If there is no ramp in `nums`, return 0.

### Example 1:
Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.

### Example 2:
Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.

### Constraints:
- 2 <= nums.length <= 5 * 10^4
- 0 <= nums[i] <= 5 * 10^4
"""


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        """O(n^2)"""
        max_ramp_width = 0

        for i in range(len(nums) - 1):
            if max_ramp_width > (len(nums) - i - 1):
                break

            for j in range(len(nums) - 1, i, -1):
                if nums[i] <= nums[j]:
                    ramp_width = j - i

                    if ramp_width > max_ramp_width:
                        max_ramp_width = ramp_width
                        break

        return max_ramp_width


class Solution2:
    def maxWidthRamp(self, nums: List[int]) -> int:
        """
        O(n log n)
        """
        sorted_idx = [i[0] for i in sorted(enumerate(nums), key=lambda x: x[1])]
        min_idx = len(nums)
        max_width = 0

        for i in range(len(nums)):
            min_idx = min(sorted_idx[i], min_idx)
            max_width = max(sorted_idx[i] - min_idx, max_width)

        return max_width


if __name__ == "__main__":
    # Test cases
    tests = [
        [[6, 0, 8, 2, 1, 5]],  # Example 1
        [[9, 8, 1, 0, 1, 9, 4, 0, 4, 1]],  # Example 2
        [[6, 7, 8, 8, 6, 5, 5, 8, 2, 2]],
    ]
    answers = [
        4,  # Expected output for Example 1
        7,  # Expected output for Example 2
        7,
    ]

    tester = Tester(Solution2().maxWidthRamp)
    tester.test(tests, answers)
