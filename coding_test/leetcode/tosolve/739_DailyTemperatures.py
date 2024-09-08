from tester import Tester  # Assuming you have a Tester class for running tests

"""
739. Daily Temperatures
Medium

Given an array of integers `temperatures` representing the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

### Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

### Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

### Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

### Constraints:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        pass  # To be implemented


if __name__ == "__main__":
    # Test cases
    tests = [
        ([73, 74, 75, 71, 69, 72, 76, 73]),  # Example 1
        ([30, 40, 50, 60]),  # Example 2
        ([30, 60, 90]),  # Example 3
    ]
    answers = [
        [1, 1, 4, 2, 1, 1, 0, 0],  # Expected output for Example 1
        [1, 1, 1, 0],  # Expected output for Example 2
        [1, 1, 0],  # Expected output for Example 3
    ]

    tester = Tester(Solution().dailyTemperatures)
    tester.test(tests, answers)
