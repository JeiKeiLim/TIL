from tester import Tester

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next: Optional[ListNode] = next

    def __repr__(self) -> str:
        result = []
        node = self
        while node is not None:
            result.append(node.val)
            node = node.next
        return str(result)

    def __eq__(self, other: "ListNode") -> bool:
        node1 = self
        node2 = other

        while node1 is not None and node2 is not None and node1.val == node2.val:
            node1 = node1.next
            node2 = node2.next

        if node1 is None and node2 is None:
            return True

        if (node1 is None and node2 is not None) or (
            node1 is not None and node2 is None
        ):
            return False

        return node1.val == node2.val


def get_head(nums: List[int]) -> ListNode:
    head = ListNode(nums[0])
    node = head

    for i in range(1, len(nums)):
        node.next = ListNode(nums[i])
        node = node.next

    return head


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Time: O(n)
        Space: O(n)
        """
        node = head
        prev_node = node

        num_map = {num: True for num in nums}

        while node is not None:
            if num_map.get(node.val, False):
                if head == node:
                    head = node.next
                    prev_node = head
                else:
                    prev_node.next = node.next
            else:
                prev_node = node

            node = node.next

        return head


if __name__ == "__main__":
    tests = [
        [[1, 2, 3], get_head([1, 2, 3, 4, 5])],
        [[1], get_head([1, 2, 1, 2, 1, 2])],
        [[5], get_head([1, 2, 3, 4])],
        [[1, 7, 6, 2, 4], get_head([3, 7, 1, 8, 1])],
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            get_head([5, 5, 5, 5, 5, 5, 5, 11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),
        ],
    ]
    answers = [
        get_head([4, 5]),
        get_head([2, 2, 2]),
        get_head([1, 2, 3, 4]),
        get_head([3, 8]),
        get_head([11]),
    ]

    tester = Tester(Solution().modifiedList)
    tester.test(tests, answers)
