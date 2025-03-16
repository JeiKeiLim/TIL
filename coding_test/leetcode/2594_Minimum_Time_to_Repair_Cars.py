from tester import Tester, generate_random_int_array
from typing import List
import heapq

"""
You are given an integer array ranks representing the ranks of some mechanics.
ranks[i] is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n^2 minutes.

You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.

Example 1:
Input: ranks = [4,2,3,1], cars = 10
Output: 16
Explanation:
- The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
- The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
- The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
- The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.

4:
    1: 4 * 1 * 1 = 4
    2: 4 * 2 * 2 = 16
    3: 4 * 3 * 3 = 36
    4: 4 * 4 * 4 = 64
3:
    1: 3 * 1 * 1 = 3
    2: 3 * 2 * 2 = 12
    3: 3 * 3 * 3 = 27
    4: 3 * 4 * 4 = 48
2:
    1: 2 * 1 * 1 = 2
    2: 2 * 2 * 2 = 8
    3: 2 * 3 * 3 = 18
    4: 2 * 4 * 4 = 32
1:
    1: 1 * 1 * 1 = 1
    2: 1 * 2 * 2 = 4
    3: 1 * 3 * 3 = 9
    4: 1 * 4 * 4 = 16

cars = 10
[1, 2, 3, 4] - 1
[4, 8, 12, 16] - 5
[9, 18, 27, 36] - 7
[16, 32, 48, 64] - 10

Example 2:
Input: ranks = [5,1,8], cars = 6
Output: 16
Explanation:
- The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
- The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
- The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.

Constraints:
1. 1 <= ranks.length <= 10^5
2. 1 <= ranks[i] <= 100
3. 1 <= cars <= 10^6
"""


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        queue = []

        ranks.sort()
        min_rank = ranks[0]

        repaired_car = 0
        for n_car in range(1, cars + 1):
            for r in ranks:
                heapq.heappush(queue, r * n_car * n_car)

            min_rank_time = min_rank * n_car * n_car
            min_val = min_rank_time
            while queue and queue[0] <= min_rank_time:
                repaired_car += 1
                queue_val = heapq.heappop(queue)
                if repaired_car >= cars:
                    min_val = min(min_val, queue_val)

            if repaired_car >= cars:
                return min_val
        return -1


if __name__ == "__main__":
    tests = [
        [[4, 2, 3, 1], 10],
        [[5, 1, 8], 6],
        [[3, 3, 1, 2, 1, 1, 3, 2, 1], 58],
        [generate_random_int_array(10**5, start_n=1, end_n=100), 10**6],
    ]
    answers = [16, 16, 75, -1]

    tester = Tester(Solution().repairCars)
    tester.test(tests, answers)
