from tester import Tester  # Assuming you have a Tester class for running tests

"""
215. Kth Largest Element in an Array
Medium

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

### Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

### Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

### Constraints:
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pass


if __name__ == "__main__":
    # Test cases
    tests = [
        ([3, 2, 1, 5, 6, 4], 2),  # Example 1
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),  # Example 2
    ]
    answers = [
        5,  # Expected output for Example 1
        4,  # Expected output for Example 2
    ]

    tester = Tester(Solution().findKthLargest)
    tester.test(tests, answers)
