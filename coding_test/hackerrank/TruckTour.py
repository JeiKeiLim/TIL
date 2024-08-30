from tester import Tester

from typing import List


def truckTour(petrolpumps: List[List[int]]) -> int:
    """

    Assumption: First trip to the pump will cost zero petrol
                The truck consume 1 liter of each kilometer

    Args:
        petrompumps: List of
        (0) - the amount of petrol
        (1) distance from the pump to the next pump
    """
    petrol_cost = [p[0] - p[1] for p in petrolpumps]

    for start_idx in range(len(petrolpumps)):
        if petrol_cost[start_idx] < 0:
            continue

        current_petrol = petrol_cost[start_idx]
        for i in range(1, len(petrolpumps)):
            next_stop_idx = (start_idx + i) % len(petrolpumps)
            current_petrol += petrol_cost[next_stop_idx]

            if current_petrol < 0:
                break

        if current_petrol >= 0:
            return start_idx

    return -1


if __name__ == "__main__":
    tests = [
        [[[1, 5], [10, 3], [3, 4]]],
    ]
    answers = [1]
    tester = Tester(truckTour)
    tester.test(tests, answers)
