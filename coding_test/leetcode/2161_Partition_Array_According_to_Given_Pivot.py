from tester import Tester, generate_random_int_array

from typing import List

"""
You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that:

1. Every element less than pivot appears before every element greater than pivot.
2. Every element equal to pivot appears in between the elements less than and greater than pivot.
3. The relative order of the elements less than pivot and the elements greater than pivot is maintained.

Return nums after the rearrangement.

Example 1:
Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]

i, prior_i, post_i
2, 1, 5

[9,10,5,10,14,3,12]

nums[i] < pivot -> nums[i], nums[prior_i] = nums[prior_i], nums[i]; prior_i += 1; i += 1
nums[i] > pivot -> nums[i], nums[post_i] = nums[post_i], nums[i]; post_i -=1;
nums[i] == pivot -> i += 1


Example 2:
Input: nums = [-3,4,3,2], pivot = 2
Output: [-3,2,4,3]

Constraints:
1. 1 <= nums.length <= 10^5
2. -10^6 <= nums[i] <= 10^6
3. pivot equals to an element of nums.
"""


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        prior = []
        post = []
        eq = []
        for n in nums:
            if n < pivot:
                prior.append(n)
            elif n > pivot:
                post.append(n)
            else:
                eq.append(n)

        return prior + eq + post


if __name__ == "__main__":
    tests = [
        [[9, 12, 5, 10, 14, 3, 10], 10],
        [[-3, 4, 3, 2], 2],
        [generate_random_int_array(10**5, start_n=-(10**6), end_n=10**6), 10**5],
    ]
    answers = [
        [9, 5, 3, 10, 10, 12, 14],
        [-3, 2, 4, 3],
        Solution().pivotArray(*tests[-1]),
    ]

    tester = Tester(Solution().pivotArray, exact_match=True)
    tester.test(tests, answers)
