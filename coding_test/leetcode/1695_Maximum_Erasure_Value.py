from tester import Tester, generate_random_int_array

from typing import List

"""
You are given an array of positive integers nums and want to erase a subarray containing unique elements.
The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

A subarray is a contiguous portion of the array.

Example 1:
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray is [2,4,5,6].

Example 2:
Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray is [5,2,1] or [1,2,5].

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
"""

from collections import deque


class Solution:
    def maximumUniqueSubarray3(self, nums: List[int]) -> int:
        queue = deque()
        seen = set()
        cum_sum = 0
        max_sum = 0
        for n in nums:
            while queue and n in seen:
                n_left = queue.popleft()
                seen.remove(n_left)
                cum_sum -= n_left

            queue.append(n)
            seen.add(n)
            cum_sum += n
            max_sum = max(max_sum, cum_sum)

        return max_sum

    def maximumUniqueSubarray2(self, nums: List[int]) -> int:
        queue = deque()
        seen = set()
        max_sum = 0
        for n in nums:
            while queue and n in seen:
                seen.remove(queue.popleft())

            queue.append(n)
            seen.add(n)
            max_sum = max(max_sum, sum(queue))

        return max_sum

    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """Naive approach."""
        unique_arr = set()
        queue = deque()
        seen = set()
        for n in nums:
            while queue and n in seen:
                seen.remove(queue.popleft())

            queue.append(n)
            seen.add(n)
            unique_arr.add(tuple(queue))

        max_sum = max(map(sum, unique_arr))
        return max_sum


if __name__ == "__main__":
    tests = [
        [[4, 2, 4, 5, 6]],
        [[5, 2, 1, 2, 5, 2, 1, 2, 5]],
        [generate_random_int_array(10**5, start_n=1, end_n=10**4)],
    ]
    answers = [17, 8, -1]

    tester = Tester(Solution().maximumUniqueSubarray3)
    tester.test(tests, answers)
