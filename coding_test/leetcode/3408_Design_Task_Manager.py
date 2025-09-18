from tester import Tester

"""
There is a task management system that allows users to manage their tasks, each associated with a priority. 
The system should efficiently handle adding, modifying, executing, and removing tasks.

Implement the TaskManager class:

• TaskManager(vector<vector<int>>& tasks)
    Initializes the task manager with a list of user-task-priority triples.
    Each element in the input list is of the form [userId, taskId, priority], which adds a task to the specified user with the given priority.

• void add(int userId, int taskId, int priority)
    Adds a task with the specified taskId and priority to the user with userId.
    It is guaranteed that taskId does not exist in the system.

• void edit(int taskId, int newPriority)
    Updates the priority of the existing taskId to newPriority.
    It is guaranteed that taskId exists in the system.

• void rmv(int taskId)
    Removes the task identified by taskId from the system.
    It is guaranteed that taskId exists in the system.

• int execTop()
    Executes the task with the highest priority across all users.
    If there are multiple tasks with the same highest priority, execute the one with the highest taskId.
    After executing, the taskId is removed from the system.
    Return the userId associated with the executed task.
    If no tasks are available, return -1.

Note: a user may be assigned multiple tasks.

Example 1:
Input:
["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]
[[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]
Output:
[null, null, null, 3, null, null, 5]

Explanation:
TaskManager taskManager = new TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]]);
taskManager.add(4, 104, 5);
taskManager.edit(102, 8);
taskManager.execTop(); // return 3
taskManager.rmv(101);
taskManager.add(5, 105, 15);
taskManager.execTop(); // return 5


Constraints:
• 1 <= tasks.length <= 10^5
• 0 <= userId <= 10^5
• 0 <= taskId <= 10^5
• 0 <= priority <= 10^9
• 0 <= newPriority <= 10^9
• At most 2 * 10^5 calls will be made in total to add, edit, rmv, and execTop methods.
• The input is generated such that taskId will be valid.
"""

import heapq


class TaskManager:

    def __init__(self, tasks: list[list[int]]):
        self.queue = []
        self.task_priorities = {}
        for user_id, task_id, priority in tasks:
            heapq.heappush(self.queue, (-priority, -task_id))
            self.task_priorities[task_id] = [-priority, user_id]

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.queue, (-priority, -taskId))
        self.task_priorities[taskId] = [-priority, userId]

    def edit(self, taskId: int, newPriority: int) -> None:
        heapq.heappush(self.queue, (-newPriority, -taskId))
        self.task_priorities[taskId][0] = -newPriority

    def rmv(self, taskId: int) -> None:
        self.task_priorities.pop(taskId)

    def execTop(self) -> int:
        if not self.task_priorities or not self.queue:
            return -1
        priority, task_id = heapq.heappop(self.queue)
        task_id = -task_id
        while self.task_priorities.get(task_id, (-1, -1))[0] != priority:
            if not self.task_priorities or not self.queue:
                return -1

            priority, task_id = heapq.heappop(self.queue)
            task_id = -task_id

        return self.task_priorities.pop(task_id)[1]



if __name__ == "__main__":
    actions = ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]
    inputs = [
        [[[1, 101, 10], [2, 102, 20], [3, 103, 15]]],
        [4, 104, 5],
        [102, 8],
        [],
        [101],
        [5, 105, 15],
        [],
    ]

    tests = [
        [actions, inputs],
        [["TaskManager", "execTop", "execTop"], [[[[1, 101, 10]]], [], []]],
    ]
    expected = [[None, None, None, 3, None, None, 5], [None, 1, -1]]

    tester = Tester(TaskManager)
    tester.test(tests, expected)
