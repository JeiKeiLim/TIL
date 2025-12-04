from tester import Tester, generate_random_int_array

"""
There are n cars on an infinitely long road, and each car is at a unique point.

You are given a string directions of length n where:
- directions[i] is 'L' if the i-th car moves left,
- directions[i] is 'R' if it moves right,
- directions[i] is 'S' if it stays stationary.

Each car moves at the same speed.

Collisions happen as follows:
- Two cars moving in opposite directions ('R' and 'L') cause 2 collisions and both stop.
- A moving car ('R' or 'L') hitting a stationary car ('S') causes 1 collision and the moving car stops.
- After colliding, a car becomes stationary.

Return the total number of collisions that will happen on the road.

Example 1:
Input: directions = "RLRSLL"
Output: 5
Explanation:
- R (0) collides with L (1): +2
- R (2) collides with S (3): +1
- S (3) collides with L (4): +1
- S (4) collides with L (5): +1
Total: 5 collisions

"LRRLRSLLR"

Example 2:
Input: directions = "LLRR"
Output: 0
Explanation:
No collisions possible.

Constraints:
- 1 <= directions.length <= 10^5
- directions[i] ∈ {'L', 'R', 'S'}
"""


class Solution:
    def countCollisions2(self, directions: str) -> int:
        n = len(directions)
        n_safe = 0
        for i in range(n):
            if directions[i] == "L":
                n_safe += 1
            else:
                break
        for i in range(n - 1, -1, -1):
            if directions[i] == "R":
                n_safe += 1
            else:
                break

        return n - directions.count("S") - n_safe

    def countCollisions(self, directions: str) -> int:
        answer = 0
        r_cnt = 0
        left_collidible = False
        for dir in directions:
            if dir == "R":
                r_cnt += 1
            elif dir == "S":
                left_collidible = True
                answer += r_cnt
                r_cnt = 0
            else:
                left_collidible = left_collidible or r_cnt > 0
                answer += r_cnt + int(r_cnt > 0 or left_collidible)
                r_cnt = 0
        return answer


if __name__ == "__main__":
    tests = [
        ["RLRSLL"],
        ["LLRR"],
        ["LRRLRSLLR"],
        ["LSSSLLSSSSLRRSLLLSLSLRRLLLLLRSSRSRRSLLLSSS"],
        ["LLRLRLLSLRLLSLSSSS"],
        ["".join("RLS"[i] for i in generate_random_int_array(10**6, end_n=2))],
    ]
    answers = [5, 0, 6, 24, 10, Solution().countCollisions(*tests[-1])]

    tester = Tester(Solution().countCollisions2)
    tester.test(tests, answers)
