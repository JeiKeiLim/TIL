from tester import Tester, generate_random_string
from typing import List

"""
문제 설명
A 회사의 물류창고에는 알파벳 대문자로 종류를 구분하는 컨테이너가 세로로 n 줄, 가로로 m줄 총 n x m개 놓여 있습니다. 
특정 종류 컨테이너의 출고 요청이 들어올 때마다 지게차로 창고에서 접근이 가능한 해당 종류의 컨테이너를 모두 꺼냅니다. 
접근이 가능한 컨테이너란 4면 중 적어도 1면이 창고 외부와 연결된 컨테이너를 말합니다.  
최근 이 물류 창고에서 창고 외부와 연결되지 않은 컨테이너도 꺼낼 수 있도록 크레인을 도입했습니다. 크레인을 사용하면 요청된 종류의 모든 컨테이너를 꺼냅니다.

위 그림처럼 세로로 4줄, 가로로 5줄이 놓인 창고를 예로 들어보겠습니다. 이때 "A", "BB", "A" 순서대로 해당 종류의 컨테이너 출고 요청이 들어왔다고 가정하겠습니다.  
“A”처럼 알파벳 하나로만 출고 요청이 들어올 경우 지게차를 사용해 출고 요청이 들어온 순간 접근 가능한 컨테이너를 꺼냅니다.  
"BB"처럼 같은 알파벳이 두 번 반복된 경우는 크레인을 사용해 요청된 종류의 모든 컨테이너를 꺼냅니다.

위 그림처럼 컨테이너가 꺼내져 3번의 출고 요청 이후 남은 컨테이너는 11개입니다.  
두 번째 요청은 크레인을 활용해 모든 B 컨테이너를 꺼냈음을 유의해 주세요.  
세 번째 요청이 들어왔을 때 2행 2열의 A 컨테이너만 접근이 가능하고 2행 3열의 A 컨테이너는 접근이 불가능했음을 유의해 주세요.

처음 물류창고에 놓인 컨테이너의 정보를 담은 1차원 문자열 배열 storage와  
출고할 컨테이너의 종류와 출고방법을 요청 순서대로 담은 1차원 문자열 배열 requests가 매개변수로 주어집니다.  
이때 모든 요청을 순서대로 완료한 후 남은 컨테이너의 수를 return 하도록 solution 함수를 완성해 주세요.

제한사항
    • 2 ≤ storage의 길이 = n ≤ 50  
      ◦ 2 ≤ storage[i]의 길이 = m ≤ 50  
        ▪ storage[i][j]는 위에서부터 i+1번째 행 j+1번째 열에 놓인 컨테이너의 종류를 의미합니다.  
        ▪ storage[i][j]는 알파벳 대문자입니다.  
    • 1 ≤ requests의 길이 ≤ 100  
      ◦ 1 ≤ requests[i]의 길이 ≤ 2  
      ◦ requests[i]는 한 종류의 알파벳 대문자로 구성된 문자열입니다.  
      ◦ requests[i]의 길이가 1이면 지게차를 이용한 출고 요청을, 2이면 크레인을 이용한 출고 요청을 의미합니다.

테스트 케이스 구성 안내
아래는 테스트 케이스 구성을 나타냅니다. 각 그룹 내의 테스트 케이스를 모두 통과하면 해당 그룹에 할당된 점수를 획득할 수 있습니다.

그룹     | 총점 | 추가 제한 사항  
#1        | 10% | requests에 크레인을 사용한 출고 요청만 존재합니다.  
#2        | 15% | requests에 지게차를 사용한 출고 요청만 존재합니다.  
#3        | 25% | requests에 컨테이너의 종류가 최대 한 번씩 등장합니다. 즉, 이전에 꺼낸 컨테이너 종류를 다시 꺼내지 않습니다.  
#4        | 50% | 제한사항 외 추가조건이 없습니다.

입출력 예  
storage                                requests        result  
["AZWQY", "CAABX", "BBDDA", "ACACA"]     ["A", "BB", "A"]     11  
["HAH", "HBH", "HHH", "HAH", "HBH"]      ["C", "B", "B", "B", "B", "H"]     4  

입출력 예 설명  
입출력 예 #1  
문제 설명의 예시와 같습니다.  
입출력 예 #2  
창고의 초기 상태와 모든 요청을 수행한 뒤의 상태입니다. 남은 컨테이너의 수인 4를 return 해야 합니다.
"""


def solution3(storage: List[str], requests: List[str]) -> int:
    for i in range(len(storage)):
        storage[i] = f"!{storage[i]}!"
    m = len(storage[0])

    storage.insert(0, "!" * m)
    storage.append("!" * m)
    n = len(storage)

    new_storage = []
    for i in range(n):
        new_storage.append(list(storage[i]))

    new_storage = [list(row) for row in storage]

    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    seen = set()

    def is_forklift_reachable(r: int, c: int) -> bool:
        if (r, c) in seen:
            return False
        seen.add((r, c))
        if new_storage[r][c] == "!":
            return True
        elif new_storage[r][c] != " ":
            return False

        for dr, dc in dirs:
            if is_forklift_reachable(r + dr, c + dc):
                return True
        return False

    def use_crane(cargo: str) -> None:
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if new_storage[i][j] == cargo:
                    new_storage[i][j] = " "
                    seen.clear()
                    if is_forklift_reachable(i, j):
                        new_storage[i][j] = "!"

    def use_forklift(cargo: str) -> None:
        candidates = []
        for i in range(n):
            for j in range(m):
                if new_storage[i][j] == cargo:
                    for dr, dc in dirs:
                        seen.clear()
                        if is_forklift_reachable(i + dr, j + dc):
                            candidates.append((i, j))
                            break
        for i, j in candidates:
            new_storage[i][j] = "!"

    for request in requests:
        if len(request) > 1:
            use_crane(request[0])
        else:
            use_forklift(request)

    return sum(new_storage[i][j] not in "! " for i in range(n) for j in range(m))


def solution2(storage: List[str], requests: List[str]) -> int:
    for i in range(len(storage)):
        storage[i] = f"!{storage[i]}!"
    m = len(storage[0])
    storage.insert(0, "!" * m)
    storage.append("!" * m)
    n = len(storage)

    new_storage = [list(row) for row in storage]
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

    for request in requests:
        if len(request) > 1:
            for i in range(1, n - 1):
                for j in range(1, m - 1):
                    if new_storage[i][j] == request[0]:
                        new_storage[i][j] = " "
            continue

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if new_storage[i][j] == "!":
                    new_storage[i][j] = " "

        while True:
            changed = False
            for i in range(1, n - 1):
                for j in range(1, m - 1):
                    if new_storage[i][j] == " ":
                        for dr, dc in dirs:
                            if new_storage[i + dr][j + dc] == "!":
                                new_storage[i][j] = "!"
                                changed = True
                                break
            if not changed:
                break

        candidates = []
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if new_storage[i][j] == request[0]:
                    for dr, dc in dirs:
                        if new_storage[i + dr][j + dc] == "!":
                            candidates.append((i, j))
                            break

        for i, j in candidates:
            new_storage[i][j] = " "

    return sum(new_storage[i][j] not in "! " for i in range(n) for j in range(m))


def solution(storage: List[str], requests: List[str]) -> int:
    for i in range(len(storage)):
        storage[i] = f"!{storage[i]}!"
    m = len(storage[0])

    storage.insert(0, "!" * m)
    storage.append("!" * m)
    n = len(storage)

    new_storage = []
    for i in range(n):
        new_storage.append(list(storage[i]))

    def is_reachable(row: int, col: int, visited: set) -> tuple[bool, set]:
        if (row, col) in visited:
            return False, visited
        if new_storage[row][col] == "!":
            return True, visited
        if new_storage[row][col] != " ":
            return False, visited

        visited.add((row, col))
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            result = is_reachable(row + dr, col + dc, visited.copy())
            if result[0]:
                return result
        return False, visited

    for request in requests:
        if len(request) > 1:
            for i in range(n):
                for j in range(m):
                    if new_storage[i][j] == request[0]:
                        new_storage[i][j] = " "
            continue
        candidates = set()
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if new_storage[i][j] != request:
                    continue
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    result = is_reachable(i + dr, j + dc, set())
                    if result[0]:
                        candidates.add((i, j))
                        for row, col in result[1]:
                            candidates.add((row, col))
                        break
        for i, j in candidates:
            new_storage[i][j] = "!"

    return sum(new_storage[i][j] not in "! " for i in range(n) for j in range(m))


if __name__ == "__main__":
    tests = [
        [["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]],
        [["HAH", "HBH", "HHH", "HAH", "HBH"], ["C", "B", "B", "B", "B", "H"]],
        [
            [
                generate_random_string(50, start_char="A", end_char="Z")
                for _ in range(50)
            ],
            [
                generate_random_string(1, max_n=2, start_char="A", end_char="Z")
                for _ in range(100)
            ],
        ],
    ]
    answers = [11, 4, solution2(tests[-1][0].copy(), tests[-1][1].copy())]

    tester = Tester(solution3, verbose=1)
    tester.test(tests, answers)
