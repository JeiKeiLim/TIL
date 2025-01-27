from tester import Tester, generate_random_int_array

from typing import List

"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first
if you want to take course bi.

- For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
- Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c,
  then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj].
For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]


Example 2:
Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]

Example 3:
Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]

[3, [[2, 0], [1, 2]], [[2, 1], [1, 0]]]


Constraints:
1. 2 <= numCourses <= 100
2. 0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
3. prerequisites[i].length == 2
4. 0 <= ai, bi <= numCourses - 1
5. ai != bi
6. All the pairs [ai, bi] are unique.
7. The prerequisites graph has no cycles.
8. 1 <= queries.length <= 10^4
9. 0 <= ui, vi <= numCourses - 1
10. ui != vi
"""


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        pre_map = {i: set() for i in range(numCourses)}
        for pre_course, course in prerequisites:
            pre_map[course].add(pre_course)

        for course in pre_map.keys():
            stack = list(pre_map[course])
            while stack:
                pre_course = stack.pop()

                for pre_precourse in pre_map[pre_course]:
                    if pre_precourse not in pre_map[course]:
                        stack.append(pre_precourse)
                pre_map[course].add(pre_course)

        answer = []
        for pre_course, course in queries:
            if pre_course in pre_map[course]:
                answer.append(True)
            else:
                answer.append(False)
        return answer


if __name__ == "__main__":
    tests = [
        [2, [[1, 0]], [[0, 1], [1, 0]]],
        [2, [], [[1, 0], [0, 1]]],
        [3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]],
        [3, [[2, 0], [1, 2]], [[2, 1], [1, 0]]],
        [
            100,
            [generate_random_int_array(2, end_n=99) for _ in range(int(100 * 99 / 2))],
            [generate_random_int_array(2, end_n=99) for _ in range(10**4)],
        ],
    ]
    answers = [
        [False, True],
        [False, False],
        [True, True],
        [True, False],
        [True] * (10**4),
    ]

    tester = Tester(Solution().checkIfPrerequisite, verbose=0)
    tester.test(tests, answers)
