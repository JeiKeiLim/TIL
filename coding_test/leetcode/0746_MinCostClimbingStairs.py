from tester import Tester  # Assuming you have a Tester class for running tests
from typing import List

"""
746. Min Cost Climbing Stairs
Easy

You are given an integer array cost where cost[i] is the cost of the ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

### Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

### Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

### Constraints:
- 2 <= cost.length <= 1000
- 0 <= cost[i] <= 999
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Started @ 23.39
        Ended @ 23:59
        O(n^2)
        """
        result = []

        def trace(step: int, current_cost: int) -> None:
            if step >= len(cost):
                result.append(current_cost)
                return

            cost1, cost2 = 0, 0
            if step + 1 < len(cost):
                cost1 = cost[step + 1]
            if step + 2 < len(cost):
                cost2 = cost[step + 2]

            trace(step + 1, current_cost + cost1)
            trace(step + 2, current_cost + cost2)

        trace(-1, 0)
        return min(result)


class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        O(n)
        """
        memo = {}

        def trace(step: int) -> int:
            if step >= len(cost):
                return 0

            if step in memo:
                return memo[step]

            memo[step] = cost[step] + min(trace(step + 1), trace(step + 2))

            return memo[step]

        return min(trace(0), trace(1))


if __name__ == "__main__":
    # Test cases
    tests = [
        [[10, 15, 20]],  # Example 1
        [[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]],  # Example 2
    ]
    answers = [
        15,  # Expected output for Example 1
        6,  # Expected output for Example 2
    ]

    tester = Tester(Solution2().minCostClimbingStairs)
    tester.test(tests, answers)
