from tester import Tester, generate_random_int_array

from typing import List

"""
You are given an array of events where events[i] = [startDayi, endDayi]. 
Each event i starts at startDayi and ends at endDayi.
You can attend an event i on any day d where startDayi <= d <= endDayi. 
You can only attend one event at any given time d.

Return the maximum number of events you can attend.

Example 1:
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: Attend the first event on day 1, the second on day 2, and the third on day 3.

Example 2:
Input: events = [[1,2],[2,3],[3,4],[1,2]]
Output: 4

Example 3:
Input: events = [[1,10],[2,3],[2,3],[3,7],[1,2],[2,4]]
Output: 4

[1, 2], [1, 2], [2, 2], [1, 5], [1, 5], [3, 3]

Constraints:
- 1 <= events.length <= 10^5
- events[i].length == 2
- 1 <= startDayi <= endDayi <= 10^5
"""

import heapq


class Solution:
    def maxEvents2(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        answer = 0

        today = 1
        i = 0
        heap = []
        while i < n or heap:
            while i < n and today == events[i][0]:
                heapq.heappush(heap, events[i][1])
                i += 1

            while heap and heap[0] < today:
                heapq.heappop(heap)

            if heap:
                heapq.heappop(heap)
                answer += 1
            today += 1
        return answer

    def maxEvents(self, events: List[List[int]]) -> int:
        """Naive approach.
        It doesn't pass some test cases.
        """
        events.sort()
        attended = set()

        for si, ei in events:
            for j in range(si, ei + 1):
                if not j in attended:
                    attended.add(j)
                    break

        return len(attended)


if __name__ == "__main__":
    tests = [
        [
            [[1, 2], [2, 3], [3, 4]],
        ],
        [
            [[1, 2], [2, 3], [3, 4], [1, 2]],
        ],
        [
            [[1, 3], [1, 3], [1, 3], [3, 4]],
        ],
        [[[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]]],
        [
            [
                sorted(generate_random_int_array(2, start_n=1, end_n=10**5))
                for _ in range(10**5)
            ]
        ],
    ]
    answers = [3, 4, 4, 5, -1]

    tester = Tester(Solution().maxEvents2)
    tester.test(tests, answers)
