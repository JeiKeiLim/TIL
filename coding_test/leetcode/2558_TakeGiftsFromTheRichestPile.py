from tester import Tester
import heapq

from typing import List

"""
You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

Choose the pile with the maximum number of gifts.
If there is more than one pile with the maximum number of gifts, choose any.
Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
Return the number of gifts remaining after k seconds.

Example 1:

Input: gifts = [25,64,9,4,100], k = 4
Output: 29
Explanation:
The gifts are taken in the following way:
- In the first second, the last pile is chosen and 10 gifts are left behind.
- Then the second pile is chosen and 8 gifts are left behind.
- After that the first pile is chosen and 5 gifts are left behind.
- Finally, the last pile is chosen again and 3 gifts are left behind.
The final remaining gifts are [5,8,9,4,3], so the total number of gifts remaining is 29.
Example 2:

Input: gifts = [1,1,1,1], k = 4
Output: 4
Explanation:
In this case, regardless which pile you choose, you have to leave behind 1 gift in each pile.
That is, you can't take any pile with you.
So, the total gifts remaining are 4.

Constraints:
1 <= gifts.length <= 103
1 <= gifts[i] <= 109
1 <= k <= 103
"""


class Solution:
    def pickGifts2(self, gifts: List[int], k: int) -> int:
        heap_gifts = [-x for x in gifts]
        heapq.heapify(heap_gifts)

        for _ in range(k):
            val = -heapq.heappop(heap_gifts)
            heapq.heappush(heap_gifts, -int(val**0.5))

        return -sum(heap_gifts)

    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            max_idx = 0
            max_val = gifts[max_idx]
            for i in range(1, len(gifts)):
                if max_val < gifts[i]:
                    max_val = gifts[i]
                    max_idx = i

            gifts[max_idx] = int(gifts[max_idx] ** 0.5)

        return sum(gifts)


if __name__ == "__main__":
    tests = [
        [[25, 64, 9, 4, 100], 4],
        [[1, 1, 1, 1], 4],
    ]
    answers = [29, 4]

    tester = Tester(Solution().pickGifts2)
    tester.test(tests, answers)
