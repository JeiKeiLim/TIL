from tester import Tester  # Assuming you have a Tester class for running tests

from typing import List

"""
841. Keys and Rooms
Medium

There are n rooms labeled from 0 to n - 1, and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.

Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We cannot enter room number 2 since the only key that unlocks it is in that room.

Constraints:
- n == rooms.length
- 2 <= n <= 1000
- 0 <= rooms[i].length <= 1000
- 1 <= sum(rooms[i].length) <= 3000
- 0 <= rooms[i][j] < n
- All the values of rooms[i] are unique.
"""


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        O(n^2)

        TODO: Optimize further if possible
        """
        rooms_to_visit = [i for i in range(1, len(rooms))]
        keys_in_hands = rooms[0]

        while len(keys_in_hands) > 0 and len(rooms_to_visit) > 0:
            key = keys_in_hands.pop(0)

            if key in rooms_to_visit:
                rooms_to_visit.remove(key)
                keys_in_hands += rooms[key]

        return len(rooms_to_visit) <= 0


class Solution2:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rooms_to_visit = set(range(1, len(rooms)))
        keys_in_hands = rooms[0]
        idx = 0

        while idx < len(keys_in_hands) and rooms_to_visit:
            key = keys_in_hands[idx]
            idx += 1

            if key in rooms_to_visit:
                rooms_to_visit.remove(key)
                keys_in_hands.extend(rooms[key])

        return len(rooms_to_visit) <= 0


if __name__ == "__main__":
    # Test cases
    tests = [
        [[[1], [2], [3], []]],  # Example 1: True
        [[[1, 3], [3, 0, 1], [2], [0]]],  # Example 2: False
    ]
    answers = [
        True,  # Expected output for Example 1
        False,  # Expected output for Example 2
    ]

    tester = Tester(Solution2().canVisitAllRooms)
    tester.test(tests, answers)
