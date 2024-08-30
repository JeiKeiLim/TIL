from tester import Tester


def isBalanced(s):
    left_to_right = {left: right for left, right in zip("{[(", "}])")}
    right_bracket_stack = []

    for bracket in s:
        if bracket in left_to_right.keys():
            right_bracket_stack.append(left_to_right[bracket])
        else:
            if len(right_bracket_stack) < 1:
                return "NO"

            current_bracket = right_bracket_stack.pop()
            if current_bracket != bracket:
                return "NO"
    return "YES" if len(right_bracket_stack) == 0 else "NO"


if __name__ == "__main__":
    tests = [
        ["{[()]}"],
        ["{[(])}"],
        ["{{[[(())]]}}"],
        ["{{([])}}"],
        ["{{)[](}}"],
        ["{(([])[])[]}"],
        ["{(([])[])[]]}"],
        ["{(([])[])[]}[]"],
        ["}})(({{)"],
        ["()()((){}{}"],
    ]
    answers = ["YES", "NO", "YES", "YES", "NO", "YES", "NO", "YES", "NO", "NO"]
    tester = Tester(isBalanced)
    tester.test(tests, answers)
