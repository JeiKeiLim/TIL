from tester import Tester, generate_random_2d_int_array

from typing import List

"""
You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].

Count the number of pairs of points (A, B), where
• A is on the upper left side of B, and
• there are no other points in the rectangle (or line) they make (including the border).

Return the count.
 
Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 0
Explanation:
There is no way to choose A and B so A is on the upper left side of B.

3|    x
2|  x
1|x
 |-----
  1 2 3 


Example 2:
Input: points = [[6,2],[4,4],[2,6]]
Output: 2
Explanation:
• The left one is the pair (points[1], points[0]), where points[1] is on the upper left side of points[0] and the rectangle is empty.
• The middle one is the pair (points[2], points[1]), same as the left one it is a valid pair.
• The right one is the pair (points[2], points[0]), where points[2] is on the upper left side of points[0], but points[1] is inside the rectangle so it's not a valid pair.

6|  x
5|
4|      x
3|
2|          x
1|
 |-----------
  1 2 3 4 5 6

Example 3:
Input: points = [[3,1],[1,3],[1,1]]
Output: 2
Explanation:
• The left one is the pair (points[2], points[0]), where points[2] is on the upper left side of points[0] and there are no other points on the line they form. Note that it is a valid state when the two points form a line.
• The middle one is the pair (points[1], points[2]), it is a valid pair same as the left one.
• The right one is the pair (points[1], points[0]), it is not a valid pair as points[2] is on the border of the rectangle.

3|x
2|
1|x   x
 |-----
  1 2 3 

Example 4:
Input: points = [[3, 1], [6, 1], [2, 4], [4, 4], [2, 6]]
Output: 5

6|  x
5|
4|  x   x
3|
2|
1|    x     x
 |-----------
  1 2 3 4 5 6

Example 5:
5|
4|
3|  x
2|
1|x           x
0|
 |-------------
  0 1 2 3 4 5 6

Constraints:
• 2 <= n <= 50
• points[i].length == 2
• 0 <= points[i][0], points[i][1] <= 50
• All points[i] are distinct.
"""
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        answer = 0
        points.sort()

        for i in range(n):
            xi, yi = points[i]

            for j in range(n):
                if i == j:
                    continue
                
                xj, yj = points[j]

                if xi <= xj and yi >= yj:
                    is_valid_pair = 1
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        
                        xk, yk = points[k]

                        if xi <= xk <= xj and yj <= yk <= yi:
                            is_valid_pair = 0
                            break
                    
                    answer += is_valid_pair
        
        return answer


if __name__ == "__main__":
    tests = [
        [[[1, 1], [2, 2], [3, 3]]],
        [[[6, 2], [4, 4], [2, 6]]],
        [[[3, 1], [1, 3], [1, 1]]],
        [[[3, 1], [6, 1], [2, 4], [4, 4], [2, 6]]],
        [[[0, 1], [0, 2], [0, 4]]],
        [[[1, 0], [2, 0], [4, 0]]],
        [[[0, 1], [1, 3], [6, 1]]],
        [generate_random_2d_int_array(50, 2, end_n=50)]
    ]
    
    answers = [0, 2, 2, 5, 2, 2, 2, -1]

    tester = Tester(Solution().numberOfPairs)
    tester.test(tests, answers)
