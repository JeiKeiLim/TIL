from tester import Tester

from typing import List


def TreeConstructor(strArr: List[str]) -> bool:
    """
    Can't be more than three times to be a parent
    Can't be more than twice to be a child
    """
    child_map = {}
    parent_map = {}

    for node in strArr:
        left, right = [
            int(num) for num in node.replace(")", "").replace("(", "").split(",")
        ]

        if left not in child_map.keys():
            child_map[left] = 1
        else:
            return False

        if right not in parent_map.keys():
            parent_map[right] = 1
        else:
            parent_map[right] += 1

        if parent_map[right] > 2:
            return False

    return True


if __name__ == "__main__":
    tests = [
        [["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]],
        [["(1,2)", "(3,2)", "(2,12)", "(5,2)"]],
    ]
    answers = [True, False]

    tester = Tester(TreeConstructor)
    tester.test(tests, answers)
