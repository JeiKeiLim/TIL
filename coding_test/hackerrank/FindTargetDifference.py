from tester import Tester

from typing import List


def findDifference(nums: List[int], target: int) -> int:
    nums.sort(reverse=True)
    result = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            diff = nums[i] - nums[j]
            if diff == target:
                result += 1
            elif diff > (target+1):
                break

    return result


if __name__ == "__main__":
    tests = [
        [[1, 3, 5, 8, 6, 4, 2], 2],
        [[
            363374326,
            364147530,
            61825163,
            1073065718,
            1281246024,
            1399469912,
            428047635,
            491595254,
            879792181,
            1069262793,
        ], 3],
        [[1, 5, 3, 4, 2], 2],
    ]
    answers = [5, 0, 3]
    tester = Tester(findDifference)
    tester.test(tests, answers)
