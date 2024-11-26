from tester import Tester  # Assuming you have a Tester class for running tests

from typing import List

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
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Started @ 15:47
        Brute force(O(n^2)) @ 15:57
        """
        answers = [0] * len(temperatures)
        for i in range(len(temperatures) - 1):
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    answers[i] = j - i
                    break

        return answers

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        sorted_temp = sorted(enumerate(temperatures), key=lambda x: x[1])
        temp_memo = {temp[1]: [] for temp in sorted_temp}
        temp_memo[sorted_temp[0][1]] = [
            i for i in range(len(temperatures)) if i != sorted_temp[0][0]
        ]

        for i in range(1, len(sorted_temp)):
            idx, temp = sorted_temp[i]
            prev_memo = temp_memo[sorted_temp[i - 1][1]].copy()
            prev_memo.remove(idx)
            temp_memo[temp] = prev_memo

        answer = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            for j in temp_memo[temp]:
                if j > i:
                    answer[i] = j - i
                    break

        return answer

    def dailyTemperatures3(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                results[idx] = i - idx
            stack.append(i)

        return results


if __name__ == "__main__":
    # Test cases
    tests = [
        [[73, 74, 75, 71, 69, 72, 76, 73]],  # Example 1
        [[30, 40, 50, 60]],  # Example 2
        [[30, 60, 90]],  # Example 3
    ]
    answers = [
        [1, 1, 4, 2, 1, 1, 0, 0],  # Expected output for Example 1
        [1, 1, 1, 0],  # Expected output for Example 2
        [1, 1, 0],  # Expected output for Example 3
    ]

    tester = Tester(Solution().dailyTemperatures3)
    tester.test(tests, answers)
