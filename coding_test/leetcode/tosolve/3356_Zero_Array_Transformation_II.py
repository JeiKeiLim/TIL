from tester import Tester, generate_random_int_array
from typing import List

"""
You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].
Each queries[i] represents the following action on nums:
    - Decrement the value at each index in the range [li, ri] in nums by at most vali.
    - The amount by which each value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.
Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

Example 1:
Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]
Output: 2
Explanation:
- For i = 0 (l = 0, r = 2, val = 1):
  - Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
  - The array will become [1, 0, 1].
- For i = 1 (l = 0, r = 2, val = 1):
  - Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
  - The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.

Example 2:
Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]
Output: -1
Explanation:
- For i = 0 (l = 1, r = 3, val = 2):
  - Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
  - The array will become [4, 1, 0, 0].
- For i = 1 (l = 0, r = 2, val = 1):
  - Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
  - The array will become [3, 0, 0, 0], which is not a Zero Array.


Constraints:
1. 1 <= nums.length <= 10^5
2. 0 <= nums[i] <= 5 * 10^5
3. 1 <= queries.length <= 10^5
4. queries[i].length == 3
5. 0 <= li <= ri < nums.length
6. 1 <= vali <= 5
"""


class Solution:
    def minOperations2(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        """
        [0,2,1],[0,3,1],[1,1,3]

        [2, 3, 0, 0]
        [0, -3, -1, -1]

        2, 5
        2, 2, 1, 0
        """
        n = len(nums)
        cum_sum = [0] * n
        cum_sum[0] = nums[0]
        for i in range(1, n):
            cum_sum[i] += cum_sum[i-1] + nums[i]

        return -1


    def minOperations(self, nums: List[int], queries: List[List[int]]) -> int:
        total = sum(nums)
        if total == 0:
            return 0

        answer = 0
        for li, ri, vali in queries:
            for i in range(li, ri + 1):
                decr_val = min(nums[i], vali)
                nums[i] -= decr_val
                total -= decr_val
            answer += 1
            if total == 0:
                return answer

        return -1


if __name__ == "__main__":
    tests = [
        [[2, 0, 2], [[0, 2, 1], [0, 2, 1], [1, 1, 3]]],
        [[4, 3, 2, 1], [[1, 3, 2], [0, 2, 1]]],
        [[2, 5, 2, 1], [[1, 1, 3], [0, 2, 1], [0, 3, 1]]],
        [[0], [[0, 0, 1]]],
        [
            generate_random_int_array(10**4, end_n=5 * 10**5),
            [
                sorted(generate_random_int_array(2, end_n=10**3 - 1)) + [3]
                for _ in range(10**4)
            ],
        ],
    ]
    answers = [2, -1, 3, 0, -1]

    tester = Tester(Solution().minOperations2)
    tester.test(tests, answers)
