from tester import Tester

from typing import List
import random

"""
You are given a 0-indexed array nums and a non-negative integer k.

In one operation, you can:
- Choose an index i that hasn't been chosen before from the range [0, nums.length - 1].
- Replace nums[i] with any integer from the range [nums[i] - k, nums[i] + k].

The beauty of the array is the length of the longest subsequence consisting of equal elements.

Return the maximum possible beauty of the array nums after applying the operation any number of times.

Note:
- A subsequence of an array is generated from the original array by deleting some elements (possibly none) 
  without changing the order of the remaining elements.

Example 1:
Input: nums = [4,6,1,2], k = 2
Output: 3
Explanation:
In this example, we apply the following operations:
- Choose index 1, replace it with 4 (from range [4,8]), nums = [4,4,1,2].
- Choose index 3, replace it with 4 (from range [0,4]), nums = [4,4,1,4].
The beauty of the array nums is 3 (subsequence consisting of indices 0, 1, and 3).

Example 2:
Input: nums = [1,1,1,1], k = 10
Output: 4
Explanation:
In this example, we don't have to apply any operations.
The beauty of the array nums is 4 (whole array).

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i], k <= 10^5
"""


class Solution:
    def maximumBeauty3(self, nums: List[int], k: int) -> int:
        """O(n log n)"""
        nums.sort()
        left = 0
        right = 1
        result = 1
        while right < len(nums):  # O(n)
            diff = nums[right] - nums[left]

            while diff > (2 * k):
                left += 1
                diff = nums[right] - nums[left]

            result = max(result, right - left + 1)
            right = max(left + 1, right + 1)

        return result

    def maximumBeauty2(self, nums: List[int], k: int) -> int:
        """O(n^2)"""
        nums.sort()
        ptr1 = 0
        ptr2 = len(nums) - 1
        result = 1
        for ptr1 in range(len(nums) - 1):
            for ptr2 in range(len(nums) - 1, ptr1, -1):
                n1 = nums[ptr1] + k
                n2 = nums[ptr2] - k
                if (n2 - n1) < 1:
                    result = max(result, ptr2 - ptr1 + 1)

        return result

    def maximumBeauty(self, nums: List[int], k: int) -> int:
        """O(nk)"""
        freq = {}
        for n in nums:
            for m in range(max(0, n - k), n + k + 1):
                freq[m] = freq.get(m, 0) + 1

        return max(freq.values())


if __name__ == "__main__":
    tests = [
        [[4, 6, 1, 2], 2],
        [[1, 1, 1, 1], 10],
        [[75, 15, 9], 28],
        [[50, 28, 30, 51], 2],
        [[48, 93, 96, 19], 24],
        [[random.randint(0, 10**5) for _ in range(10**5)], 10**5],
    ]
    answers = [
        3,
        4,
        2,
        2,
        3,
        -1,
    ]

    tester = Tester(Solution().maximumBeauty3, verbose=0)
    tester.test(tests, answers)
