from tester import Tester


def towerBreakers(n: int, m: int) -> int:
    if m == 1:
        return 2

    if (n % 2) == 0:
        return 2
    else:
        return 1


if __name__ == "__main__":
    tests = [
        [2, 2],
        [1, 4],
    ]
    answers = [2, 1]
    tester = Tester(towerBreakers)
    tester.test(tests, answers)
