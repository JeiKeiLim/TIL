from tester import Tester

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """Find the pivot index of a list of numbers

        ex)
        nums = [1, 7, 3, 6, 5, 6]
        pivotIndex(nums) -> 3

        [ left ] [p] [right]
        [1, 7, 3, 6, 5, 6]

        sum([1, 7, 3]) == sum([5, 6])

        Args:
            nums: list of numbers

        Returns:
            int: the pivot index of the leftmost index
            -1 if there is no pivot index
        """
        leftmost_sum = 0
        rightmost_sum = sum(nums) - nums[0]

        for i in range(len(nums) - 1):
            if leftmost_sum == rightmost_sum:
                return i

            leftmost_sum += nums[i]
            rightmost_sum -= nums[i + 1]

        if leftmost_sum == rightmost_sum:
            return len(nums)-1

        return -1


if __name__ == "__main__":
    tests = [
        [[1, 7, 3, 6, 5, 6]],
        [[1, 2, 3]],
        [[2, 1, -1]],
        [[-1, -1, 0, -1, -1, 0]],
        [[-1, -1, -1, 0, -1, -1]],
        [[-1, -1, 0, 1, 1, 0]],
    ]
    answers = [3, -1, 0, 2, 2, 5]

    tester = Tester(Solution().pivotIndex)
    tester.test(tests, answers)
