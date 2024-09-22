from tester import Tester  # Assuming you have a Tester class for running tests

from typing import List

"""
875. Koko Eating Bananas
Medium

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has fewer than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

### Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

### Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

### Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

### Constraints:
- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Brute force solution
        TODO: Find optimal solution

        O(n^2)
        """
        min_pile = 1
        max_pile = max(piles)

        for k in range(min_pile, max_pile+1):
            hour_spent = 0
            for pile in piles:
                while pile > 0:
                    pile -= k
                    hour_spent += 1

                if hour_spent > h:
                    break

            if hour_spent <= h:
                return k

        return 0


class Solution2:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        O(n log m)
        """
        left = 1  # Minimum possible speed
        right = max(piles)  # Maximum possible speed
        min_k = right  # Initialize min_k to the maximum speed

        while left <= right:
            k = (left + right) // 2
            # Calculate total hours needed at speed k
            total_hours = sum((pile + k - 1) // k for pile in piles)
            if total_hours <= h:
                # Found a possible minimum speed, try to find a smaller one
                min_k = k
                right = k - 1
            else:
                # Need to increase speed
                left = k + 1

        return min_k


if __name__ == "__main__":
    # Test cases
    tests = [
        [[3, 6, 7, 11], 8],  # Example 1
        [[30, 11, 23, 4, 20], 5],  # Example 2
        [[30, 11, 23, 4, 20], 6],  # Example 3
        [[3000, 1100, 2300, 4, 2000] * 100, 600],  # Example 3
        [[312884470], 312884469],
    ]
    answers = [
        4,  # Expected output for Example 1
        30,  # Expected output for Example 2
        23,  # Expected output for Example 3
        2300,  # Expected output for Example 3
        2,
    ]

    tester = Tester(Solution2().minEatingSpeed)
    tester.test(tests, answers)
