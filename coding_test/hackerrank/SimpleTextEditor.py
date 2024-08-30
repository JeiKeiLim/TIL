from tester import Tester

from typing import List, Tuple


def do_cmd(text: str, cmd: str, data: str, last_states: List[str]) -> Tuple[str, str]:
    if cmd == "1":
        last_states.append(text)
        return text + data, ""
    if cmd == "2":
        last_states.append(text)
        n_delete = int(data)
        return text[:-n_delete], ""
    if cmd == "3":
        print_idx = int(data) - 1
        return text, text[print_idx]

    return last_states.pop(), ""


def simpleTextEditor(queries: List[str]) -> List[str]:
    text = ""
    last_states = [text]
    results = []
    for query in queries:
        cmdata = query.split(" ")
        cmd = cmdata[0]
        data = ""
        if len(cmdata) > 1:
            data = cmdata[1]
        text, result = do_cmd(text, cmd, data, last_states)
        if result != "":
            results.append(result)
    return results


if __name__ == "__main__":
    tests = [
        [["1 abc", "3 3", "2 3", "1 xy", "3 2", "4", "4", "3 1"]],
    ]
    answers = [["c", "y", "a"]]
    tester = Tester(simpleTextEditor)
    tester.test(tests, answers)
