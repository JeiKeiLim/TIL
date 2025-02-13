from tester import Tester, generate_random_int_array

from typing import List
import heapq

"""
You are given a 0-indexed integer array nums, and an integer k.

You are allowed to perform some operations on nums, where in a single operation, you can:
1. Select the two smallest integers x and y from nums.
2. Remove x and y from nums.
3. Insert (min(x, y) * 2 + max(x, y)) at any position in the array.

Note that you can only apply the described operation if nums contains at least two elements.

Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.

Example 1:
Input: nums = [2,11,10,1,3], k = 10
Output: 2
Explanation:
1. Remove elements 1 and 2, then add 1 * 2 + 2 = 4. nums becomes [4, 11, 10, 3].
2. Remove elements 3 and 4, then add 3 * 2 + 4 = 10. nums becomes [10, 11, 10].
Now, all elements are >= 10.

Example 2:
Input: nums = [1,1,2,4,9], k = 20
Output: 4
Explanation:
1. nums becomes [2, 4, 9, 3].
2. nums becomes [7, 4, 9].
3. nums becomes [15, 9].
4. nums becomes [33].
Now, all elements are >= 20.

Constraints:
1. 2 <= nums.length <= 2 * 10^5
2. 1 <= nums[i] <= 10^9
3. 1 <= k <= 10^9
4. The input is generated such that an answer always exists.
"""


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        answer = 0
        while nums[0] < k and len(nums) > 1:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            answer += 1

        return answer


if __name__ == "__main__":
    tests = [
        [[2, 11, 10, 1, 3], 10],
        [[1, 1, 2, 4, 9], 20],
        [generate_random_int_array(2 * 10 ** 5, start_n=1, end_n=10**9), 10**9]
    ]
    answers = [2, 4, -1]

    tester = Tester(Solution().minOperations)
    tester.test(tests, answers)
