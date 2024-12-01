from tester import Tester

import random

"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.

You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""


class Solution:
    def canFinish2(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        free_courses = set(list(range(numCourses)))

        course_map = {course: [] for course in range(numCourses)}
        reverse_course_map = {course: [] for course in range(numCourses)}

        for course, prerequisite in prerequisites:
            course_map[course].append(prerequisite)
            reverse_course_map[prerequisite].append(course)

            if prerequisite in free_courses:
                free_courses.remove(prerequisite)

        n_course_left = numCourses

        while free_courses:
            course = free_courses.pop()
            n_course_left -= 1

            for pre_course in course_map[course]:
                reverse_course_map[pre_course].remove(course)

                if len(reverse_course_map[pre_course]) == 0:
                    free_courses.add(pre_course)

        return n_course_left == 0

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        Condition 1: Find cyclic reference.

        [0, 1, 2, 3]

        [0, 1]
        [0, 2]
        [1, 3]
        """
        course_map = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            course_map[course].append(prerequisite)

        course_took = set()

        def dfs(course: int) -> bool:
            if len(course_map[course]) == 0:
                return True

            if course in course_took:
                return False

            course_took.add(course)

            for prerequisite in course_map[course]:
                if not dfs(prerequisite):
                    return False

            course_map[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


if __name__ == "__main__":
    tests = [
        [2, [[1, 0]]],
        [2, [[1, 0], [0, 1]]],
        [4, [[0, 1], [0, 2], [1, 3], [2, 3]]],
        [3, [[1, 0], [0, 2], [2, 1]]],
        [7, [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]],
        [4, [[0, 1], [3, 1], [1, 3], [3, 2]]],
    ]
    long_test = [[i, i + 1] for i in range(699)]
    for _ in range(100):
        long_test.append(random.choices(list(range(0, 699)), k=2))
    # tests.append([700, long_test])

    answers = [True, False, True, False, True, False, False]

    tester = Tester(Solution().canFinish)
    tester.test(tests, answers)
