from tester import Tester
from data_structure import get_ListNode, ListNode

from typing import Optional, List


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
        [[1, 2, 3], get_ListNode([1, 2, 3, 4, 5])],
        [[1], get_ListNode([1, 2, 1, 2, 1, 2])],
        [[5], get_ListNode([1, 2, 3, 4])],
        [[1, 7, 6, 2, 4], get_ListNode([3, 7, 1, 8, 1])],
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            get_ListNode([5, 5, 5, 5, 5, 5, 5, 11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),
        ],
    ]
    answers = [
        get_ListNode([4, 5]),
        get_ListNode([2, 2, 2]),
        get_ListNode([1, 2, 3, 4]),
        get_ListNode([3, 8]),
        get_ListNode([11]),
    ]

    tester = Tester(Solution().modifiedList)
    tester.test(tests, answers)
