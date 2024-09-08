from tester import Tester  # Assuming you have a Tester class for running tests

"""
162. Find Peak Element
Medium

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

### Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

### Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

### Constraints:
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i + 1] for all valid i.
"""


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        ([1, 2, 3, 1]),  # Example 1
        ([1, 2, 1, 3, 5, 6, 4]),  # Example 2
    ]
    answers = [
        2,  # Expected output for Example 1
        5,  # Expected output for Example 2 (can also return 1)
    ]

    tester = Tester(Solution().findPeakElement)
    tester.test(tests, answers)
