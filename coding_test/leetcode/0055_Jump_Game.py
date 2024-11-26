from tester import Tester
from typing import List

"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
"""


class Solution:
    def canJump3(self, nums: List[int]) -> bool:
        current_position = 0
        for i in range(len(nums)):
            if current_position < i:
                return False

            current_position = max(current_position, nums[i] + i)

            if current_position >= len(nums) - 1:
                return True

        return False

    def canJump2(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) < 2:
            return True

        is_pitfall = [True for _ in range(len(nums))]
        is_pitfall[-1] = False

        for i, n in enumerate(nums):
            for j in range(i, min(len(nums), i + n)):
                is_pitfall[j] = False

        return sum(is_pitfall) == 0

    def canJump(self, nums: List[int]) -> bool:
        paths_map = {}

        def check_path(paths: List[int]) -> bool:
            if not paths or len(paths) < 2:
                return True

            if tuple(paths) in paths_map:
                return paths_map[tuple(paths)]

            possible_jump = paths[0]
            for jump in range(1, possible_jump+1):
                check_paths = paths[jump:]
                result = check_path(check_paths)
                paths_map[tuple(check_paths)] = result

                if result:
                    return True

            return False

        return check_path(nums)


if __name__ == "__main__":
    tests = [
        [[2, 3, 1, 1, 4]],
        [[3, 2, 1, 0, 4]],
        [[0, 2, 3]],
        [[1, 0, 1, 0]],
        [[2, 0, 0]],
        [[1, 0, 1, 1]],
        [[2, 5, 0, 0]],
        [[1, 1, 1, 0]],
        [[5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]],
        [[2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2,
          2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3, 8, 2, 4,
          0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4,
          3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7, 1, 9, 1, 9, 4, 9, 0, 1,
          9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6]],
        [[9997] + list(range(9997, -1, -1)) + [0]],
    ]
    answers = [True, False, False, False, True, False, True, True, True, False, False]

    tester = Tester(Solution().canJump3, verbose=0)
    tester.test(tests, answers)
