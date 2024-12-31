from tester import Tester

from typing import List

"""
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:
- A 1-day pass is sold for costs[0] dollars,
- A 7-day pass is sold for costs[1] dollars, and
- A 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

Return the minimum number of dollars you need to travel every day in the given list of days.

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
- On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
- On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
- On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.

Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
- On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
- On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.

Constraints:
1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
"""


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * len(days)
        dp[0] = min(costs)
        day7_idx = 0
        day30_idx = 0

        for i in range(1, len(days)):
            while days[i] - days[day7_idx] >= 7:
                day7_idx += 1
            while days[i] - days[day30_idx] >= 30:
                day30_idx += 1

            day1_cost = dp[i - 1] + costs[0]
            day7_cost = dp[day7_idx - 1] + costs[1]
            day30_cost = dp[day30_idx - 1] + costs[2]
            dp[i] = min(day1_cost, day7_cost, day30_cost)

            # print(f"{days[i]=}, {day7_idx=}, {day1_cost=}, {day7_cost=}, {day30_cost=}, {dp=}")

        return dp[-1]


if __name__ == "__main__":
    tests = [
        [[1, 4, 6, 7, 8, 20], [2, 7, 15]],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]],
        [[6, 8, 9, 18, 20, 21, 23, 25], [2, 10, 41]],
        [[1, 4, 6, 7, 8, 20], [7, 2, 15]],
    ]
    answers = [11, 17, 16, 6]

    tester = Tester(Solution().mincostTickets)
    tester.test(tests, answers)
