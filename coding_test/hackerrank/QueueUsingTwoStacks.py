from tester import Tester


def solution(query: str) -> str:
    lines = query.split("\n")
    n_query = int(lines[0])
    queue = []

    result = []

    for line in lines[1:]:
        cmdata = line.split(" ")
        cmd = cmdata[0]
        data = -1
        if len(cmdata) == 2:
            data = cmdata[1]

        if cmd == "1":
            queue.append(data)
        elif cmd == "2":
            queue.pop(0)
        else:
            result.append(queue[0])
            print(queue[0])

    return "\n".join(result)


if __name__ == "__main__":
    tests = [
        [
            r"""10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2
3"""
        ]
    ]
    answers = [
        r"""14
14
60"""
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
