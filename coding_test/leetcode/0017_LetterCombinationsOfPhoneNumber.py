from tester import Tester

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        letter_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        letter_sets = [letter_map[digit] for digit in digits]
        combinations = []

        def create_combinations(indices: List[int]):
            current_combination = "".join(
                [letter_sets[i][indices[i]] for i in range(len(indices))]
            )
            combinations.append(current_combination)

            for i in range(len(indices) - 1, -1, -1):
                if (indices[i] + 1) < len(letter_sets[i]):
                    new_indices = (
                        indices[:i] + [indices[i] + 1] + [0] * (len(indices) - i - 1)
                    )
                    create_combinations(
                        new_indices
                    )
                    break

        create_combinations([0] * len(digits))
        return combinations


if __name__ == "__main__":
    tests = [
        ["23"],
        ["2"],
        [""],
    ]
    answers = [
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        ["a", "b", "c"],
        [],
    ]

    tester = Tester(Solution().letterCombinations)
    tester.test(tests, answers)
