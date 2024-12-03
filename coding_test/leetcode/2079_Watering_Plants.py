from tester import Tester
from typing import List

"""
You want to water n plants in your garden with a watering can. The plants are arranged in a row, and the ith plant is located at x = i. There is a river at x = -1 where you can refill the watering can.

Rules:
- Water the plants in order from left to right.
- If you do not have enough water to completely water the next plant, return to the river to refill.
- You cannot refill the watering can early.

Given a 0-indexed integer array plants where plants[i] is the amount of water the ith plant needs, and an integer capacity representing the watering can capacity, return the number of steps needed to water all the plants.

Example 1:
Input: plants = [2,2,3,3], capacity = 5
Output: 14
Explanation: Start at the river with a full watering can:
- Walk to plant 0 (1 step) and water it. Watering can has 3 units of water.
- Walk to plant 1 (1 step) and water it. Watering can has 1 unit of water.
- Since you cannot completely water plant 2, walk back to the river to refill (2 steps).
- Walk to plant 2 (3 steps) and water it. Watering can has 2 units of water.
- Since you cannot completely water plant 3, walk back to the river to refill (3 steps).
- Walk to plant 3 (4 steps) and water it.
Steps needed = 1 + 1 + 2 + 3 + 3 + 4 = 14.

Example 2:
Input: plants = [1,1,1,4,2,3], capacity = 4
Output: 30
Explanation: Start at the river with a full watering can:
- Water plants 0, 1, and 2 (3 steps). Return to river (3 steps).
- Water plant 3 (4 steps). Return to river (4 steps).
- Water plant 4 (5 steps). Return to river (5 steps).
- Water plant 5 (6 steps).
Steps needed = 3 + 3 + 4 + 4 + 5 + 5 + 6 = 30.

Example 3:
Input: plants = [7,7,7,7,7,7,7], capacity = 8
Output: 49
Explanation: You have to refill before watering each plant.
Steps needed = 1 + 1 + 2 + 2 + 3 + 3 + 4 + 4 + 5 + 5 + 6 + 6 + 7 = 49.

Constraints:
1 <= plants.length <= 1000
1 <= plants[i] <= 10^6
max(plants[i]) <= capacity <= 10^9
"""


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 1
        water_can = capacity - plants[0]

        for i in range(1, len(plants)):
            water = plants[i]
            water_can -= water

            if water_can < 0:
                steps += (i * 2)
                water_can = capacity - water

            steps += 1

        return steps


if __name__ == "__main__":
    tests = [
        [[2, 2, 3, 3], 5],
        [[1, 1, 1, 4, 2, 3], 4],
        [[7, 7, 7, 7, 7, 7, 7], 8],
        [[3, 2, 4, 2, 1], 6],
    ]
    answers = [
        14,
        30,
        49,
        17,
    ]

    tester = Tester(Solution().wateringPlants)
    tester.test(tests, answers)
