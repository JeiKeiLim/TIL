from tester import Tester


class SinglyLinkedListNode:
    def __init__(self, data: int) -> None:
        self.next = None
        self.data = data


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last_node = None

    def insert_node(self, data: int) -> None:
        node = SinglyLinkedListNode(data)

        if self.head == None:
            self.head = node

        if self.last_node != None:
            self.last_node.next = node
        self.last_node = node


def mergeLists(
    head1: SinglyLinkedListNode, head2: SinglyLinkedListNode
) -> SinglyLinkedListNode:
    new_head = SinglyLinkedList()

    while head1 is not None or head2 is not None:
        if head1 is None:
            new_head.insert_node(head2.data)
            head2 = head2.next
            continue
        if head2 is None:
            new_head.insert_node(head1.data)
            head1 = head1.next
            continue

        if head1.data < head2.data:
            new_head.insert_node(head1.data)
            head1 = head1.next
        else:
            new_head.insert_node(head2.data)
            head2 = head2.next

    new_list = []
    new_head = new_head.head
    while new_head is not None:
        new_list.append(new_head.data)
        new_head = new_head.next

    return [new_list]


if __name__ == "__main__":
    test_inputs = [
        [[1, 2, 3], [3, 4]],
        [[4, 5, 6], [1, 2, 10]],
    ]
    answers = [[[1, 2, 3, 3, 4]], [[1, 2, 4, 5, 6, 10]]]

    tests = []
    for inputs in test_inputs:
        head1 = SinglyLinkedList()
        head2 = SinglyLinkedList()

        for input in inputs[0]:
            head1.insert_node(input)
        for input in inputs[1]:
            head2.insert_node(input)

        tests.append([head1.head, head2.head])

    tester = Tester(mergeLists)
    tester.test(tests, answers)
