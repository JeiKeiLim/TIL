from tester import Tester

from typing import List, Dict


def get_character_map(message: str) -> Dict[str, int]:
    message_map = {}
    for char in message:
        message_map[char] = message_map.get(char, 0) + 1

    return message_map


def is_substring(message: str, target: str) -> bool:
    target_map = get_character_map(target)
    message_map = get_character_map(message)

    for target_char, target_num in target_map.items():
        if target_char not in message_map.keys():
            return False

        if message_map[target_char] < target_num:
            return False

    return True


def MinWindowSubstring(strArr: List[str]) -> str:
    """It's O(n log n) solution
    Optimal solution is O(n)
    """
    message, target = strArr[0], strArr[1]

    left_idx = 0
    right_idx = len(message) - 1
    candidates = []

    for left_idx in range(len(message) - len(target) + 1):
        for right_idx in range(left_idx + len(target), len(message) + 1):
            candidate_message = message[left_idx:right_idx]
            if is_substring(candidate_message, target):
                candidates.append(candidate_message)

    candidates.sort(key=lambda x: len(x))
    return candidates[0]


if __name__ == "__main__":
    tests = [
        [["ahffaksfajeeubsne", "jefaa"]],
        [["aaffhkksemckelloe", "fhea"]],
        [["aaabaaddae", "aed"]],
        [["aaffsfsfasfasfasfasfasfacasfafe", "fafe"]],
        [["caae", "cae"]],
    ]
    answers = ["aksfaje", "affhkkse", "dae", "fafe", "caae"]

    tester = Tester(MinWindowSubstring)
    tester.test(tests, answers)
