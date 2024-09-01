import time

import random


class RandomizedSet:

    def __init__(self):
        self.idx_map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if self.idx_map.get(val, None) is None:
            self.list.append(val)
            self.idx_map[val] = len(self.list) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if self.idx_map.get(val, None) is not None:
            idx = self.idx_map[val]
            self.list[idx] = self.list[-1]
            self.idx_map[self.list[-1]] = idx
            self.list.pop()
            del self.idx_map[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)
        # return self.list[random.randint(0, len(self.list) - 1)]


if __name__ == "__main__":
    randomSet = RandomizedSet()
    n_test = 100000
    insert_sets = [random.randint(-(n_test // 2), n_test // 2) for _ in range(n_test)]
    remove_sets = [
        random.randint(-(n_test // 2), n_test // 2) for _ in range(int(n_test))
    ]

    t0 = time.monotonic_ns()
    for num in insert_sets:
        randomSet.insert(num)

    t1 = time.monotonic_ns()
    print(f"{len(randomSet.idx_map)=:,d}")

    for num in remove_sets:
        randomSet.remove(num)

    t2 = time.monotonic_ns()
    for i in range(n_test):
        _ = randomSet.getRandom()
    t3 = time.monotonic_ns()

    for i in range(10):
        print(f"{randomSet.getRandom()=:8,d}")

    print(f"{len(randomSet.idx_map)=:,d}")
    print(
        f"Total: {(t3 - t0)/1E+6:,.2f}ms, "
        f"Insert time: {(t1 - t0)/1E+6:,.2f}ms, "
        f"Remove time: {(t2 - t1)/1E+6:,.2f}ms, "
        f"GetRandom time: {(t3 - t2)/1E+6:,.2f}ms"
    )
