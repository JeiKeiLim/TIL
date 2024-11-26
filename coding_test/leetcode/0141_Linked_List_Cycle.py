from tester import Tester
from data_structure import ListNode
from typing import Optional

"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""


class Solution:
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        node = head.next
        node_map = {}
        while node:
            if node.val not in node_map:
                node_map[node.val] = [node]
            elif node in  node_map[node.val]:
                return True
            else:
                node_map[node.val].append(node)

            node = node.next

        return False


if __name__ == "__main__":

    def create_cycle_list(values, pos):
        if not values:
            return None
        nodes = [ListNode(val) for val in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if pos != -1:
            nodes[-1].next = nodes[pos]
        return nodes[0]

    tests = [
        [create_cycle_list([3, 2, 0, -4], 1)],
        [create_cycle_list([1, 2], 0)],
        [create_cycle_list([1], -1)],
    ]
    answers = [True, True, False]

    tester = Tester(Solution().hasCycle2)
    tester.test(tests, answers)
