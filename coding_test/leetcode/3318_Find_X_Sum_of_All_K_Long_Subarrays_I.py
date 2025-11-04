from tester import Tester, generate_random_int_array

"""
You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:
1. Count the occurrences of all elements in the array.
2. Keep only the occurrences of the top x most frequent elements. 
   If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
3. Calculate the sum of the resulting array.

If an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].

Example 1:
Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2
Output: [6,10,12]

Example 2:
Input: nums = [3,8,7,8,7,5], k = 2, x = 2
Output: [11,15,15,15,12]

Constraints:
• 1 <= n == nums.length <= 50
• 1 <= nums[i] <= 50
• 1 <= x <= k <= nums.length
"""


class Solution:
    def xSumSubarrays(self, nums: list[int], k: int, x: int) -> list[int]:
        answer = []
        freq_map = {}
        for i, num in enumerate(nums):
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1

            if (i + 2) <= k:
                continue

            candidates = sorted(
                freq_map.items(), key=lambda f: (f[1], f[0]), reverse=True
            )[:x]
            answer.append(sum(c[0] * c[1] for c in candidates))

            freq_map[nums[i - k + 1]] -= 1
        return answer


if __name__ == "__main__":
    tests = [
        [[1, 1, 2, 2, 3, 4, 2, 3], 6, 2],
        [[3, 8, 7, 8, 7, 5], 2, 2],
        [generate_random_int_array(1000), 5, 500]
    ]
    answers = [
        [6, 10, 12],
        [11, 15, 15, 15, 12],
        [-1, -1]
    ]

    tester = Tester(Solution().xSumSubarrays)
    tester.test(tests, answers)
